#! /usr/bin/python3

import smtplib
import sys

mac = sys.argv[1]
ip = sys.argv[2]
interface = sys.argv[4]
if int(sys.argv[5]) == 0:
    reason = "ip change"
elif int(sys.argv[5]) == 1:
    reason = "mac address only detected but not in whithe list"
elif int(sys.argv[5]) == 2:
    reason = "mac address in black list"
elif int(sys.argv[5]) == 3:
    reason = "new mac address"
elif int(sys.argv[5]) == 4:
    reason = "unauthorized arp request"
elif int(sys.argv[5]) == 5:
    reason = "abusive number of arp request detected"
elif int(sys.argv[5]) == 6:
    reason = "ethernet mac address different from arp mac address"
elif int(sys.argv[5]) == 7:
    reason = "global flood detection"
elif int(sys.argv[5]) == 8:
    reason = "new mac adress without ip"
elif int(sys.argv[5]) == 9:
    reason = "mac change"
else:
    reason = "ERROR"
vendor = sys.argv[6]


SERVER = "localhost"

FROM = "arpwatcher@example.com" #change to different domain if you own one
TO = ["<YOUR_EMAIL@HERE>"] #must be a list
# !!! edit ^^^ !!!
# add/ change your e-mail address where you want to get notifications

SUBJECT = reason

TEXT = "Mac: " + mac + "of :" + vendor + "with ip: " + ip + "on interface: " + interface + ": " + reason + "\n"

# Prepare actual message

message = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

# Send the mail

server = smtplib.SMTP(SERVER)
server.sendmail(FROM, TO, message)
server.quit()
