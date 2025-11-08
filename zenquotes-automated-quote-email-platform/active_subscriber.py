from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()

def fetch_user():

# Connecting to database
    conn = psycopg2.connect(
        host = os.getenv("PGHOST"),
        dbname = os.getenv("PGDATABASE"),
        user = os.getenv("PGUSER"),
        password = os.getenv("PGPASSWORD"),
        port = os.getenv("PGPORT")
    )

    cur = conn.cursor()
    
    # Extracting active subscriber from database
    cur.execute("""
                    SELECT 
                            user_id, 
                            first_name,  
                            email_address, 
                            subscription_status
                    FROM users
                    WHERE subscription_status = 'active';  
    """)
    users = cur.fetchall()
    conn.close()
    return users

