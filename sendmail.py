import smtplib

sender_addr = 'sender@mail.address'
recipient_addr = 'recipient@mail.address'

msg = ("From: {sender_addr}\r\nTo: {recipient_addr}\r\n\r\n".format(sender_addr=sender_addr, recipient_addr=recipient_addr))
msg = msg + "content body\r\n"

print(msg)

server = smtplib.SMTP('localhost')
server.set_debuglevel(1)
server.sendmail(sender_addr, recipient_addr, msg)
server.quit()
