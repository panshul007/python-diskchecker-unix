'''
Created on Sep 18, 2013

@author: panshul
'''
import smtplib

from email.mime.text import MIMEText


username="username@domain.com"
password="guessme"


def prepareMessage(dsf,recipients,machine):
    message = format("Hello,\nFree disk space on %r is dangerously low. Please free some disk space urgently.\n The current stats are:\ntotal: %r GB used: %r GB free: %r GB" %(machine,dsf[0],dsf[1],dsf[2]))
    msg = MIMEText(message)
    msg['Subject'] = format("ALERT: Disk space low on %r" %(machine))
    msg['From'] = username
    msg['To'] = ','.join(recipients)
    return msg
 

def sendDiskFullMail(dsf,recipients,machine):
    msg = prepareMessage(dsf,recipients,machine)
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(username,password)
    s.sendmail(username, recipients, msg.as_string())
    s.quit()    

