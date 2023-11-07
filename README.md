# YG Entertainment Stock Data Retrieval

This Python script allows you to retrieve historical stock data for YG Entertainment using the Yahoo Finance API. The data is saved to a CSV file for further analysis.

## Prerequisites

Before using this script, ensure you have the following installed:

- Python (3.x recommended)
- `yfinance` library for accessing Yahoo Finance data
- `pandas` library for data manipulation and saving to CSV

You can install the required libraries using pip:

```
pip install yfinance pandas
```

## Usage
1. Clone this repository or download the script to your local machine.
2. Open the Python script (e.g., stock.py) in a text editor or integrated development environment (IDE).
3. Modify the ticker_symbol variable with the desired stock symbol.
4. Run the script
    ```
    python stock.py
    ```
5. The script will retrieve one month of historical stock data and save it to a CSV file with the name YG_Entertainment_Stock_Data.csv.