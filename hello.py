import os
from typing import Optional, Dict, Any
from prefect import flow, task
from openai import OpenAI
from dotenv import load_dotenv
from prompts import SYSTEM_PROMPTS, MODEL_CONFIG

# Load environment variables from .env file
load_dotenv()

drive_extract = """
✔checkfirst 
Supercharging regulated service companies with Al powered 
workflows. 
Investor Deck Q3 2025 
Why Now 
A trillion-dollar platform shift ideal for transforming regulated industries 
Al-based quality testing and inspection can increase productivity by up to 50% 
McKinsey 
& Company 
McKinsey Digital: Smartening up 
with Artificial Intelligence 
Market 
Checkfirst revolutionizes regulated companies starting with a large, heavily regulated industry: TICC 
TAM £60bn 
SAM £1bn 
SOM £233m 
Bottom-up market size 
TAM: 610k companies in regulated services industries SAM: 12K TICC companies with $10m+ revenue in Europe/US Average Annual Contract Value: £100k 
£1bn "beachhead" market: 
TICC: Testing, Inspection, Certification & Compliance: 
Ensure compliance for quality, safety and sustainability 
• This industry alone is huge: $260bn, growing $11bn/year Standardised service delivery, following complex regulations Rapid PE consolidation, which accelerates tech adoption Leaders prioritise GenAl to streamline operations 
Sources: ZoomInfo, PitchBook, PWC, Bloomberg, Fortune, Gartner, Checkfirst Universe database 
Al software spending will grow up to 25.2% per year, to $297.9 billion by 2027. 
Gartner 
Forecast Analysis: Al Software Market 
Team 
Meet the repeat founders behind Checkfirst 
An experienced founding team of product and problem obsessed hustlers with deep industry knowledge and experience 
Benjamin 
CEO 
Multi exit CEO/Founder 
Helped scale Nexmo and Agora to unicorn status 
5 years of TICC experience 
Oyvind 
CPO 
CTO-turned-CEO of Poq, Grew to 100+ employees, £20m funding and $2bn GMV. Full Stack Engineer 
Rami 
CTO 
CTO/CEO Elephants Tech. Hired and managed over 400 engineers in 8 years Full Stack Engineer 
Team 
Aman BD - Al Transformation 
Spencer BD - Al Transformation 
Elmera Customer Success 
Sam Product Designer 
Rania Developer 
Assem Developer Tarek Developer Ahmed Developer Omar Developer Islam Developer Ibrahim Developer Ahmed QA Engineer 
Problem 
Regulated companies struggle with "red tape" 
Regulation overhead 
Excessive paperwork and complex manual processes leads to reduced efficiency. 
1 
Expensive operations 
Companies hire large teams and build bespoke systems to deal with the complexity. 
2 
3 
66 
Businesses that fail to adapt and adopt could get undercut on turnaround times as well as costs. They stand to lose market share as a result 
PWC, 2024 
Sizing the prize: What's the real value of Al 
Unable to compete 
This leaves them stuck on aging, bespoke solutions and high cost bases; unable to keep up with competition. 
Solution 
Unlocked by our agents & platform for Al automation. 
66 
With AI, TICC companies can streamline workflows, enhance service delivery, and achieve operational excellence. 
BURE 
RITAS 
Stephane Ponthieux 
$ 
0000 
7828 
BUREAU VERITAS 
ex Bureau Veritas Operations Director 
Al automation 
platform 
Encode regulation into Al-automated workflows, improving productivity 
Human and agent collaboration 
Enable multimodal 
collaboration and 
oversight of agents 
Vertical Al agents and products 
3 proven products & agents that automate industry- 
specific workflows 
Faster & cheaper service delivery 
Faster delivery for improved profitability and customer experience 
Product 
With high-value, industry-specific Al workflows 
Short term plan is to offer products for the full TICC cycle as we grow within each customer. 
ScheduleAl 
• Enable Al-first workflows 
• Allocate & schedule with Al 
• 25+ automation features 
1 
2 
3 
4 
Book 
Plan 
Schedule 
Prepare 
8 
7 
6 
Repeat 
Verify 
Report 
5 
Inspect 
VerifyAl 
• Document data extraction 
• API-first platform 
⚫ LLM foundation models 
InspectAl 
• Digital Checklists 
• API-first platform 
• Al image verification 
Product 
The Checkfirst Suite empowers people, 
eliminating manual work. 
ScheduleAl* 
InspectAl* 
VerifyAl* 
Solution A 
97% service level 
121 allocated visits 
Q4 unallocated visits 
1250km travel time 
0.2 Tonnes CO2 emissions 
48 hotel nights needed 
<Lorem ipsum dolor 
Q 
Health safety quality control and god bless the environment 
sit amet consectetur 
adipiscing. 
Regulatory Compliance 
32 
Lorem ipsum dolor sit amet, consectetur adipiscing 
Certificate request form 
Conform Not conform (Pending) 
NIA 
Lopum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
Simply follow the instructions given. 
Production capacity and control 
> 
32 
Basic Management System 
Conform Not conform 
Pending NIA 
> 
Lopum dolor sit amet, consectetur adipiscing elit, sed do 
Health safety quality control and 
80% 
78% 
78% 
40% 
View 
god bless the environment 
> 
tempor incididunt ut labore et 
4crea 
Laser ipsum dolor sit amet, consectetur adipiscing 
Jan 
Feb 
Mar 
Apr 
Solution B 
95% service level 
99 allocated visits 
Q 6 unallocated visits 
850km travel time 
0.1 Tonnes CO2 emissions 
36 hotel nights needed 
80% 
80% 
78% 
76% 
View 
Jan 
Feb 
Mar 
Apr 
Resource Planning 
- Planning from weeks to minutes 
- Effective rescheduling stops churn 
- 
Win new business by responding faster 
- 
- 
- 
68 
Basic social responsibility 
> 
128 
Lovers ipsum dolor sit amet, consectetur adipiscing 
+ Submit 
Add image 
Next section 
Upload the following documents to verify authenticity 
Please upload your V4001 
Required 
Document upload 
If expiry date 
Is earlier than 
Days Then QRaise an issue 
X 
If coverage amount Less than 
Please upload your V5002 
£9100 Then 
Request v50 
Document upload 
V 
If expiry date 
Is earlier than 
30 Days V 
Then Raise an issue 
X 
If coverage amount Less than £9100 Then + Request v60 
Add criteria 
Add section 
The verification module is ready to analyse data and feed into your system via API! 
← 7/8 
1010 
Report Generation 
Streamline onsite data collection 
GenAl image processing 
Al generated report summaries and analytics 
Document Verification 
- GenAl prompts allow processing from 
days to seconds 
- Better utilisation and happier workforce 
- 
More accuracy 
Click links for demo 
How it works: ScheduleAl 
Scheduling with ScheduleAl is core to customers impacting company goals, people and planet 
Benefits: Win new business. Reschedule to avoid churn. Plan in minutes not weeks. 
Solution A 
97% service level 
117 allocated visits 
Q4 unallocated visits 
45-50% $ 
2350km travel time 
0.4 Tonnes CO2 emissions 
48 hotel nights needed 
Scheduling aligned with company goals 
We empower planners to choose based on company goals and forecasts whether that is financially or ESG driven 
95% service level 
115 allocated visits 
Q 6 unallocated visits 
1850km travel time 
35-40% 
0.2 Tonnes CO2 emissions 
36 hotel nights needed 
Solution B 
Open 
Apr 
80% 
76% 
78% 
40% 
Jan 
Feb 
Mar 
Anot 
80% 
80% 
78% 
76% 
Open 
Jan 
Feb 
Mar 
Apr 
This is our ICP's top priority as it drives them to achieve their financial and ESG goals 
We see Checkfirst as a way to improve efficiencies and productivity within TICC, whilst keeping Trust and standards at their highest. 
David Perez, 
Aenor, Chief BD Officer 
[ 
How it works: Technology 
Using LLMs to power proprietary Al tech 
Our industry-specific Al platform is based on proprietary data and improves with every interaction, creating a self-reinforcing competitive advantage 
Vertical Al Agents 
• Planning Agent dynamically optimizes schedules and allocations using Gen-Al and Constraint Programming. 
• Validation Agent ensures data accuracy and compliance through RAG and intelligent document processing. 
Feedback loops 
• Reinforcement learning drives performance by analyzing outcomes like approvals and completions. 
• Learning loops are integrated into real-world usage, ensuring continuously improving accuracy. 
Al Platform 
• Multimodal workflows let Al agents, humans, and models collaborate on complex tasks. 
• Allocation Model for automating scheduling, using Symbolic Al & Constraint Programming. 
• Dashboards to manage schedules, oversee automations and human-in-the-loop. 
✔checkfirst 
Proprietary models 
• Data partnerships with UKAS and clients create a defensible data moat. 
• Proprietary Al models are tailored to industry-specific workflows, leveraging primary research with 100+ industry professionals. 
How it works: VerifyAl 
Making VerifyAl a one-of-a-kind 'co-pilot' for document processing 
Converting unstructured documents to a structured, verified dataset, at scale 
RAG PLATFORM 
OpenAl 
Vector database 
Document models 
Verification rules 
Foundation models 
Claude 
Gemini 
Policies 
Certificates 
Documents 
Invoices 
Reports 
DATA EXTRACTION PIPELINE 
Prepare 
QUALITY MANAGEMENT 
Verify 
VerifyAl agent 
Feedback API 
Al safety guardrails 
Model evaluation 
Human in the loop 
{...} 
Verified data 
Benefits 
We already outperform the 
market for our leading clients 
And as a result, we are onboarding market leaders every month 
"Checkfirst successfully processed thousands of data points, empowering UKAS to harness GenAl to optimise the service to our clients." 
Georgia Alsop 
Director of Finance & Corporate Services 
UKAS 
1 
2 
3 
4 
Faster planning 
Plan 49,000 hours worth of audits in 12 minutes 
22% less travel 
Reduced travel with 
nearby appointments 
11% higher utilisation Improved internal utilisation by optimising schedules 
42% lower cost 
Reduced subcontractor 
costs 
AENOR 
CONTROLUNION 
Alcumus 
Safer, Healthier, Stronger 
Alcumus 
Safer, Healthier, Stronger 
Competition 
Establishing Checkfirst as The GenAl platform for TICC. 
Why do customers choose CheckfirstAl? 
• Vertical focus: We understand our customer problem intimately & solve high-value, industry-specific pain points. 
• Integration: Unlike off-the-shelf Al tools, we connect seamlessly into existing enterprise workflows and systems 
• Al-first: Checkfirst learns from real-world feedback loops, so the more customers we get, the better our accuracy becomes. 
66 
"Since we started working in this industry, we've been looking for a system like Checkfirst. It has empowered us to allocate more than 90% of our audits automatically in 2 minutes." 
Juan Maties Garcia, Managing Director Control Union Certifications 
Vertical 
Intact Systems 
Checkfirst 
Audit Comply 
Scope 
TIC Systems 
SaaS 
ServiceNow 
Appian 
UiPath 
Horizontal 
Audit Flo 
Al-first 
Celonis 
Hyperscience 
Contextual Al 
Horizontal enterprise players include SFDC, MS, SAP 
Business Model 
We land-and-expand up to £5m ACV 
Usage pricing and multiple products lets us grow current customers to more than £1m ARR 
Ideal Customer Profile 
· 
Testing inspection & certification 
$10m+ revenue in Europe/US 
CEO/MD, CIO, Business unit leaders 
15 Customers 
€100k Av. initial ACV 
5 Weeks go-live 
Validated channels 
• 
Industry events and partnerships 
• Private Equity community 
• LinkedIn outreach 
• Ben and Aman's network 
Usage pricing 
· 
Pay per report, page or booking 
• ScheduleAl: £100K ACV 
VerifyAl: £100K ACV 
InspectAl acts as an add on 
Expansion process 
· 
Upsell ScheduleAl, InspectAl & VerifyAl 
Expand business units & geography 
• 
Increase usage to grow ARR 
Traction 
And our GTM is working with TICC enterprises 
£0-500k contractually agreed revenue in 6 months 
✔checkfirst 
Booked revenue YTD 
£500,000 
£400,000 
£300,000 
£200,000 
£100,000 
£0 
Q1 
Q2 
Services 
ARR 
Q3 forecast 
Ask 
Funding brings Checkfirst to £4m ARR 
We are raising £1.5m+ to reach £4m ARR from 50 customers in the next 18 months 
Key milestones 
Use of funds 
Onboard customers 
35% 
Other 
5% 
30% 
Product development 
30% 
Growth 
Sales and marketing 
Onboard at least 20 
customers in 8 months 
Recruit a VP Marketing Build out GTM delivery and product teams 
Product development 
• 
• 
Consolidate ScheduleAl 
Fully automate VerifyAl 
Build further GenAl stack 
for TICC 
How can I join? 
Our Ask 
Raising up to £1.5m 
• Confirmed strategic investors (tech and G2M expertise) 
Term sheets in place 
Final offers end of July 
• 
Existing investors committed to follow-on - £400k confirmed 
• Minimum ticket of £100k and new investors limited space 
16
"""

