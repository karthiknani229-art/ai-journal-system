AI-Assisted Journaling System

A full-stack prototype that allows users to write journal entries, detect emotions from their text, and view mood insights over time.

This project was built as part of a Full Stack Developer Internship assignment for RevoltronX – Team ArvyaX, focused on building innovative wellness and AI-driven experiences.

 Features

Create journal entries

Emotion detection based on journal text

Store entries in a database

View journal history

Visualize mood trends with charts

How It Works

User writes a journal entry in the web interface.

The frontend sends the text to the backend API.

The backend analyzes the emotion from the text.

The entry and emotion are stored in the database.

The frontend displays the emotion and updates mood insights.

 Tech Stack
Frontend

HTML

CSS

JavaScript

Chart.js

Backend

Python

FastAPI

Database

SQLite

Deployment

Frontend: Netlify

Backend: Render

Source Code: GitHub

 Project Structure
ai-journal-system
│
├── backend
│   ├── main.py
│   └── requirements.txt
│
├── frontend
│   ├── index.html
│   ├── script.js
│   └── style.css
│
└── README.md
 Running Locally
1. Clone the Repository
git clone https://github.com/your-username/ai-journal-system.git
cd ai-journal-system
2. Start Backend
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

Backend runs at:

http://127.0.0.1:8000

API documentation:

http://127.0.0.1:8000/docs
3. Start Frontend
cd frontend
python -m http.server 5500

Open in browser:

http://127.0.0.1:5500
 Mood Insights

The application generates emotion analytics by analyzing past journal entries and displaying them using Chart.js.

Example emotions tracked:

Happy

Sad

Stress

Angry

Neutral

 Live Demo

Frontend:

https://your-netlify-app.netlify.app

Backend API:

https://your-render-api.onrender.com/docs
 Note

If the backend is deployed on the Render free tier, the server may take 1-2 minutes to wake up after inactivity.


 Author

Karthik Penta
Full Stack Developer

GitHub:
https://github.com/karthiknani229-art
