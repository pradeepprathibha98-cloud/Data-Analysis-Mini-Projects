# Python Data Analysis Mini Projects

[![Python](https://img.shields.io/badge/Python-3-blue.svg)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-arrays-013243.svg)](https://numpy.org/)
[![Pandas](https://img.shields.io/badge/Pandas-data%20analysis-150458.svg)](https://pandas.pydata.org/)

A collection of small Python exercises in numerical computing, data manipulation, customer segmentation, and visualization. These projects are intended for learning and demonstration; they are not production systems or financial tools.

## Projects

| Project | What it demonstrates | Data / behavior |
| --- | --- | --- |
| `RFM_Engine.py` | Aggregates Recency, Frequency, and Monetary metrics, assigns quantile scores, and creates simple customer segments. | Generates random transaction data in memory; no external dataset is required. |
| `Stock_market_tracker.py` | NumPy broadcasting, filtering, aggregation, reshaping, and index operations. | Uses fixed sample arrays; it does not retrieve live stock prices. |
| `build-pd.py` | Basic Pandas data loading, type conversion, duplicate removal, and tabular output. | Reads `pokemon.csv` from the project directory. |
| `mtplb.py` | Matplotlib charting practice and data preparation with NumPy and Pandas. | Reads `pokemon.csv`; most plotting examples are currently commented out. |
| `sbrn.py` | Seaborn pair-plot visualization using sample datasets. | Loads Seaborn sample datasets, which may require an internet connection. |

## Getting started

Use Python 3 with `pip`. From the project directory, create and activate a virtual environment, then install the libraries used by the examples:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

macOS / Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install numpy pandas matplotlib seaborn
```

Run an example from the project directory:

```bash
python RFM_Engine.py
python Stock_market_tracker.py
python build-pd.py
python mtplb.py
python sbrn.py
```

The CSV-reading scripts expect `pokemon.csv` in the current project directory. `employees.csv` and `data.json` are additional sample files and are not currently used by the active scripts. The Seaborn example downloads its sample datasets when they are not already cached.

## Repository contents

```text
.
├── RFM_Engine.py
├── Stock_market_tracker.py
├── build-pd.py
├── mtplb.py
├── sbrn.py
├── pokemon.csv
├── employees.csv
├── data.json
└── README.md
```

**Repository note:** `build-pd.py`, `mtplb.py`, `sbrn.py`, and the sample data files are currently ignored by Git in this working copy. They will not appear in a clone until the ignore rules are updated and the files are added to the repository.
