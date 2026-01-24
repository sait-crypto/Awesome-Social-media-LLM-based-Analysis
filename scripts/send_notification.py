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
    pr_branch = os.environ.get('PR_BRANCH', 'Unknown')
    pr_user = os.environ.get('PR_USER', 'Unknown User') # 新增用户
    
    if not all([sender, password, receiver, smtp_server]):
        print("Skipping email: Missing SMTP configuration.")
        return

    log_content = ""
    # 优先读取 Update 日志，其次是 Validation 日志
    if os.path.exists('update_log.txt'):
        with open('update_log.txt', 'r', encoding='utf-8', errors='ignore') as f:
            log_content = f.read()
    elif os.path.exists('validation_log.txt'):
         with open('validation_log.txt', 'r', encoding='utf-8', errors='ignore') as f:
            log_content = "=== Validation Log (Update not run) ===\n" + f.read()

    # 邮件标题包含状态和分支
    subject = f"[{pr_branch}] PR by @{pr_user}: {status}"
    
    body = f"""
    PR Submitter: {pr_user}
    PR Branch: {pr_branch}
    Workflow Status: {status}
    
    === Execution Log ===
    {log_content}
    
    ==========================
    """

    message = MIMEText(body, 'plain', 'utf-8')
    message['From'] = f"Awesome Bot <{sender}>"
    message['To'] = receiver
    message['Subject'] = subject

    try:
        if smtp_port == '465':
            if smtp_server is None or smtp_port is None:
                raise ValueError("SMTP服务器和端口不能为空")
            server = smtplib.SMTP_SSL(smtp_server, int(smtp_port))
        else:
            if smtp_server is None or smtp_port is None:
                raise ValueError("SMTP服务器和端口不能为空")
            server = smtplib.SMTP(smtp_server, int(smtp_port))
            server.starttls()
            
        if sender is None or password is None:
            raise ValueError("发件人和密码不能为空")
        server.login(sender, password)
        if sender is None or receiver is None:
            raise ValueError("发件人和收件人不能为空")
        server.sendmail(sender, [receiver], message.as_string())
        server.quit()
        print("Notification email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    send_email()