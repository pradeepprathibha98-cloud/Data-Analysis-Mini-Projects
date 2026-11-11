# Python Data Analysis Mini Projects

[![Python](https://img.shields.io/badge/Python-3-blue.svg)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-orange.svg)](https://jupyter.org/)
[![NumPy](https://img.shields.io/badge/NumPy-arrays-013243.svg)](https://numpy.org/)
[![Pandas](https://img.shields.io/badge/Pandas-data%20analysis-150458.svg)](https://pandas.pydata.org/)

This repository contains small, hands-on projects developed while learning Python and data analysis. The notebooks cover NumPy operations, customer segmentation, and the preparation and exploration of Bengaluru housing data. Each project focuses on practicing core concepts rather than providing a production-ready application.

## Projects

| Notebook | Overview | Data and scope |
| --- | --- | --- |
| [Customer Segmentation](./Customer%20Segmentation.ipynb) | Creates sample transactions, calculates Recency, Frequency, and Monetary metrics, assigns quartile scores, and groups customers into simple segments. | Generates random transaction data in the notebook; no external dataset is needed. |
| [NumPy Stocks Analysis](./Numpy%20Stocks%20Analysis.ipynb) | Practices NumPy broadcasting, filtering, aggregation, reshaping, and finding maximum values using sample stock-price and sales arrays. | Uses values defined in the notebook; it does not fetch live market data or provide investment advice. |
| [Housing Data Analysis](./Housing%20Data%20Analysis.ipynb) | Cleans and explores Bengaluru housing data, engineers features, handles location categories, and filters several types of outliers. | Uses the included [`Bengaluru_House_Data.csv`](./Bengaluru_House_Data.csv) dataset. |

## Getting started

You will need Python 3 and Jupyter Notebook (or an editor that supports `.ipynb` files, such as Visual Studio Code).

1. Clone the repository and move into its directory:

   ```bash
   git clone https://github.com/pradeepprathibha98-cloud/Data-Analysis-Mini-Projects.git
   cd Data-Analysis-Mini-Projects
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

The RFM and stock-market notebooks can be run with their built-in sample data. The housing notebook reads the included `Bengaluru_House_Data.csv` file from the project root.

## Repository structure

```text
.
├── .gitignore
├── Bengaluru_House_Data.csv
├── Customer Segmentation.ipynb
├── Housing Data Analysis.ipynb
├── Numpy Stocks Analysis.ipynb
└── README.md
```

The notebooks are educational exercises. In particular, the stock-market notebook uses illustrative arrays, and the housing notebook performs data preparation and exploration rather than training a complete price-prediction model.
