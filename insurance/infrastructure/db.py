import sqlite3
import os

from insurance.infrastructure.queries import load_sql 

def get_db():
    return sqlite3.connect(os.getenv("INSURANCE_DB_PATH", "insurance.db"))

def fetch_all_policies():
    query = load_sql("select_all_policies.sql")
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return rows

def fetch_policy_by_uuid(uuid):
    conn = get_db()
    cursor = conn.cursor()
    sql = load_sql("select_policy_by_uuid.sql")
    cursor.execute(sql, {"uuid": uuid})
    row = cursor.fetchone()
    conn.close()
    return row
