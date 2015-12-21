import smtplib
from parser import *

__author__ = 'Albert Yu'
__version__ = '0.1'

# This will send an email from asoconflicts@gmail.com to mlswanson@amherst.edu every time a conflict is reported


def write_email(password, conflict):
    """
    Connects to mail server, writes the email, and quits.
    :param password: the password, which will be passed as a raw input
    :param conflict, the newly submitted conflict object (in parser.py)
    :return: void
    """
    smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_obj.ehlo()
    smtp_obj.starttls()
    smtp_obj.login('asoconflicts@gmail.com', password)
    smtp_obj.sendmail('asoconflicts@gmail.com', 'mlswanson@amherst.edu',
                      'Subject: New Conflict\n' +
                      'Dear Mark, a new conflict has been reported. \n' +
                      conflict.to_string())
    smtp_obj.quit()





