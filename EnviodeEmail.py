import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "Coloque o e-mail de envio"
rec_list =  ['teste1@hotmail.com', 'teste1@hotmail.com' , 'teste1@hotmail.com', 'teste1@hotmail.com','teste1@hotmail.com']
rec =  ', '.join(rec_list)

# Instância do MIMEMultipart
msg = MIMEMultipart()


msg['From'] = fromaddr

msg['To'] = rec

msg['Subject'] = "REINF - DIA DE ABRIR CHAMADO SOBRE O REINF!!"

body = """E-mail automático para a abertura do chamado sobre REINF/EXTRATO FISCAL."""

msg.attach(MIMEText(body, 'plain'))

#Servidor SMTP
s = smtplib.SMTP('smtp.gmail.com', 587)

# Segurança
s.starttls()

s.login(fromaddr, 'coloque sua senha')

# Converte para String
text = msg.as_string()

s.sendmail(fromaddr, rec_list, text)

print = "Enviado com sucesso";
s.quit()