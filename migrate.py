from sqlalchemy import create_engine, inspect, text

engine = create_engine("sqlite:///./your_database.db")  # apne DB path yahan daalo
conn = engine.connect()

inspector = inspect(engine)

# Check if 'users' table exists
if 'users' in inspector.get_table_names():
    columns = [col['name'] for col in inspector.get_columns('users')]
    
    if 'verification_token' not in columns:
        conn.execute(text("ALTER TABLE users ADD COLUMN verification_token TEXT"))
        print("verification_token added")
    else:
        print("verification_token already exists")
    
    if 'verification_expiry' not in columns:
        conn.execute(text("ALTER TABLE users ADD COLUMN verification_expiry DATETIME"))
        print("verification_expiry added")
    else:
        print("verification_expiry already exists")
    
    if 'is_verified' not in columns:
        conn.execute(text("ALTER TABLE users ADD COLUMN is_verified BOOLEAN"))
        print("is_verified added")
    else:
        print("is_verified already exists")

else:
    print("Table 'users' does not exist!")

conn.close()
