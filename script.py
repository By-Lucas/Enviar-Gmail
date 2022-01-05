import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

Email_Enviar = "TESTE@gmail.com"
Email_Receber = "TESTE@gmail.com, TESTE@gmail.com"

# Instância do MIMEMultipart
msg = MIMEMultipart()


msg['From'] = Email_Enviar

msg['To'] = Email_Receber

msg['Subject'] = "Veja mais peojetos!!!"

body = """Várias automacoes e sistemas criados do 0 no meu GitHub.\n
acompanhe no link https://github.com/By-Lucas"""

msg.attach(MIMEText(body, 'plain'))

#Servidor SMTP
s = smtplib.SMTP('smtp.gmail.com', 587)

# Segurança
s.starttls()

s.login(Email_Enviar, 'SENHA DO EMAIL')

# Converte para String
text = msg.as_string()

s.sendmail(Email_Enviar, Email_Receber, text)

s.quit()
