import sqlite3

# आपके केस में database file है test.db
conn = sqlite3.connect("test.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM alembic_version;")
conn.commit()

print("✅ alembic_version table cleaned successfully.")

conn.close()
