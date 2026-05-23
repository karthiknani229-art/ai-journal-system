# AI-Assisted Journaling System

A full-stack journaling platform that analyzes journal entries for emotion detection and mood insights using AI-driven text processing.

## Live Demo

- Frontend: https://ai-journal-system.netlify.app/
- Backend API: https://ai-journal-system-2sc8.onrender.com/
- Swagger Docs: https://ai-journal-system-2sc8.onrender.com/docs

> Note: Backend is on Render's free tier — first request may take 30–60 seconds due to cold start.

## Tech Stack

**Frontend:** HTML, CSS, JavaScript, Chart.js

**Backend:** Python, FastAPI

**Database:** SQLite

**Deployment:** Netlify (Frontend), Render (Backend)

## Features

- Write and store journal entries
- Automatic emotion detection from entry text
- View full journal history
- Interactive mood trend visualization with Chart.js
- Tracks 5 emotion categories: Happy, Sad, Stress, Angry, Neutral

## How It Works

```
User writes journal entry
        ↓
Frontend sends text to backend API
        ↓
Backend analyzes emotion from text
        ↓
Entry and detected emotion stored in SQLite
        ↓
Frontend displays emotion and updates mood charts
```

## Project Structure

```
ai-journal-system/
│
├── backend/
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
└── README.md
```

## Local Setup

**1. Clone the repository**

```bash
git clone https://github.com/karthiknani229-art/ai-journal-system.git
cd ai-journal-system
```

**2. Start backend**

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

Backend runs at: http://127.0.0.1:8000

Swagger docs at: http://127.0.0.1:8000/docs

**3. Start frontend**

```bash
cd frontend
python -m http.server 5500
```

Open in browser: http://127.0.0.1:5500

## Author

Penta Karthik — [GitHub](https://github.com/karthiknani229-art)
