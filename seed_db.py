import sqlite3
import uuid
import datetime

conn = sqlite3.connect('insurance.db')
cursor = conn.cursor()


cursor.execute("""DROP TABLE IF EXISTS insurance_policies;""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS insurance_policies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    uuid TEXT UNIQUE NOT NULL,
    item TEXT NOT NULL,
    policy_holder_name TEXT NOT NULL,
    coverage_amount REAL NOT NULL,
    premium REAL NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL
)
""")

    # Insert sample data
cursor.execute("INSERT INTO insurance_policies ( uuid, item, policy_holder_name, coverage_amount, premium, start_date, end_date) VALUES (?, ?, ?, ?, ?, ?, ?)", ( str(uuid.uuid4()), "Home Insurance", "Alice", 100.0, 10.0, datetime.date(2023, 1, 1), datetime.date(2024, 1, 1)))
cursor.execute("INSERT INTO insurance_policies ( uuid, item, policy_holder_name, coverage_amount, premium, start_date, end_date) VALUES (?, ?, ?, ?, ?, ?, ?)", ( str(uuid.uuid4()), "Auto Insurance", "Bob", 150.0, 15.0, datetime.date(2023, 1, 1), datetime.date(2024, 1, 1)))
cursor.execute("INSERT INTO insurance_policies ( uuid, item, policy_holder_name, coverage_amount, premium, start_date, end_date) VALUES (?, ?, ?, ?, ?, ?, ?)", ( str(uuid.uuid4()), "Life Insurance", "Charlie", 200.0, 20.0, datetime.date(2023, 1, 1), datetime.date(2024, 1, 1)))

conn.commit()
conn.close()