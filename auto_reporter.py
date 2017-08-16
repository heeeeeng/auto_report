import time
import io

import smtplib
from os.path import basename
from email.mime.base import MIMEBase

import _conf

def main():
    conf = _conf.conf
    update_report_data()
    send_email(conf)

def update_report_data():
    pass

def send_email(conf):
    cur_date = time.localtime()
    date_format = conf["report"]["date_format"]

    source_addr = conf["source_email"]["addr"] 
    target_addr = conf["target_email"]["addr"]

    msg = MIMEText("")

    subject_format = conf["email"]["subject_format"]
    subject = subject_format.format(
        date = time.strftime(date_format, cur_date),
        name = conf["yourname"]
    )


    filename = conf["filename"]["cur_filename"]
    f = open(filename, "r")
    attachment = MIMEText(f.read())
    attachment.add_header('Content-Disposition', 'attachment', filename=filename)           
    msg.attach(attachment)
    f.close()

    msg["From"] = source_addr
    msg["To"] = target_addr
    msg["Subject"] = subject
    msg.attach(attachment)

    s = smtplib.SMTP('localhost')
    s.sendmail(source_addr, target_addr, msg.as_string())
    s.quit()

main()