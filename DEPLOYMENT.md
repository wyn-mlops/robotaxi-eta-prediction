# Deployment Guide

This document outlines the deployment strategy and environment configurations for the Lobo Project (Robotaxi ETA). 

## 🌍 Environments

We maintain two separate environments to ensure stability and safe releases:
1. **Staging Environment**: Used for testing new features before they go live. Triggered by merges/pushes to the `staging` branch.
2. **Production Environment**: The live environment. Triggered by merges/pushes to the `main` branch.

## 🔐 Configuration & Secrets Management

We do not hardcode environment variables in the code. Instead, we inject them dynamically during the GitHub Actions CD process.

### .env Generation
During the CD pipeline (handled in `.github/workflows/staging.yml` and `.github/workflows/prod.yml`), the runner creates a `.env` file on the fly using GitHub Secrets.

- **Staging Secrets**: Configured in the `staging` GitHub Environment (e.g., `STAGING_API_URL`).
- **Production Secrets**: Configured in the `production` GitHub Environment (e.g., `PROD_API_URL`).

### Docker Image Build
Once the `.env` file is generated, the pipeline builds the Docker image. 
- Staging Image: Tagged as `robotaxi-eta-staging:<commit-sha>`
- Production Image: Tagged as `robotaxi-eta-prod:<commit-sha>`

## 🔄 Deployment Workflow

1. **Developer pushes to `staging`**: 
   - CI pipeline runs tests.
   - CD pipeline creates `.env` from Staging Secrets.
   - Docker image is built and tagged for staging.
2. **Verification**: The team verifies the staging environment. 
3. **Merge to `main`**: 
   - CI pipeline runs tests again.
   - CD pipeline creates `.env` from Production Secrets.
   - Docker image is built and tagged for production.

*Note: As per the project requirements, the actual deployment to a cloud host (e.g., AWS/Azure) is simulated by building the final Docker image successfully.*

## ⏪ Rollback Strategy (Optional)
If a production build fails or contains bugs, we can revert the `main` branch to the previous stable commit hash and re-trigger the CD pipeline to build the previous version of the Docker image.