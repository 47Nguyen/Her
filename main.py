from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import csv
import os

app = FastAPI(title="CSV Form App")

# Static + Templates setup
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

CSV_FILE = "entries.csv"
CSV_HEADERS = ["date", "description"]

def init_csv():
    """Ensure CSV exists and has headers."""
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(CSV_HEADERS)

init_csv()


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/submit")
def submit_entry(date: str = Form(...), description: str = Form(...)):
    # Append row to CSV
    with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([date, description])

    return RedirectResponse(url="/", status_code=303)


@app.get("/entries", response_class=HTMLResponse)
def view_entries(request: Request):
    entries = []
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            entries = list(reader)

    return templates.TemplateResponse("entries.html", {"request": request, "entries": entries})


@app.get("/health")
def health():
    return {"status": "ok"}
