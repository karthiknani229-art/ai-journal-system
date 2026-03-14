from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

app = FastAPI()

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- DATABASE ----------

def init_db():
    conn = sqlite3.connect("journal.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS journals(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text TEXT,
        emotion TEXT
    )
    """)

    conn.commit()
    conn.close()

init_db()


# ---------- MODEL ----------

class Journal(BaseModel):
    text: str


# ---------- HOME ----------

@app.get("/")
def home():
    return {"message": "AI Journal API running"}


# ---------- CREATE JOURNAL ----------

@app.post("/journal")
def create_journal(journal: Journal):

    text = journal.text.lower()

    if "happy" in text or "good" in text or "great" in text:
        emotion = "happy"
    elif "sad" in text:
        emotion = "sad"
    elif "angry" in text:
        emotion = "angry"
    elif "stress" in text or "anxious" in text:
        emotion = "stress"
    else:
        emotion = "neutral"

    conn = sqlite3.connect("journal.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO journals(text, emotion) VALUES (?,?)",
        (journal.text, emotion)
    )

    conn.commit()
    conn.close()

    return {"emotion": emotion}


# ---------- GET JOURNALS ----------

@app.get("/journals")
def get_journals():

    conn = sqlite3.connect("journal.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM journals")
    rows = cursor.fetchall()

    conn.close()

    return rows