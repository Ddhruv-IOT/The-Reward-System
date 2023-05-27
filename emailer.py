import streamlit as st
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

email_id = st.secrets["emailer"]["email"]
password = st.secrets["emailer"]["password"]


@st.cache_resource
def connect_SMPT():
    print("Connecting to SMTP server...")
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login(email_id, password)
    return s


subject = "Congratulations"
body = """
<html>
  <body>
    <h2>Introducing the RAIoT Rewards Program!</h2>
    <p>
		Welcome to the Reward Program of RAIOT Labs! where your talents are recognized and celebrated.
		We are thrilled to have you on board. Get ready for an exciting journey where you can showcase your skills and earn recognition.
		Participate by completing tasks and answering questions to earn points. As you accumulate points, you will be awarded badges to acknowledge your achievements.
		Your dedication and expertise will also be highlighted on our social media handles, giving you well-deserved recognition among our community.
		Join us now and unlock a world of opportunities in the realm of innovation and technology!
  	</p>
    <p>Please find your ID and password below:</p>
    <ul>
      <li>Your ID: <strong>&lt;id&gt;</strong></li>
      <li>Your Password: <strong>&lt;pwd&gt;</strong></li>
    </ul>
    <p>For more information, visit our website: <a href="https://www.ddhruv.com">www.ddhruv.com</a></p>
  </body>
</html>

"""


def send_email(s, email):
    msg = MIMEMultipart()
    msg["From"] = email_id
    msg["To"] = email
    msg["Subject"] = subject

    # Add the email body as HTML
    msg.attach(MIMEText(body, "html"))
    s.sendmail(email_id, email, msg.as_string())
    return f"Email sent to: {email}"


def stop_SMPT(s):
    s.quit()
    return "SMTP server stopped"


if __name__ == "__main__":
    s = connect_SMPT()
    send_email(s, "ddhruvarora2+st@gmail.com")
    stop_SMPT(s)
