# FastAPI Mobile-Friendly CSV Form App

This is a simple FastAPI + Jinja2 web app that works great on **Android** and **iOS**.
Users just click your deployed link and it opens the form.

## Features
- Mobile-friendly responsive UI
- Saves entries (date, description) to `entries.csv`
- View saved entries at `/entries`
- Health check at `/health`

---

## Run locally

```bash
python -m venv .venv
# Activate:
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate

pip install -r requirements.txt
uvicorn main:app --reload
```

Open: http://127.0.0.1:8000

---

## Deploy (Render - easiest)

1. Push this project to GitHub
2. Go to Render -> New -> Web Service -> connect repo
3. Render will detect it
4. Start command:
```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

Then you'll get a public URL like:
`https://your-app.onrender.com`

Share that link to any phone.

---

## Notes about CSV persistence
Many free hosts reset files on redeploy. If you need permanent storage, use:
- Render Persistent Disk, or
- a database (Postgres), or
- object storage (S3)
