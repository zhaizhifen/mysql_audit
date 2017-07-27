import smtplib, traceback
from email.mime.text import MIMEText

import settings

class Entity():
    def __init__(self):
        pass

def get_object(row):
    info = Entity()
    for key, value in row.items():
        if(value == "None"):
            value = None
        setattr(info, key, value)
    return info

def send_text(subject, to_list, content):
    send_mail(subject, to_list, content, "plain")

def send_html(subject, to_list, content):
    send_mail(subject, to_list, content, "html")

def send_mail(subject, to_list, content, mail_type):
    list_t = []
    server = None
    if(isinstance(to_list, list) == False):
        list_t.append(to_list)
    try:
        message = MIMEText(content, _subtype=mail_type, _charset="utf8")
        message['Subject'] = subject
        message['To'] = ";".join(list_t)
        message['From'] = settings.EMAIL_USER

        server = smtplib.SMTP()
        server.connect(settings.EMAIL_HOST)
        server.login(settings.EMAIL_USER, settings.EMAIL_PASSWORD)
        server.sendmail(settings.EMAIL_USER, list_t, message.as_string())
    except:
        traceback.print_exc()
    finally:
        if(server != None):
            server.close()

