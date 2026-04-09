
---

## Project Structure

```
BigDataThesis/
├── EDA/
│   └── primary_data_analysis.ipynb   # Main EDA notebook (business dataset)
├── utils/
│   └── JSONtoCSV.py                  # Yelp JSON → CSV converter utility
└── README.md
```

---

## Dataset

**Yelp Academic Dataset** — a public dataset containing:

| File | Description |
|------|-------------|
| `yelp_academic_dataset_business.json` | Business metadata, attributes, categories, hours |
| `yelp_academic_dataset_review.json` | Full review text with star ratings |
| `yelp_academic_dataset_user.json` | User profiles and social graph |
| `yelp_academic_dataset_tip.json` | Short tips left by users |
| `yelp_academic_dataset_checkin.json` | Business check-in timestamps |

---

## Completed Work

### Utility — `utils/JSONtoCSV.py`

Converts all Yelp JSON files to CSV format for downstream analysis.

- Flattens nested dictionaries into `parent_child` columns
- Joins list values using `/_/` as a separator
- Batch converts an entire directory in one call

```python
from utils.JSONtoCSV import YelpJsonToCsvConverter

converter = YelpJsonToCsvConverter(
    source_directory="yelp_data/",
    output_directory="yelp_csv/"
)
converter.convert_all()
```

---

### EDA — `EDA/primary_data_analysis.ipynb`

Exploratory data analysis focused on the **business** dataset.

#### Feature Engineering

| Feature Group | Details |
|---------------|---------|
| **Categories** | Dummy vectors; rare categories (< 500 occurrences) collapsed into a single `rare` column |
| **Cities** | One-hot encoded across 11 cities; low-frequency states (NY, SC, VT) removed |
| **Attributes** | Boolean attributes → 1/0; categorical → ordinal; nested attrs (Ambience, Parking, GoodForMeal) parsed individually |
| **Operating Hours** | Parsed into `{Day}_start_time` + `{Day}_op_hrs` for all 7 days (14 columns total) |

#### Exploratory Analysis

- Average rating and review count heatmaps across:
  - **City × Category** (top 11 cities, top 20 categories)
  - **Category × General Attributes** (top 20 categories, top 10 attributes)
  - **Restaurant Category × Specific Attributes** (top 16 restaurant categories, top 10 specific attributes)
- Comparison of business metrics **with** vs **without** key attributes

#### Baseline Models

| Model | Type |
|-------|------|
| K-Nearest Neighbours | Regression |
| Decision Tree | Classification |
| Linear Regression | Regression |
| Random Forest | Classification |
| Logistic Regression | Classification |

Feature importance analysis grouped by: **City (11)**, **Attributes (52)**, **Categories (191)**, **Operating Hours (14)**

---

## Roadmap

### Current Sprint — Due: 11 April 2026

- [ ] Complete full EDA in Python for the remaining CSV datasets:
  - [ ] `yelp_academic_dataset_review.csv`
  - [ ] `yelp_academic_dataset_user.csv`
  - [ ] `yelp_academic_dataset_tip.csv`
  - [ ] `yelp_academic_dataset_checkin.csv`
- [ ] Feature engineering and visualisations for each dataset
- [ ] Cross-dataset joins and correlation analysis

### Next Week — Week of 14 April 2026

- [ ] Set up a complete EDA pipeline on **Apache Spark**
- [ ] Deploy and configure the Spark cluster on **Google Cloud Platform (GCP)**
- [ ] Migrate Python EDA workflows to distributed PySpark jobs
- [ ] Validate results at scale against local Python outputs

---

## Tech Stack

| Layer | Tools |
|-------|-------|
| Language | Python 3 |
| Data Processing | pandas, NumPy |
| Visualisation | Matplotlib |
| Machine Learning | scikit-learn |
| Big Data (Planned) | Apache Spark, PySpark |
| Cloud (Planned) | Google Cloud Platform  |

---
