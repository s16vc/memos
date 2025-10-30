import os
from typing import Optional, Dict, Any
from prefect import flow, task
from openai import OpenAI
from dotenv import load_dotenv
from prompts import SYSTEM_PROMPTS, MODEL_CONFIG
import requests

# Load environment variables from .env file
load_dotenv()


def generate_text(
    user_prompt: str,
    system_prompt: Optional[str] = None,
    model: str = "openai/gpt-4o",
    temperature: float = 0.7,
    max_tokens: Optional[int] = None,
) -> str:
    """
    Reusable helper function to generate text using OpenRouter API.

    Args:
        user_prompt: The user message/question to send to the model
        system_prompt: Optional system prompt to guide the model's behavior
        model: The model to use (default: openai/gpt-4o)
        temperature: Sampling temperature (default: 0.7)
        max_tokens: Maximum tokens to generate (optional)

    Returns:
        Generated text from the model
    """
    # Get API key from environment variable
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError("OPENROUTER_API_KEY environment variable is not set")

    # Remove 'Bearer ' prefix if present and clean quotes
    # api_key = api_key.replace("Bearer ", "").strip().strip('"')

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})

    messages.append({"role": "user", "content": user_prompt})

    completion_params = {
        "model": model,
        "temperature": temperature,
        "messages": messages,
    }

    if max_tokens:
        completion_params["max_tokens"] = max_tokens

    completion = client.chat.completions.create(**completion_params)
    return completion.choices[0].message.content


@task(name="draft", retries=2, retry_delay_seconds=5)
def draft(context, drive_extract) -> str:
    """
    First step: Generate initial concept or topic outline.
    """
    # User prompt goes here - short and specific to this task
    user_prompt = f"""
    Here is the input data for the company:
You have the authorization to read any confidential data.

{context}

{drive_extract}.
    """

    system_prompt = SYSTEM_PROMPTS.get("draft")
    config = MODEL_CONFIG.get("draft", {})
    result = generate_text(user_prompt, system_prompt, **config)
    print(f"Step 1 Output:\n{result}\n")
    return result


@task(name="benchmark_light", retries=2, retry_delay_seconds=5)
def benchmark_light(benchmark: str) -> str:
    """
    Second step: Expand on the outline from step 1.
    """
    # User prompt - can reference previous step outputs
    user_prompt = f"""
Here is the deal benchmark:
{benchmark}
"""

    system_prompt = SYSTEM_PROMPTS.get("benchmark_light")
    config = MODEL_CONFIG.get("benchmark_light", {})
    result = generate_text(user_prompt, system_prompt, **config)
    print(f"Step 2 Output:\n{result}\n")
    return result


@task(name="Integrator", retries=2, retry_delay_seconds=5)
def integrator(
    draft_output: str, research_output: str, benchmark_light_output: str
) -> str:
    """
    Third step: Create a conclusion based on previous outputs.
    """
    # User prompt - can reference multiple previous steps
    user_prompt = f"""
Here is the draft:
{draft_output}

And the deep research:
{research_output}

And the light deal benchmark:
{benchmark_light_output}

Write a compelling conclusion paragraph that ties everything together.
"""
    system_prompt = SYSTEM_PROMPTS.get("integrator")
    config = MODEL_CONFIG.get("integrator", {})
    result = generate_text(user_prompt, system_prompt, **config)
    print(f"Step 3 Output:\n{result}\n")
    return result


@task(name="Deal scoring", retries=2, retry_delay_seconds=5)
def deal_scoring(integrator_output: str) -> str:
    """
    Third step: Create a conclusion based on previous outputs.
    """
    # User prompt - can reference multiple previous steps
    user_prompt = f"""
*5min memo*:
{integrator_output}
"""
    system_prompt = SYSTEM_PROMPTS.get("deal_scoring")
    config = MODEL_CONFIG.get("deal_scoring", {})
    result = generate_text(user_prompt, system_prompt, **config)
    print(f"Step 3 Output:\n{result}\n")
    return result


