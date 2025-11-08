from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()

conn = psycopg2.connect( 
    host = os.getenv("PGHOST"), 
    dbname = os.getenv("PGDATABASE"), 
    user = os.getenv("PGUSER"), 
    password = os.getenv("PGPASSWORD"), 
    port = os.getenv("PGPORT")
)

#Connect to postgres database and create table

cur = conn.cursor()

cur.execute(""" CREATE TABLE IF NOT EXISTS users (
            user_id INT PRIMARY KEY,
            first_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255) NOT NULL,
            email_address VARCHAR(255) NOT NULL,
            subscription_status VARCHAR(255) NOT NULL,
            email_frequency VARCHAR(255)
            );
             """)

#Insert subscribers' record to the database.

cur.execute(""" INSERT INTO users(user_id, first_name, last_name, email_address, 
            subscription_status, email_frequency)
    VALUES
    (1, 'John', 'Doe', 'john.doe@example.com', 'active', 'daily'),
    (2, 'Jane', 'Smith', 'jane.smith@example.com', 'inactive', 'weekly'),
    (3, 'Michael', 'Johnson', 'michael.johnson@example.com', 'active', 'daily'),
    (4, 'Emily', 'Davis', 'emily.davis@example.com', 'active', 'weekly'),
    (5, 'Chris', 'Brown', 'chris.brown@example.com', 'inactive', 'daily'),
    (6, 'Olivia', 'Taylor', 'olivia.taylor@example.com', 'active', 'daily'),
    (7, 'Daniel', 'Wilson', 'daniel.wilson@example.com', 'inactive', 'weekly'),
    (8, 'Sophia', 'Martinez', 'sophia.martinez@example.com', 'active', 'weekly'),
    (9, 'James', 'Anderson', 'james.anderson@example.com', 'active', 'daily'),
    (10, 'Ava', 'Thomas', 'ava.thomas@example.com', 'inactive', 'weekly'),
    (11, 'William', 'Jackson', 'william.jackson@example.com', 'active', 'daily'),
    (12, 'Isabella', 'White', 'isabella.white@example.com', 'inactive', 'daily'),
    (13, 'Ethan', 'Harris', 'ethan.harris@example.com', 'active', 'weekly'),
    (14, 'Mia', 'Martin', 'mia.martin@example.com', 'active', 'daily'),
    (15, 'Alexander', 'Thompson', 'alexander.thompson@example.com', 'inactive', 'weekly'),
    (16, 'Charlotte', 'Garcia', 'charlotte.garcia@example.com', 'active', 'daily'),
    (17, 'Benjamin', 'Clark', 'benjamin.clark@example.com', 'inactive', 'daily'),
    (18, 'Amelia', 'Rodriguez', 'amelia.rodriguez@example.com', 'active', 'weekly'),
    (19, 'Lucas', 'Lewis', 'lucas.lewis@example.com', 'active', 'daily'),
    (20, 'Harper', 'Lee', 'harper.lee@example.com', 'inactive', 'weekly');
""")

conn.commit()
cur.close()
conn.close()