context = """Company name: Checkfirst
Airtables notes: AI-powered workflows for regulated companies in testing, inspection, certification and compliance industries
"""

benchmark = """
Here’s a concise benchmarking summary for Checkfirst, comparing reported traction to leading benchmarks. 

---

**Checkfirst Benchmarking Summary: Q3 2025 Deck**

**Stage & Context:**  
- Raising: Likely pre-Series A/Series A (stated raise: £1.5m, £500k YTD booked revenue, aiming for £4m ARR in 18 months).
- Age: Not stated; unclear founding or product launch date. Would need confirmation for growth velocity analysis.

---

### Reported Key Metrics

**ARR / Booked Revenue:**
- £500k YTD booked revenue (as of Q3 2025, historical, “Traction” slide)
- Benchmark: Series A SaaS usually raises at £1.5–5M ARR (OpenView SaaS Benchmarks 2024; Mostly Metrics 2023).
- ⚠️ Mixed — Solid early traction, but current ARR is below typical Series A median. On track for strong projected growth, but historic baseline is low for the round size and target.

**Growth:**
- Goal: Reach £4m ARR from 50 customers in 18 months (projected, “Ask” slide)
- Benchmark: Top-tier SaaS typically shows 2–3x YoY growth pre-Series A (OpenView SaaS Benchmarks 2024)
- ✅ Strong (if achieved) — Would represent >3–4x annualized growth, but this is a forward-looking target, not proven history.

**ACV (Initial/Expansion):**
- £100k average initial ACV (historical, “Business Model”/“Ideal Customer Profile”)
- Benchmark: £50–120k ACV fits well for vertical SaaS in enterprise/regulatory markets (Bessemer “Scaling to $100M ARR” 2022).
- ✅ Strong — High ACV confirms large contracts and matches successful vertical SaaS playbooks.

**Customer Count and Sales Cycle:**
- 15 customers, 5-week average go-live (“Ideal Customer Profile”)
- Benchmark: Series A vertical SaaS median: 10–20 live, contracted customers (Lenny Rachitsky, 2023).
- ✅ Strong — Good commercial validation at this stage; sales cycle is short for enterprise SaaS.

---

### What’s Missing or Unclear

- **Burn rate / cash runway:** Not reported (needed for efficiency/capital intensity benchmarks).
- **Net Revenue Retention (NRR) or Gross Revenue Retention (GRR):** Not reported for existing cohort (critical for SaaS benchmarking).
- **Detailed historical ARR growth:** Only current booked and future goal reported, not full historic trajectory.
- **Customer logo/type breakdown:** Not granular. Would help to validate product-market fit with referenceable enterprise clients.

---

**Overall Benchmarking Verdict:**  
⚠️ Mixed — ACV and customer count are strong for the stage, projected growth is ambitious. However, current ARR is below “classic” Series A benchmarks and absence of unit economics, retention, and burn makes completeness an issue. Would focus diligence on verifying growth velocity (with founding/launch date), SaaS cohort retention, and burn/runway.
"""