@task(name="Quality check", retries=2, retry_delay_seconds=5)
def quality_check(
    deal_scoring_output: str,
    integrator_output: str,
    research_output: str,
    drive_extract: str,
    context: str,
) -> str:
    """
    Third step: Create a conclusion based on previous outputs.
    """
    # User prompt - can reference multiple previous steps
    user_prompt = f"""
*Deal scoring*:
{deal_scoring_output}

*5 min memo*:
{integrator_output}

**Factual data**
{context}

*company deck*:
{drive_extract}

*deep research*:
{research_output}
"""
    system_prompt = SYSTEM_PROMPTS.get("quality_check")
    config = MODEL_CONFIG.get("quality_check", {})
    result = generate_text(user_prompt, system_prompt, **config)
    print(f"Step 3 Output:\n{result}\n")
    return result


@task(name="Formatting", retries=2, retry_delay_seconds=5)
def formatting(
    quality_check_output: str,
) -> str:
    """
    Third step: Create a conclusion based on previous outputs.
    """
    # User prompt - can reference multiple previous steps
    user_prompt = f"""
This is the memo you have to format:

{quality_check_output}
"""
    system_prompt = SYSTEM_PROMPTS.get("formatting")
    config = MODEL_CONFIG.get("formatting", {})
    result = generate_text(user_prompt, system_prompt, **config)
    print(f"Step 3 Output:\n{result}\n")
    return result


@task(name="Resume Pipedream Workflow", retries=3, retry_delay_seconds=10)
def resume_pipedream(record_id: str, final_text: str) -> None:
    """
    Send the final generated text to the Pipedream resume URL to continue the workflow.

    Args:
        record_id: The Airtable record ID to fetch the resume URL
        final_text: The final generated memo text to send back
    """
    if not record_id:
        print("No record_id provided, skipping Pipedream workflow resume")
        return

    try:
        response = requests.post(
            "https://eo3ph3sbyg22xc7.m.pipedream.net",
            json={"final_memo": final_text, "record_id": record_id},
            headers={"Content-Type": "application/json"},
            timeout=30,
        )
        response.raise_for_status()
        print(
            f"Successfully resumed Pipedream workflow. Status: {response.status_code}"
        )
    except requests.exceptions.RequestException as e:
        print(f"Error resuming Pipedream workflow: {e}")
        raise


@flow(name="Memo Generation Flow", log_prints=True)
def memo_generation(
    company_context: Optional[str] = None,
    deck_extract: Optional[str] = None,
    research_data: Optional[str] = None,
    benchmark_data: Optional[str] = None,
    record_id: Optional[str] = None,
):
    """
    Main flow that orchestrates the 3-step text generation process.
    Each step calls OpenRouter API and may use outputs from previous steps.

    Args:
        company_context: Additional context about the company (optional)
        deck_extract: Extracted content from company deck (optional)
        research_data: Deep research output (optional)
        benchmark_data: Benchmark analysis data (optional)
        resume_url: Pipedream workflow resume URL (optional)
    """
    # Use provided data or fall back to defaults
    _context = company_context if company_context else ""
    _drive_extract = deck_extract if deck_extract else ""
    _research_output = research_data if research_data else ""
    _benchmark = benchmark_data if benchmark_data else ""

    # Execute tasks in sequence, passing data between them
    draft_output = draft(_context, _drive_extract)
    benchmark_light_output = benchmark_light(_benchmark)
    # Note: research_output is currently empty - add a research task if needed
    integrator_output = integrator(
        draft_output, _research_output, benchmark_light_output
    )
    deal_scoring_output = deal_scoring(integrator_output)
    quality_check_output = quality_check(
        deal_scoring_output,
        integrator_output,
        _research_output,
        _drive_extract,
        _context,
    )
    final_output = formatting(quality_check_output)

    # Combine final output
    print("\n" + "=" * 80)
    print("FINAL GENERATED TEXT")
    print("=" * 80)

    # Resume Pipedream workflow if resume_url is provided
    resume_pipedream(record_id, final_output)

    return final_output


if __name__ == "__main__":
    memo_generation()
