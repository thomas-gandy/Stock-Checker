import smtplib, ssl, getpass, sys, os

def sendMail(emailList, subject, body):
    message = f"""\
Subject: {subject}

{body}
"""
                
    port = 465
    senderEmail = os.environ["stockCheckerSenderEmail"]
    password = os.environ["stockCheckerPassword"]
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(senderEmail, password)
        for receiverEmail in emailList:
            server.sendmail(senderEmail, receiverEmail, message)
