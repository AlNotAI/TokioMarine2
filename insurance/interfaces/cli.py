import click
import sqlite3
import uuid
import datetime

@click.group()
def cli(): 
    """Insurance CLI Application"""
    pass    

@cli.command()
@click.option("--db", default="insurance.db", help="Path to the SQLite database file.")
def init_db(db):
    """Initialize the database."""
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS insurance_policies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        uuid TEXT UNIQUE NOT NULL,
        policy_holder_name TEXT NOT NULL,
        coverage REAL NOT NULL,
        premium REAL NOT NULL,
        start_date DATE NOT NULL,
        end_date DATE NOT NULL
    )
    """)

    # Insert sample data
    cursor.execute("INSERT INTO insurance_policies ( uuid, policy_holder_name, coverage, premium, start_date, end_date) VALUES (?, ?, ?, ?, ?, ?)", ( str(uuid.uuid4()), "Sample Policy", 100.0, 10.0, datetime.date(2023, 1, 1), datetime.date(2024, 1, 1)))
    cursor.execute("INSERT INTO insurance_policies ( uuid, policy_holder_name, coverage, premium, start_date, end_date) VALUES (?, ?, ?, ?, ?, ?)", ( str(uuid.uuid4()), "Another Policy", 150.0, 15.0, datetime.date(2023, 1, 1), datetime.date(2024, 1, 1)))
    cursor.execute("INSERT INTO insurance_policies ( uuid, policy_holder_name, coverage, premium, start_date, end_date) VALUES (?, ?, ?, ?, ?, ?)", ( str(uuid.uuid4()), "Third Policy", 200.0, 20.0, datetime.date(2023, 1, 1), datetime.date(2024, 1, 1)))

    conn.commit()
    conn.close()
    click.echo(f"Database initialized at {db}")

