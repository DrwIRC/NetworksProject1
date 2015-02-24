import smtplib
"""
Part 2 Project 1 Computer Networks
Names: Brendan Malone and Sam Cesario

The python scrpit below implements a simple STMP mail client. The
code was tested on a cell phone's 4G connection

"""
serverName = raw_input('Name of SMTP SERVER to Connect to: ')
sendFrom = raw_input('Send From: ')
sendTo = raw_input('Send To (Can be multiple separate by a comma only): ')
Mess = raw_input('Message (Only Text): ')

sender    = sendFrom #'xcsamcxc@gmail.com'
receivers  = sendTo.split(",")
message   = Mess     #"Hey Malone, I sent this from python!"

#Connect to SMTP
smtpO = smtplib.SMTP('smtp.gmail.com',25)
print('Connected')
smtpO.ehlo()
smtpO.starttls()
smtpO.ehlo()
smtpO.login('SamDummy12@gmail.com','samgoogle')
smtpO.sendmail(sender, receivers, message)
smtpO.quit()
print "From: " + sender + "\n" + "To: " + " , ".join(receivers) + "\n" + "Body: " + message + "\n"

