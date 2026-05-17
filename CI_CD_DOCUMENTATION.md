# CI/CD Pipeline Documentation

## Overview

This project uses GitHub Actions to implement Continuous Integration and Continuous Deployment (CI/CD).

## Workflow File

Location:

.github/workflows/ci.yml

## Pipeline Stages

### 1. Checkout Repository

The workflow checks out the latest repository code.

### 2. Setup Python

Python 3.12 environment is configured automatically.

### 3. Install Dependencies

Required packages installed:

- fastapi
- uvicorn
- pytest
- httpx

### 4. Automated Testing

The pipeline automatically executes:

```bash
PYTHONPATH=. pytest
