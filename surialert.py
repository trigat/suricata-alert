# SURIALERT - Suricata Email Alert
# - Parse through end of log and report alerts -
# www.trigat.com
# Python 3

from collections import deque
import smtplib, ssl
import sys

suricata_log = "fast.log"

# Make sure your Gmail is enabled to allow less secure apps
# https://myaccount.google.com/lesssecureapps
port = 587

send_address = "sender@gmail.com"
receive_address = "receiver@protonmail.com"
password = "PASSWORD"

search_strings = ["NMAP OS Detection Probe", "SCAN Suspicious", \
                 "SSH brute forcing", "other than Reverse Proxy", \
                 "ET SCAN Possible Nmap User-Agent Observed"]

def send_mail(line_group):
    group_text = ('\n'.join(line_group)) # use join to form string with deque
    message = "Subject: Suricata Alert \n\n" + group_text
    try:
        with smtplib.SMTP("smtp.gmail.com", port) as server:
            server.ehlo()
            server.starttls()
            server.login(send_address, password)
            server.sendmail(send_address, receive_address, message)
    except:
        print("\nSMTP: NO CONNECTION\n")
    #print(group_text)

with open(suricata_log) as log:
    line_group = deque(log, 40) # number of lines at end of file
    for line in line_group:
        for string_item in search_strings:
            if string_item in line:
                #print(line)
                send_mail(line_group)
                sys.exit(0)  # don't send e-mails in a loop
