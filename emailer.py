import smtplib

# list of email_id to send the mail
li = ["ddhruvarora@gmail.com"]

for dest in li:
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.starttls()
	s.login("sender_email_id", "sender_email_id_password")
	message = "Message_you_need_to_send"
	s.sendmail("sender_email_id", dest, message)
	s.quit()
