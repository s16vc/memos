"""
Deployment configuration for memo generation flow
This creates a deployment that can be triggered by webhooks
"""
from hello import memo_generation

if __name__ == "__main__":
    # Create a deployment that runs on demand (triggered by webhooks/automations)
    memo_generation.serve(
        name="memo-generation-webhook",
        tags=["webhook", "memo-generation"],
        description="Memo generation flow triggered via Prefect Cloud webhooks"
    )
