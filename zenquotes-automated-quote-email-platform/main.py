from extract_quote import extract_quote
from active_subscriber import fetch_user
from send_email import send_email
import csv
import time
import os

LOG_FILE = "logs/email_log.csv"
def log_status(email, status, message):
    # Ensure the 'logs' directory exists
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

    # Write the log entry
    with open(LOG_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([email, status, message])

    
"""Fuction to send quote to each user fetched from the databse"""
def send_quote_to_users():

    quote = extract_quote()

    QUOTE_FETCHED = "logs/quote_fetched.txt"

    with open(QUOTE_FETCHED, "w", encoding="utf-8") as file:
        file.write(quote)
    
    print(f"Quote saved successfully to {QUOTE_FETCHED}")

    users = fetch_user()
    subject = "Daily Inspirational Quote from MindFuel 🌟"

    if not quote:
        print("Failed to fetch quote. Exiting.")
        return
    
    for user in users:
        email = user[2]
        name = user[1]
        
        message = (
            f"Hi {name},\n\n"
            f"Here is your inspirational quote for today:\n\n"
            f"{quote}\n\n"
            f"Have a wonderful and productive day!\n\n"
            f" — MindFuel Team"
        )

        for attempt in range(3):  # Retry logic
            success, msg = send_email(email, subject, message)
            if success:
                print(f"Sent to {email}")
                log_status(email, "SUCCESS", msg)
                break
            else:
                print(f"Attempt {attempt + 1} failed for {email}: {msg}")
                time.sleep(5)
        else:
            log_status(email, "FAILED", msg)
            print(f"Could not send to {email} after 3 attempts.")

if __name__ == "__main__":
    send_quote_to_users()
