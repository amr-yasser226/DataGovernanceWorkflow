**Data Governance Workflow**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](#license)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-green.svg)](#prerequisites)

---

## 📄 Overview

This repository implements a comprehensive, end-to-end **Data Governance** framework for tabular datasets. The project is organized into four major phases:

1. **Data Profiling** – Exploratory analysis and automated reporting
2. **Quality Control** – Data cleaning, outlier removal, and schema validation
3. **Privacy & Security** – Field-level encryption and compliance transformations (GDPR, CCPA, HIPAA)
4. **Documentation & Discussion** – Methodology write‑up and security analysis, including an optional frequency‑analysis attack on Caesar‑ciphered data

Alongside the core workflow, a bonus script demonstrates a frequency‑analysis attack to recover encrypted columns.

---

## 📑 Table of Contents

* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Repository Structure](#repository-structure)
* [Usage](#usage)
* [Project Phases](#project-phases)
* [Examples](#examples)
* [Dependencies](#dependencies)
* [Contributing](#contributing)
* [Authors & Credits](#authors--credits)
* [License](#license)

---

## 🔧 Prerequisites

* **Python 3.8+**
* [Git](https://git-scm.com/)
* [JupyterLab](https://jupyter.org/)

---

## 🚀 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-org/data-governance-workflow.git
   cd data-governance-workflow
   ```

2. **Install dependencies**

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

3. **Launch JupyterLab**

   ```bash
   jupyter lab
   ```

---

## 📂 Repository Structure

```text
├── .gitignore
├── data_profiling.ipynb        # Phase 0: Automated profiling with YData
├── profiling_helpers.py        # Phase 0: Custom profiling functions
├── quality_control.ipynb       # Phase 1: Cleaning & schema validation
├── data_encryption.ipynb       # Phase 2: Encryption & compliance transforms
├── attacks/
│   └── frequency_attack.py     # Bonus: Frequency‑analysis on Caesar cipher
├── data/
│   ├── ssh_logs_processed.csv  # Raw input dataset
│   ├── Cleaned_csv.csv         # Phase 1 output
│   ├── encrypted_data.csv      # Phase 2 encrypted output
│   ├── gdpr_compliant.csv      # Phase 2 GDPR transform
│   ├── ccpa_compliant.csv      # Phase 2 CCPA transform
│   ├── hipaa_report.json       # Phase 2 HIPAA audit stub
│   └── recovered_columns.csv   # Phase 3 recovered data
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation (this file)
```

---

## ⚙️ Usage

### 1. Execute Notebooks in Sequence

Open each notebook in JupyterLab and follow the phase-specific instructions:

* **Phase 0**: `data_profiling.ipynb`
* **Phase 1**: `quality_control.ipynb`
* **Phase 2**: `data_encryption.ipynb`
* **Phase 3**: Document your findings and run the bonus attack

### 2. Run the Frequency‑Analysis Attack (Bonus)

```bash
cd attacks
python frequency_attack.py
```

Output is saved to `../data/recovered_columns.csv` and summarized in the console.

---

## 🗂 Project Phases

### Phase 0 – Data Profiling

**Objective**: Generate summary statistics, detect anomalies, and produce a profiling report.

* **Automated**: `data_profiling.ipynb` uses **YData Profiling**
* **Custom**: `profiling_helpers.py` computes bespoke metrics
* **Deliverables**: Interactive HTML/PDF report, code notebooks

### Phase 1 – Quality Control

**Objective**: Clean dataset by handling duplicates, imputing missing values, removing outliers, and enforcing schema.

* **Notebook**: `quality_control.ipynb`
* **Key Steps**:

  * Deduplication & Null‑value imputation (median/mode)
  * IQR‑based outlier detection and removal
  * Schema enforcement via **Pandera**
* **Output**: `data/Cleaned_csv.csv`

### Phase 2 – Privacy & Security

**Objective**: Encrypt sensitive fields and apply compliance rules (GDPR, CCPA, HIPAA).

* **Notebook**: `data_encryption.ipynb`
* **Encryption Methods**:

  * **Fernet** for passwords
  * **Caesar cipher** for usernames
  * **Playfair (or Caesar)** for location data
* **Compliance**:

  * **GDPR**: IP anonymization + pseudonymization stub
  * **CCPA**: Do‑Not‑Sell flag + `can_sell_data` column
  * **HIPAA**: Stub audit report (`hipaa_report.json`)
* **Outputs**:

  * `data/encrypted_data.csv`
  * `data/gdpr_compliant.csv`
  * `data/ccpa_compliant.csv`
  * `data/hipaa_report.json`

### Phase 3 – Documentation & Discussion

**Objective**: Present methodologies, discuss results, and optionally demonstrate a security attack.

* Write a comprehensive project report
* Include visualizations and code snippets
* **Bonus**: Frequency‑analysis attack script (`attacks/frequency_attack.py`)

---

## 🛠 Dependencies

All required packages are listed in `requirements.txt`. To update dependencies:

```bash
pip freeze > requirements.txt
```

---

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request. For major changes, open an issue first to discuss your ideas.

---

## 👥 Authors & Credits

* **Project Team**: Your Name, Student A, Student B
* **Instructor & TA**: Dr. XYZ
* **Data Source**: SSH login logs from \[Original Source Link]

---

## 📜 License

This project is licensed under the **MIT License**. See [LICENSE](./LICENSE) for details.

---
