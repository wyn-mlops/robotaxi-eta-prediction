# Model & Data Provenance
This document links code (Git), data (DVC), and experiments (MLflow) for reproducibility.
| Data Version | Git Tag | MLflow Run ID |
| :--- | :--- | :--- |
| v1.0 | Initial commit | `5ecf8bdc53d642309f29329a2ccfbb74` |
| v2.0 | `v2.0` | `N/A (trained on member A's local machine)` |
**How to reproduce:**
Checkout the Git tag, run `dvc pull` to fetch data from Azure, and run `python train.py`.
