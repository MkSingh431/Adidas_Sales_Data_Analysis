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

Notes & troubleshooting

- Ensure `Adidas.xlsx` and `adidas_logo.jpg` are present in the same folder as `app.py`.
- If pandas fails to read the Excel file, install `openpyxl` (`pip install openpyxl`).
- If images or file paths fail, check current working directory: Streamlit runs with the app folder as the working directory when launched from that folder.
- If the browser does not open, copy the local URL shown in the terminal (http://localhost:8501).

Files
- App entry: Streamlit_project/PythonStreamlit/Adidas/app.py
- README: Streamlit_project/PythonStreamlit/Adidas/README.md

Questions or next steps
- Want me to add the logo display (`st.image`) to `app.py` and a requirements snippet?