research_output = """
The relentless march of artificial intelligence into the hallowed halls of finance presents a fascinating paradox: the promise of unparalleled efficiency clashing with the messy reality of legacy data. At the heart of this contemporary crucible lies Elevate, a nascent venture positioning itself as the indispensable AI-powered data management platform for the private equity world's increasingly prevalent "roll-up" strategies. The fundamental question is not merely whether such a solution is *needed*, but whether Elevate can truly deliver on its audacious promise to transform fragmented acquisition data into a clean, queryable foundation for growth, thereby unlocking the full potential of AI in an industry notoriously resistant to change.

### The Unseen Billions in Data Chaos

The market landscape Elevate seeks to conquer is vast, yet acutely specialized. Its target demographic comprises private equity-backed roll-up companies, those ambitious entities built through a series of strategic acquisitions. To grasp the sheer scale, one must first consider the global private equity ecosystem, estimated to house between 7,000 and 10,000 firms. A conservative estimate suggests that 30% to 50% of these firms actively employ roll-up strategies, translating to a formidable cohort of 2,100 to 5,000 PE firms. Each of these, in turn, typically manages an average of two to three platform companies—the initial acquisitions that serve as the foundation for subsequent add-ons. This yields an estimated 4,200 to 15,000 ideal customer profiles (ICPs) for Elevate.[^1]

If we take a mid-range figure of 10,000 platform companies, and conservatively assign an Average Contract Value (ACV) of $150,000 per year for a specialized enterprise SaaS solution addressing such critical data challenges, the bottom-up Total Addressable Market (TAM) for Elevate stands at an impressive $1.5 billion. This calculation, while inferred, underscores the significant financial commitment private equity firms are willing to make for solutions that genuinely enhance operational efficiency and accelerate value creation.

From a top-down perspective, Elevate operates within the broader, multi-billion-dollar markets of data management, migration, and AI in finance. The global Data Migration Services Market alone was valued at $10.3 billion in 2023, with projections soaring to $31.9 billion by 2030, exhibiting a robust Compound Annual Growth Rate (CAGR) of 17.5%. Similarly, the Data Integration Tools Market, valued at $14.5 billion in 2022, is expected to reach $30.8 billion by 2029, growing at an 11.4% CAGR. Elevate's niche, while precise, is a vital artery within these colossal markets.

The incumbent players in this space are a mixed bag, ranging from the leviathans of technology like Informatica, Talend, Microsoft, AWS, and Google Cloud, to the bespoke services offered by consulting giants such as Accenture, Deloitte, and Riveron. These traditional solutions, while powerful, often lack the specialized AI-first approach tailored specifically for the unique complexities of private equity roll-ups. The market for general data management and migration is mature and somewhat consolidated, yet the specific segment of AI-powered data management for PE roll-ups remains remarkably fragmented and ripe for disruption. There is no apparent overstatement in Elevate's TAM assumptions; rather, the challenge lies in capturing a meaningful share of this clearly defined, albeit inferred, opportunity.

### The Arena of Data Gladiators

In the competitive arena, Elevate faces a diverse array of gladiators, both direct and adjacent. Its direct competitors, as identified by market intelligence, primarily offer general data cleansing and management solutions. Cleanlab, founded in 2021, has raised $30 million in Series A funding for its broad data cleansing platform, yet it conspicuously lacks Elevate's explicit specialization in PE roll-up acquisition data. Similarly, Osmos, a 2019 Seattle-based venture, provides cloud-based data cleansing and migration, having secured $13 million in Series A funding. While performing core functions akin to Elevate, its generalist approach misses the nuanced demands of private equity. YZR, a French AI-based data management platform founded in 2018 with $14.4 million in Series A funding, leverages AI but again, without the laser focus on the PE roll-up niche. Other players like Scrub AI and Sweephy offer components of Elevate's offering, such as data cleansing and preparation, but without the integrated, vertical-specific solution.

The adjacent competitive landscape is dominated by the formidable consulting firms—Accenture, Deloitte, Riveron—which offer bespoke data strategy, migration, and integration services. While these firms bring deep expertise, they typically lack a scalable, dedicated AI-powered platform product. Their solutions are often project-based, resource-intensive, and less amenable to the rapid, repeatable integration cycles demanded by aggressive roll-up strategies. General ETL (Extract, Transform, Load) and data integration tools, such as Informatica and Talend, form the foundational layer for data migration, but they necessitate significant manual effort and customization, precisely the inefficiencies Elevate aims to automate and eliminate.

A notable gap in the market becomes apparent: the precise combination of an AI-powered data management and migration platform specifically tailored for private equity roll-ups. This niche, with its unique challenges of disparate legacy systems, rapid integration timelines, and the imperative for immediate, actionable insights, appears underserved by generalist solutions.

However, a potential area of ambiguity, or perhaps an evolving strategic pivot, lies in the "AI marketplace platform" mentioned in some initial notes. Elevate's public-facing website primarily emphasizes data management and migration. Further investigation reveals that this "AI marketplace" is not a traditional transactional platform but rather an "AI Services" layer built atop Elevate's core data warehouse. This layer provides access to B2B AI services, enabling rapid experimentation with Elevate's own AI agents and those from partner companies. It's a crucial distinction: not a bazaar for AI tools, but an integrated capability to *leverage* AI on clean, consolidated data. This nuance, if not clearly communicated, could lead to misinterpretations of Elevate's core offering and future direction. As for shutdowns in this specific niche, the digital graveyard remains conspicuously quiet, perhaps a testament to the nascent stage of this specialized market.

### The Early Footprints of Traction

Elevate, a company born in 2024, has already secured a $500,000 seed funding round in the same year, notably from Y Combinator. For a venture in its infancy, this backing from one of the most prestigious accelerators in the world serves as a potent validation of its team and underlying concept. Such an early-stage investment is typical for companies still in their pre-product or very early product phases, indicating nascent traction rather than established revenue or user growth. While the funding amount and investor are publicly verifiable, other critical metrics such as customer count, revenue, user growth, or retention remain, as expected, undisclosed. This is not underwhelming for a company at this stage; it simply means the true test of market adoption and scalability lies ahead.

### Riding the AI Tsunami

Elevate's timing appears fortuitous, riding several powerful macro and category trends. The pervasive integration of AI across all enterprise functions is no longer a futuristic fantasy but a present-day imperative. Businesses, including those within private equity portfolios, are scrambling to adopt AI to enhance efficiency, automate tedious tasks, and sharpen decision-making. Private equity itself is undergoing a profound transformation, with an increasing reliance on data analytics for everything from deal sourcing and due diligence to operational improvements and value creation within portfolio companies. The "buy-and-build" or roll-up strategy, a cornerstone of many PE firms, continues its relentless ascent, inherently generating complex data integration challenges across multiple acquired entities.

These trends create significant tailwinds for Elevate. Continuous advancements in AI and machine learning make sophisticated data analysis and automated migration not just possible, but increasingly effective. The sustained high levels of private equity investment and M&A activity fuel a constant demand for efficient post-acquisition integration solutions. Furthermore, PE firms are intensely focused on driving operational efficiencies and extracting data-driven insights to maximize returns, creating a voracious market for tools that streamline these processes.

However, the journey is not without its headwinds. Potential economic downturns could lead to a slowdown in M&A activity and PE investment, directly impacting demand. The management of sensitive financial and operational data across diverse acquired entities raises significant data privacy and security concerns, demanding robust and compliant solutions. Moreover, despite the promise of AI, the inherent complexity and customization required for integrating disparate legacy systems will always pose formidable technical challenges, a reality that no amount of algorithmic wizardry can entirely erase.

### The Uncharted Waters and Lingering Questions

While Elevate presents a compelling thesis, certain aspects warrant closer scrutiny. The initial discrepancy regarding the "AI marketplace platform" versus the clarified "AI Services" layer, while now understood, highlights the importance of precise communication in a high-stakes investment environment. Early-stage ventures, by their very nature, operate with limited public information, making a comprehensive assessment of product-market fit and early impact a delicate dance of inference and informed speculation.

For founders, the questions that demand answers are incisive: What specific, acute pain points for PE-backed roll-ups does Elevate address that existing generalist data integration solutions or even bespoke consulting services fail to solve effectively? How does the "AI Services" layer truly differentiate itself, and what tangible value does it deliver beyond mere data consolidation? What are the current customer numbers, and more importantly, what key performance indicators (KPIs) are being tracked to demonstrate early traction and quantifiable value creation for clients? How does Elevate navigate the labyrinthine complexity and sheer diversity of data structures encountered across various acquired companies within a typical roll-up strategy? Finally, what is the commercialization strategy, and what are the typical sales cycle and Average Contract Value (ACV) for initial customers?

The assumptions underpinning Elevate's potential must be rigorously validated. The problem-solution fit needs confirmation through expert calls with PE partners, CFOs, and operational leaders of portfolio companies, ensuring that Elevate addresses a critical, currently underserved need. The technical feasibility and scalability of Elevate's AI and migration tools must be verified with real-world client data, especially given the varied nature of legacy systems and industries within roll-ups. This demands thorough technical due diligence and candid reference checks with early adopters. If the "AI Services" component is indeed strategic, its viability and the potential for network effects to drive adoption and success must be assessed. Ultimately, the core question remains: does Elevate's specialized focus and AI capabilities provide a sustainable competitive advantage over both the generalist data solution providers and the entrenched consulting engagements?

In the grand theater of capital and innovation, Elevate stands at a pivotal juncture. It is a testament to the relentless pursuit of efficiency, a digital alchemist promising to transmute the lead of fragmented data into the gold of actionable intelligence. The future of private equity, increasingly reliant on data-driven decisions and AI-powered insights, hinges on solutions like Elevate. Whether it can navigate the treacherous currents of market adoption and technical complexity to truly elevate its clients, and itself, remains the most intriguing question of all.



[^1]: Elevate works with leading private equity backed roll ups and platforms who are actively making acquisitions [Elevate](https://useelevate.dev/)
"""


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
def draft() -> str:
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
def benchmark_light(step_1_output: str) -> str:
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


@flow(name="Memo Generation Flow", log_prints=True)
def memo_generation(
    company_name: str = "Checkfirst",
    company_context: Optional[str] = None,
    deck_extract: Optional[str] = None,
    research_data: Optional[str] = None,
    benchmark_data: Optional[str] = None,
):
    """
    Main flow that orchestrates the 3-step text generation process.
    Each step calls OpenRouter API and may use outputs from previous steps.

    Args:
        company_name: Name of the company being analyzed
        company_context: Additional context about the company (optional)
        deck_extract: Extracted content from company deck (optional)
        research_data: Deep research output (optional)
        benchmark_data: Benchmark analysis data (optional)
    """
    # Use provided data or fall back to defaults
    _context = company_context if company_context else context
    _drive_extract = deck_extract if deck_extract else drive_extract
    _research_output = research_data if research_data else research_output
    _benchmark = benchmark_data if benchmark_data else benchmark

    print(f"Processing memo for: {company_name}")

    # Execute tasks in sequence, passing data between them
    draft_output = draft()
    benchmark_light_output = benchmark_light(draft_output)
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

    return final_output


if __name__ == "__main__":
    memo_generation()
