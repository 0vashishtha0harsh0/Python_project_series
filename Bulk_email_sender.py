import csv
from email.message import EmailMessage
import smtplib

def get_credentials(filepath):
    with open("Credentials.txt", "r") as f:
        email_address = f.readline().strip()
        email_pass = f.readline().strip()
        return (email_address, email_pass)

def login(email_address, email_pass, s):
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(email_address, email_pass)
    print("Login Successful")

def send_mail():
    s = smtplib.SMTP("smtp.gmail.com", 587)
    email_address, email_pass = get_credentials("./Credentials.txt")
    login(email_address, email_pass, s)
    subject = "Welcome to My Python Basic Email Sender Program"
    body = """I have created a simple program which is used to send a bulk of emails from a CSV file.
    This program helps you save time!"""
    
    with open("emails.csv", newline="") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=",")
        for email in spamreader:
            recipient = email[0]
            message = EmailMessage()
            message.set_content(body)
            message["Subject"] = subject
            message["From"] = email_address
            message["To"] = recipient
            s.send_message(message)
            print("Sent to " + recipient)
    s.quit()
    print("All emails sent successfully!")

if __name__ == "__main__":
    send_mail()
