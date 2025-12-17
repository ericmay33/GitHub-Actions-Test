# GitHub Actions Test Repository

This repository contains intentionally broken GitHub Actions workflows for DevOps testing purposes.

## Workflow Errors Included

1. **Syntax Error** - Python syntax error in shell command
2. **Failing Tests** - Pytest tests that always fail
3. **Missing Dependency** - Import errors due to missing packages
4. **Environment Variable Error** - Missing required secrets
5. **Timeout Error** - Job that exceeds timeout limit

## Setup Instructions

1. Create a new GitHub repository
2. Add all files as shown in the structure
3. Push to GitHub
4. Watch the Actions tab for failures

## Testing with Your Code

Update `TEST_REPO_URL` in your Python script:

```python
TEST_REPO_URL = "https://github.com/YOUR_USERNAME/GitHub-Actions-Test"
```
