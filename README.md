# Lobo Projection (Robotaxi ETA)

This project is a Machine Learning-powered application designed to predict the Estimated Time of Arrival (ETA) for Robotaxis. The project fully integrates DevOps and MLOps practices, including automated CI/CD pipelines, containerization with Docker, and experiment tracking.

## 🚀 CI/CD Pipeline Workflow

Our development process follows a strict branching strategy and automated pipeline flow from code commit to deployment.

### Code Flow: Commit → Build → Test → Staging → Prod

1. **Commit**: Developers write code locally and commit to `feature/*` branches.
2. **Pull Request (PR)**: PRs are created to merge into `dev`, `staging`, or `main`. The CI pipeline automatically runs.
3. **Build & Test (CI)**: Upon a PR or push, GitHub Actions builds the Docker image and runs the full test suite along with linting/static analysis. If any step fails, the PR cannot be merged.
4. **Staging Deployment (CD)**: When code is merged into the `staging` branch, the Staging CD pipeline triggers. It uses GitHub Secrets to generate a staging `.env` file and builds the staging Docker image.
5. **Production Deployment (CD)**: When code is merged into the `main` branch, the Production CD pipeline triggers. It uses production-specific GitHub Secrets to generate the production `.env` file and builds the production Docker image.

### Branch & Pipeline Trigger Mapping

| Branch | Triggered Pipeline | Actions Performed | Required Status |
| :--- | :--- | :--- | :--- |
| `feature/*` | PR to `dev` | CI (Test, Lint, Build) | Required to merge |
| `dev` | PR / Push | CI (Test, Lint, Build) | Required to merge |
| `staging` | Push (Merge) | CI + **Staging CD** (.env generation, Docker build) | Must pass CI first |
| `main` | Push (Merge) | CI + **Production CD** (.env generation, Docker build) | Must pass CI first |

## 📂 Project Structure

- `app/`: Service entrypoint and API server.
- `ml/`: Training scripts, MLflow tracking, and dataset documentation.
- `.github/workflows/`: GitHub Actions CI/CD configurations.
- `tests/`: Automated test suites.
- `Dockerfile`: Docker configuration for the application.
- `DEPLOYMENT.md`: Detailed documentation on the deployment process.

## 🛠️ How to Run Locally

Follow these steps to set up the project locally and run the application:

1. **Clone the repository and install dependencies:**
    git clone https://github.com/wyn-mlops/robotaxi-eta-prediction.git
    cd robotaxi-eta-prediction
    pip install -r requirements.txt

2. **Generate the dataset (v1) and pull DVC data:**
    python make_data.py
    dvc pull
    *(Note: You need the Azure credentials configured via dvc remote to pull the data.)*

3. **Train the Machine Learning model:**
    python train.py
    *(This will generate the model.pkl required for the API and log experiments to MLflow).*

4. **Start the FastAPI server:**
    uvicorn app.main:app --reload
    The application will be available at http://127.0.0.1:8000.

For more details on deployment, please refer to [DEPLOYMENT.md](DEPLOYMENT.md).
