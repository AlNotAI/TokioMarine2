import sqlite3
import uuid
import datetime

conn = sqlite3.connect('insurance.db')
cursor = conn.cursor()

cursor.execute("""
ALTER TABLE insurance_policies
RENAME COLUMN coverage TO coverage_amount
""")

# Insert sample data
conn.commit()
conn.close()