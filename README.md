# Healthcare Data Basics

Python practice projects that combine nursing experience with data analysis.
Each script uses a small **synthetic** hospital dataset (no real patient data) to practice a core analytics skill.

## Scripts

| Script | What it does | Skills |
|---|---|---|
| `01_hospital_dataset_exploration.py` | Builds a basic hospital dataset and plots patients per department | DataFrames, value counts, bar charts |
| `02_data_cleaning.py` | Handles missing values and compares length of stay by department | Missing data, imputation, groupby |
| `03_correlation_analysis.py` | Tests the relationship between age and length of stay | Correlation, scatter plots |
| `04_clinical_questions_summary.py` | Frames a clinical question and answers it with summary statistics | describe(), groupby, interpretation |
| `05_bed_occupancy_analysis.py` | Analyzes length of stay by age and diagnosis across 20 patients | EDA, correlation, grouped charts |

## How to run

```bash
pip install pandas matplotlib
python 01_hospital_dataset_exploration.py
```

## Note on data

All datasets are invented for learning purposes. They do not represent any real hospital or patient.

## Next

A larger supply-readiness project built on simulated hospital data:
[hajj-supply-readiness](https://github.com/yosras-dotcomAi/hajj-supply-readiness)

## Tools

Python, pandas, matplotlib
