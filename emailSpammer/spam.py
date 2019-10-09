import smtplib

for i in range(0,5)
	conn = smtplib.SMTP('smtp.gmail.com',587)# connect to gmail
	conn.ehlo()
	conn.starttls()
	conn.login('your_email','your_password') # write your email and password for the gmail account
	conn.sendmail('your_email','recipient_address','Subject: Write email subject here\n\n Write the message here  ') # write your email and recipient address here
conn.quit()
