import smtplib

smtp_object = smtplib.SMTP('smtp.gmail.com',587)
#smtp_object.ehlo()
from_1  = 'yaaaah@gmail.com'


smtp_object.starttls()
#input('Whats yor password')
#import getpass
#User = getpass.getpass(prompt='user: ')
#password = getpass.getpass(prompt='Password: ')
#User = input("User: ")
#password = input("Password: ")
try:
    smtp_object.login(from_1,"megadoido")
    print('Logado')
except:
    print("Error na autenticação")

from_1  = 'yaaaah@gmail.com'

text_msg = 'Isso eh um teste de mensagem  com quebra de linhas para o gmail\nass\nMarcelo Andrade'
subject ='TESTE MSG 3 '
msg = "Subject: "+ subject+'\n'+text_msg
smtp_object.sendmail(from_1,from_1,msg)
smtp_object.quit()



