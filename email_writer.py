import smtplib

__author__ = 'Albert Yu'
__version__ = '0.1'

# This will send an email from asoconflicts@gmail.com to mlswanson@amherst.edu every time a conflict is reported


def write_email(password):
    """
    Connects to mail server, writes the email, and quits.
    :param password: the password, which will be passed as a raw input
    :return: nothing
    """
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login('asoconflicts@gmail.com', password)
    smtpObj.sendmail(' asoconflicts@gmail.com ', ' mlswanson@amherst.edu ',
                     'Subject: So long.\nDear Alice, so long and thanks for all the fish. Sincerely, Bob')
    smtpObj.quit()


