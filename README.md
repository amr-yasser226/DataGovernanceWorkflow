# Data Governance Workflow

This repository contains a full end‑to‑end Data Governance project, covering data profiling, quality control, privacy/security implementation, and a bonus frequency‑analysis attack on a Caesar‑ciphered dataset.

---

## 📂 Repository Structure

```

.
├── .gitignore
├── Data\_encryption.ipynb         # Phase 2: Encryption & Compliance transformations
├── data\_profiling.ipynb          # Phase 0: YData Profiling notebook
├── profilling\_code.ipynb         # Phase 0: Custom profiling notebook
├── profilling\_code.py            # Phase 0: Profiling helper script
├── Quality\_Control.ipynb         # Phase 1: Data cleaning & schema validation
├── README.md                     # ← You are here
├── requirements.txt              # Python dependencies
│
├── attacks
│   └── frequency\_attack.py       # Phase 3 Bonus: Caesar cipher brute‑force attack
│
└── data
├── ssh\_logs\_processed.csv    # Raw dataset (Phase 0 input)
├── Cleaned\_csv.csv           # Phase 1 cleaned dataset
├── encrypted\_data.csv        # Phase 2 encrypted output
├── gdpr\_compliant.csv        # Phase 2 GDPR‑transformed data
├── ccpa\_compliant.csv        # Phase 2 CCPA‑transformed data
├── hipaa\_report.json         # Phase 2 HIPAA‑compliance stub report
├── recovered\_columns.csv     # Phase 3 recovered plaintext columns
└── .gitkeep

````

---

## 🚀 Getting Started

1. **Clone the repo**  
   ```bash
   git clone https://github.com/your‑org/data‑governance‑workflow.git
   cd data‑governance‑workflow
````

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   *Key libraries include:*

   * `pandas`, `numpy`
   * `ydata-profiling` (for automated profiling)
   * `pandera` (for schema validation)
   * `cryptography` (for Fernet encryption)
   * `python-gdpr-utils`, `ccpa`, `Hippo`, `pyTenable`, `SecurityMonkey` (stubs/real for compliance)

3. **Launch Jupyter notebooks**

   ```bash
   jupyter lab
   ```

   Then open and run each notebook in sequence (see Phases below).

---

## 🗓️ Project Phases

### Phase 0 – Data Profiling (3 pts)

* **Goal:** Select a dataset (≥10 000 records, contains textual, numeric, and password fields) and profile it.
* **Notebook(s):**

  * `data_profiling.ipynb` – Automated profiling with YData ProfileReport
  * `profilling_code.ipynb` & `profilling_code.py` – Custom column‑wise statistics and notes
* **Deliverables:**

  * Profiling report (HTML/PDF)
  * Code and issue identification

### Phase 1 – Quality Control (3 pts)

* **Goal:** Clean data, drop duplicates, impute missing values, remove outliers, and validate schema.
* **Notebook:** `Quality_Control.ipynb`
* **Key steps:**

  * Deduplication & null‑imputation (median/mode)
  * IQR‑based outlier removal
  * Schema validation using `pandera`
* **Deliverables:** Cleaned CSV (`data/Cleaned_csv.csv`), code, and documentation.

### Phase 2 – Privacy & Security (5 pts)

* **Goal:** Encrypt sensitive fields, implement GDPR/CCPA/HIPAA procedures.
* **Notebook:** `Data_encryption.ipynb`
* **Encryption:**

  * **Fernet** for `Password`
  * **Caesar cipher** for `Username`
  * **Playfair** (or Caesar) for `City` & `Country`
* **Compliance transformations:**

  * **GDPR** (IP anonymization + pseudonymization stub)
  * **CCPA** (`DoNotSell` flag + `can_sell_data` column)
  * **HIPAA** stub audit (`hipaa_report.json`)
* **Outputs:**

  * `data/encrypted_data.csv`
  * `data/gdpr_compliant.csv`
  * `data/ccpa_compliant.csv`
  * `data/hipaa_report.json`

### Phase 3 – Documentation & Discussion (10 pts)

* **Goal:** Document methodology, present findings, and discuss code.
* **Bonus (3 pts):**

  * **Frequency‑analysis attack** on Caesar‑encrypted columns.
  * **Script:** `attacks/frequency_attack.py`
  * **Outputs:**

    * Recovered columns saved to `data/recovered_columns.csv`
    * Console summary of best shifts, match rates, and sample mismatches.

---

## ▶️ Usage Examples

### Run the Caesar‑attack script

```bash
cd attacks
python frequency_attack.py
```

Results will be written to `../data/recovered_columns.csv` and printed on-screen.

### Open a notebook

From the repo root:

```bash
jupyter lab Data_encryption.ipynb
```

---

## 🛠 Dependencies

Dependencies are recorded in `requirements.txt`. To update:

```bash
pip freeze > requirements.txt
```

---

## 👩‍💻 Team & Credits

* **Your Name**, **Student A**, **Student B**
* Instructor & TA: Dr. XYZ
* Dataset selected: SSH login logs from \[source/link].

---

## 📜 License & Policies

* All code and write‑ups are original and comply with academic honesty policies.
* **AI usage:** No unauthorized AI‑generated content was used.

---