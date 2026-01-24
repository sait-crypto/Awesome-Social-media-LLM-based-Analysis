import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def send_email():
    sender = os.environ.get('SMTP_USER')
    password = os.environ.get('SMTP_PASSWORD')
    receiver = os.environ.get('NOTIFICATION_EMAIL')
    smtp_server = os.environ.get('SMTP_SERVER')
    smtp_port = os.environ.get('SMTP_PORT')
    
    status = os.environ.get('workflow_status', 'Unknown')
    
    if not all([sender, password, receiver, smtp_server]):
        print("Skipping email: Missing SMTP configuration.")
        return

    # 读取 update.py 的日志
    log_content = ""
    if os.path.exists('update_log.txt'):
        with open('update_log.txt', 'r', encoding='utf-8', errors='ignore') as f:
            log_content = f.read()

    subject = f"Paper Submission Process Result: {status}"
    
    body = f"""
    GitHub Action Workflow Status: {status}
    
    === Update Script Logs ===
    {log_content}
    
    ==========================
    Please check the repository for details.
    """

    message = MIMEText(body, 'plain', 'utf-8')
    message['From'] = Header(f"Awesome Bot <{sender}>", 'utf-8')
    message['To'] =  Header(receiver, 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')

    try:
        if smtp_port == '465':
            server = smtplib.SMTP_SSL(smtp_server, int(smtp_port))
        else:
            server = smtplib.SMTP(smtp_server, int(smtp_port))
            server.starttls()
            
        server.login(sender, password)
        server.sendmail(sender, [receiver], message.as_string())
        server.quit()
        print("Notification email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    send_email()