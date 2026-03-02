Adidas Streamlit App
=====================

Quick start
-----------

Prerequisites
- Python 3.8 or newer
- Git (optional)

Recommended: use a virtual environment (venv) or conda.

Windows (Command Prompt) — venv
```cmd
python -m venv .venv
.venv\Scripts\activate
```

Conda
```bash
conda create -n adidas python=3.10 -y
conda activate adidas
```

Install dependencies

If there's a `requirements.txt` in the workspace root, install from it:

```bash
pip install -r requirements.txt
```

If not, install the minimal set used by the app:

```bash
pip install streamlit pandas pillow plotly openpyxl
```

Run the app

Open a terminal in the project folder and run:

```bash
cd Streamlit_project\PythonStreamlit\Adidas
streamlit run app.py
```

Adidas Sales — Streamlit Dashboard

A Streamlit dashboard that visualizes Adidas sales data and retail performance. The app aggregates sales and profit by retailer, region, state and sales method, and provides interactive charts and downloadable CSV exports.

**Features**
- **Interactive filters:** Filter by `Retailer` and `Year` from the sidebar.
- **KPI tiles:** Total Sales, Total Profit, Total Quantity, Total Cost, Total Retailers.
- **Charts:** bar charts, pie chart, Plotly line chart for state profiles.
- **Tables & exports:** styled tables with download buttons for CSV export.

**Files in this repository**
- `app.py`: Streamlit app entry point (dashboard implementation).
- `Adidas.xlsx`: Source data (Excel workbook) — required for the app to run.
- `logo.png`: Optional logo displayed in the sidebar if present.
- `requirements.txt`: Python dependencies for the project.
- `analysis.ipynb`: Analysis notebook (optional).

**Data schema (expected columns in `Adidas.xlsx`)**
The app expects the Excel file to contain at least the following columns (case-sensitive):
- `InvoiceDate` (date/time)
- `TotalSales` (numeric)
- `OperatingProfit` (numeric)
- `UnitsSold` (numeric)
- `Retailer` (string)
- `RetailerID` (id)
- `Region` (string)
- `SalesMethod` (string)
- `State` (string)

If your column names differ, update `app.py` accordingly.

**Prerequisites**
- Python 3.8 or newer
- Recommended: create and use a virtual environment (venv or conda)

Windows (Command Prompt) — venv
```cmd
python -m venv .venv
.venv\Scripts\activate
```

Conda
```bash
conda create -n adidas python=3.10 -y
conda activate adidas
```

**Install dependencies**
Install from the provided `requirements.txt` (recommended):
```bash
pip install -r requirements.txt
```

The `requirements.txt` in this repository contains most plotting and data libraries, but ensure the following packages are installed if not present:
```bash
pip install streamlit seaborn openpyxl
```

**Run the app**
From the project root (the folder containing `app.py`) run:
```bash
streamlit run app.py
```

By default Streamlit serves on `http://localhost:8501`. If the browser does not open automatically, copy the URL shown in the terminal.

**Usage tips**
- Place `Adidas.xlsx` and `logo.png` in the same folder as `app.py` before launching.
- Use the sidebar to choose retailers and years — charts and KPIs update automatically.
- Download CSV exports from the expanders (e.g., regional sales).

**Troubleshooting**
- If pandas cannot read the Excel file: `pip install openpyxl`.
- If `streamlit` is not found: `pip install streamlit` or check your virtual environment activation.
- If plots look off, confirm numeric columns are not strings and `InvoiceDate` parses correctly.

**Extending the app**
- Add new aggregations or charts by editing `app.py`.
- If your dataset is large, consider pre-aggregating data or increasing available memory for Python.

**Contributing & License**
- Contributions welcome — open an issue or submit a pull request.
- This repository does not include a license file. If you want to publish the project, add a `LICENSE`.

**Contact**
- For help or questions, open an issue in this repo or contact the project owner.

---

If you want, I can also:
- add `streamlit` and `seaborn` to `requirements.txt`,
- or run the app locally and verify it starts (I can provide the commands).