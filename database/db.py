import sqlite3
from datetime import datetime

# Database Connect

def init_db():
    conn = sqlite3.connect("database/progress.db")
    cursor = conn.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS sessions (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   date TEXT,
                   text TEXT,
                   filler_count INTEGER,
                   grammar_errors INTEGER,
                   sentiment TEXT,
                   score INTEGER
                   )
                   ''')
    conn.commit()
    conn.close()
    print("Database Ready!")


    # Session Save
def save_session(text, filler_count, grammar_errors, sentiment, score):
    conn = sqlite3.connect("database/progress.db")
    cursor = conn.cursor()
    cursor.execute('''
                   INSERT INTO sessions(
                   date, text, filler_count, grammar_errors, sentiment, score)
                   VALUES(?, ?, ?, ?, ?, ?)''', 
                   (datetime.now().strftime("%Y-%m-%d %H:%M"),
                    text,
                    filler_count,
                    grammar_errors,
                    sentiment,
                    score
                    ))
    conn.commit()
    conn.close()
    print("Session Saved!")


# Progress History
def get_history():
    conn = sqlite3.connect("database/progress.db")
    cursor = conn.cursor()
    cursor.execute('''
                   SELECT date, score, filler_count,
                   grammar_errors, sentiment
                   FROM sessions
                   ORDER BY id DESC
                   LIMIT 10
                   ''')
    rows = cursor.fetchall()
    conn.close()
    return rows



if __name__ == "__main__":
    init_db()
    save_session(
        text = "Um I am basically a good developer",
        filler_count = 3,
        grammar_errors = 1,
        sentiment = "Positive",
        score = 75
    )
    history = get_history()
    print("\n Session History:")
    for row in history:
        print(f"   {row[0]} | Score: {row[1]} | Fillers: {row[2]}")