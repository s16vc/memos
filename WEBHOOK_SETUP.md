# Webhook Setup Guide for Memo Generation Flow

## Overview
This guide explains how to trigger your `memo_generation` flow using Prefect Cloud webhooks.

## Prerequisites
- Prefect Cloud account (webhooks are a Cloud feature)
- Flow deployed and running

## Step 1: Deploy Your Flow

First, start your deployment server:

```bash
# Activate your virtual environment
source .venv/bin/activate

# Run the deployment
python deploy.py
```

This will keep running and listening for flow triggers.

## Step 2: Create a Webhook in Prefect Cloud

### Option A: Using Prefect Cloud UI

1. Go to your Prefect Cloud workspace
2. Navigate to **Webhooks** section
3. Click **Create Webhook**
4. Configure:
   - **Name**: `trigger-memo-generation`
   - **Description**: `Webhook to trigger memo generation flow`
   - **Template**: Use the template below

### Option B: Using Prefect CLI

```bash
prefect cloud webhook create trigger-memo-generation \
    --description "Triggers memo generation flow" \
    --template '{ "event": "memo.generation.trigger", "resource": { "prefect.resource.id": "memo-generation-webhook" } }'
```

## Webhook Templates

### Simple Static Template
If you just want to trigger the flow without any parameters:

```json
{
    "event": "memo.generation.trigger",
    "resource": {
        "prefect.resource.id": "memo-generation-webhook",
        "prefect.resource.name": "Memo Generation Webhook"
    }
}
```

### Dynamic Template (with POST data)
If you want to pass data via POST request:

```json
{
    "event": "memo.generation.trigger",
    "resource": {
        "prefect.resource.id": "memo-generation-webhook",
        "prefect.resource.name": "Memo Generation Webhook",
        "trigger_source": "{{ body.source|default('unknown') }}",
        "company_name": "{{ body.company_name|default('') }}"
    }
}
```

## Step 3: Create an Automation

After creating the webhook, you need to create an automation to run your flow when the webhook event is received.

### Using Prefect Cloud UI:

1. Go to **Automations** → **Create Automation**
2. Configure:
   - **Trigger**:
     - Type: `Event`
     - Event: `memo.generation.trigger`
     - Resource ID: `memo-generation-webhook`
   - **Action**:
     - Type: `Run a deployment`
     - Deployment: Select `memo_generation/memo-generation-webhook`

### Using Prefect CLI:

```bash
# First, get your deployment ID
prefect deployment ls

# Then create the automation (replace <deployment-id> with actual ID)
prefect automation create \
    --name "Webhook Triggered Memo Generation" \
    --trigger '{"type": "event", "match": {"prefect.resource.id": "memo-generation-webhook"}, "expect": ["memo.generation.trigger"]}' \
    --action '{"type": "run-deployment", "deployment_id": "<deployment-id>"}'
```

## Step 4: Trigger Your Webhook

Once the webhook URL is created (e.g., `https://api.prefect.cloud/hooks/AERylZ_uewzpDx-8fcweHQ`), you can trigger it:

### Simple GET request:
```bash
curl https://api.prefect.cloud/hooks/YOUR-WEBHOOK-ID
```

### POST request with data:
```bash
curl -X POST https://api.prefect.cloud/hooks/YOUR-WEBHOOK-ID \
    -H "Content-Type: application/json" \
    -d '{
        "source": "external_system",
        "company_name": "Checkfirst"
    }'
```

### POST with form data:
```bash
curl -X POST https://api.prefect.cloud/hooks/YOUR-WEBHOOK-ID \
    -d "source=external_system" \
    -d "company_name=Checkfirst"
```

## Step 5: Monitor and Debug

### Check webhook events:
```bash
prefect cloud webhook ls
prefect cloud webhook get YOUR-WEBHOOK-NAME
```

### Monitor for failures:
In Prefect Cloud UI, watch for `prefect-cloud.webhook.failed` events in the Event Feed if something goes wrong.

## Troubleshooting

1. **Webhook returns 400**: Check your template syntax - it must produce valid JSON
2. **Flow not triggering**: Verify the automation is active and the event name matches
3. **Deployment not found**: Make sure `deploy.py` is running

## Security (Pro/Enterprise)

For enhanced security, associate a service account with your webhook:

```bash
# Create or use existing service account
prefect cloud service-account create webhook-service-account

# Associate with webhook and use API key in requests
curl -X POST https://api.prefect.cloud/hooks/YOUR-WEBHOOK-ID \
    -H "Authorization: Bearer <service-account-api-key>" \
    -H "Content-Type: application/json" \
    -d '{"source": "secure_system"}'
```

## Example Integration

Here's a complete example of triggering from a Python script:

```python
import requests

webhook_url = "https://api.prefect.cloud/hooks/YOUR-WEBHOOK-ID"

# Trigger the memo generation
response = requests.post(
    webhook_url,
    json={
        "source": "automated_process",
        "company_name": "Checkfirst"
    }
)

if response.status_code == 204:
    print("Webhook triggered successfully!")
else:
    print(f"Error: {response.status_code}")
```
