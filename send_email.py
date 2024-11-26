import smtplib, ssl

def subimit_email(user_email, subject, message):
    host = "smtp.gmail.com"
    port = 465
    password = "uzak expe maxr ivik"
    service_email = "devjohnv@gmail.com"
    context = ssl.create_default_context()

    service_message = """
    Hello! We'll be back in touch. Thank you for feedback.

    Kind regards"""

    processed_message = f"""Subject: {subject}.
    \n{message}\n\nMessage by {user_email}
    """

    with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
        server.login(service_email, password)
        # Receiving email feedback
        server.sendmail(service_email, service_email, processed_message)

"""        # Answering feedback
        server.sendmail(service_email, user_email, service_message)"""