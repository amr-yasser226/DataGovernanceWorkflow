# DataGovernanceWorkflow

## Project Overview

The DataGovernanceWorkflow repository provides a comprehensive pipeline for managing, profiling, encrypting, and auditing sensitive data. It includes encryption routines, data profiling and quality control notebooks, compliance report generation (GDPR, CCPA, HIPAA), and attack simulation scripts. The workflow is organized to separate raw data, analysis notebooks, scripts, and generated reports for clarity and reproducibility.

## Repository Structure

```
DataGovernanceWorkflow/
├── data/              # Raw and processed datasets (CSV, JSON)
├── scripts/           # Standalone Python scripts for encryption, decryption, and attack simulations
├── notebooks/         # Jupyter notebooks for interactive exploration and profiling
├── reports/           # Generated HTML and PDF reports (profiling, compliance, quality control)
├── requirements.txt   # Python package dependencies
├── LICENSE            # Project license
└── README.md          # Project overview and instructions
```

## Data Directory (`data/`)

Contains raw input files and outputs from processing steps:

* `ccpa_compliant.csv`: Data annotated for CCPA compliance (DoNotSell flag and can\_sell\_data column).
* `Cleaned_csv.csv`: Preprocessed dataset used for encryption and profiling.
* `encrypted_data.csv`: Sensitive columns encrypted using Fernet, Caesar, and Playfair ciphers.
* `gdpr_compliant.csv`: Data anonymized for GDPR fields (IP, Username, Password, City, Country).
* `hipaa_report.json`: HIPAA compliance findings in JSON format.
* `recovered_columns.csv`: Columns recovered after brute-force decryption of Caesar-encrypted fields.
* `ssh_logs_processed.csv`: SSH log dataset cleaned and formatted for profiling and validation.

## Scripts Directory (`scripts/`)

* `frequency_attack.py`: Implements an improved brute-force attack on Caesar-ciphered columns, diagnoses mismatches, and applies custom fixes to maximize recovery accuracy.
* `profilling_code.py`: Generates programmatic, text-based profiling of numeric, datetime, and categorical columns, and visualizes login attempt patterns by hour, country, and city.

## Notebooks Directory (`notebooks/`)

1. **Data\_encryption.ipynb**

   * Reads the cleaned CSV and drops index columns.
   * Encrypts `Password` with Fernet.
   * Applies Ceasar cipher (shift=3) to `Username`, `City`, and `Country`.
   * Assigns usernames to random categories for role-permissions testing.
   * Integrates GDPR, CCPA, and HIPAA pseudonymization or stub routines, exporting compliance artifacts.

2. **data\_profiling.ipynb**

   * Uses `ydata_profiling` to generate an HTML profiling report of the SSH log dataset.

3. **profilling\_code.ipynb**

   * Programmatic profiling: computes summary statistics for each column (numeric, datetime, categorical).
   * Builds a pandas DataFrame of profiling information and displays it.
   * Converts and analyzes combined datetime fields and plots login attempts by hour, country, and city.

4. **Quality\_Control.ipynb**

   * Loads the SSH log data and inspects schema.
   * Cleans duplicates and missing values (median for numeric, mode for categorical).
   * Removes outliers based on 1.5 × IQR rule.
   * Validates the cleaned dataset against a Pandera schema, reporting any failures.

## Reports Directory (`reports/`)

* `profiling_report.html`
  Interactive HTML summary of data profiling.
* `profiling_report.pdf`
  PDF export of the profiling report.
* `profiling_data_ssh_logs_process.html`
  HTML rendering of the profiling steps for SSH logs.
* `Phase 1.pdf`
  Quality Control notebook report summarizing cleaning, outlier handling, and schema validation.

## Compliance Workflows

1. **GDPR Compliance**

   * Anonymizes IP addresses and pseudonymizes other sensitive fields using `python_gdpr_utils` if available, else a stub based on MD5 hashing.
   * Outputs `gdpr_compliant.csv`.

2. **CCPA Compliance**

   * Adds `DoNotSell` flag per user with consistent random assignment.
   * Derives `can_sell_data` column.
   * Outputs `ccpa_compliant.csv`.

3. **HIPAA Compliance**

   * Runs HIPAA scanners (`HippoScanner`, `TenableIO`, `SecurityMonkey`) if installed, else returns an empty stub.
   * Outputs `hipaa_report.json`.

## Setup and Usage

1. **Environment Setup**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Run Encryption and Compliance Pipeline**

   ```bash
   python scripts/frequency_attack.py       # Attacks and recovers encrypted fields
   # For notebooks, launch Jupyter Lab:
   jupyter lab notebooks
   ```

3. **Generate Reports**

   * Open `notebooks/data_profiling.ipynb` to regenerate profiling HTML.
   * Run `Quality_Control.ipynb` to validate data schema and update the Phase 1 report.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
