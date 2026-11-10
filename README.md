# Python Data Analysis Mini Projects

[![Python](https://img.shields.io/badge/Python-3-blue.svg)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-orange.svg)](https://jupyter.org/)
[![NumPy](https://img.shields.io/badge/NumPy-arrays-013243.svg)](https://numpy.org/)
[![Pandas](https://img.shields.io/badge/Pandas-data%20analysis-150458.svg)](https://pandas.pydata.org/)

This repository contains small, hands-on projects developed while learning Python and data analysis. The notebooks cover NumPy operations, customer segmentation, and the preparation and exploration of Bengaluru housing data. Each project focuses on practicing core concepts rather than providing a production-ready application.

## Projects

| Notebook | Overview | Data and scope |
| --- | --- | --- |
| [Cutomer Segmentation.ipynb](./Customer Segmentaation.ipynb) | Creates sample transactions, calculates Recency, Frequency, and Monetary metrics, assigns quartile scores, and groups customers into simple segments. | Generates random transaction data in the notebook; no external dataset is needed. |
| [Numpy Stocks Analysis.ipynb](./Numpy Stocks Analysis.ipynb) | Practices NumPy broadcasting, filtering, aggregation, reshaping, and finding maximum values using sample stock-price and sales arrays. | Uses values defined in the notebook; it does not fetch live market data or provide investment advice. |
| [Housing Data Analysis.ipynb](./Housing Data Analysis.ipynb) | Cleans and explores Bengaluru housing data, engineers features, handles location categories, and filters several types of outliers. | Requires `Bengaluru_House_Data.csv` in the project root. The dataset is not included in this repository. |

## Getting started

You will need Python 3 and Jupyter Notebook (or an editor that supports `.ipynb` files, such as Visual Studio Code).

1. Clone the repository and move into its directory:

   ```bash
   git clone https://github.com/pradeepprathibha98-cloud/Data-Analysis-Toolkit.git
   cd Data-Analysis-Toolkit
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   ```

   On Windows PowerShell:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

   On macOS or Linux:

   ```bash
   source .venv/bin/activate
   ```

3. Install the libraries used by the notebooks:

   ```bash
   python -m pip install numpy pandas matplotlib jupyter
   ```

4. Start Jupyter from the repository directory and open a notebook:

   ```bash
   jupyter notebook
   ```

The RFM and stock-market notebooks can be run with their built-in sample data. To run the housing notebook, place a compatible `Bengaluru_House_Data.csv` file in the project root first; the notebook reads it using that filename.

## Repository structure

```text
.
├── .gitignore
├── Customer Segmentation.ipynb
├── Housing Data Analysis.ipynb
├── Numpy Stocks Analysis.ipynb
├── __pycache__/
│   ├── sbrn.cpython-314.pyc
│   └── seaborn.cpython-314.pyc
└── README.md
```

The `__pycache__` files are compiled Python artifacts already tracked in the repository; they are not needed to run the notebooks. The notebooks are educational exercises. In particular, the stock-market notebook uses illustrative arrays, and the housing notebook performs data preparation and exploration rather than training a complete price-prediction model.
