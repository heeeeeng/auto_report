import time
from email.mime.text import MIMEText

import _conf

def main():
    conf = _conf.conf
    update_report_data()
    send_email(conf)

def update_report_data():
    pass

def send_email(conf):
    cur_date = time.localtime()

    source_addr = conf["source_email"]["addr"] 
    target_addr = conf["target_email"]["addr"]

    msg = MIMEText("")

    msg["From"] = source_addr
    msg["To"] = target_addr

    subject = conf[]


main()