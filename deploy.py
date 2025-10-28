"""
Deployment configuration for memo generation flow
This creates a deployment that can be triggered by webhooks
"""

from prefect.runner.storage import GitRepository
from hello import memo_generation

if __name__ == "__main__":
    # Create a deployment that runs on demand (triggered by webhooks/automations)
    # Using GitHub as the source repository with dependency installation
    memo_generation.from_source(
        source=GitRepository(
            url="https://github.com/s16vc/memos.git",
            branch="master",
        ),
        entrypoint="hello.py:memo_generation",
    ).deploy(
        name="memo-generation-webhook",
        tags=["webhook", "memo-generation"],
        description="Memo generation flow triggered via webhooks",
        work_pool_name="mainPool",
        job_variables={
            "pip_install_requirements": "requirements.txt"
        }
    )
