# import dos metodos
import ftplib
import smtplib
from zipfile import ZipFile
import os
from os.path import basename   
import datetime as dt 
import shutil

#function para enviar email sucesso ou nao    
def enviaEmail(msg,subj):
    smtp_object = smtplib.SMTP('smtp.interon.com.br',587)
    #smtp_object.ehlo()
    from_1  = 'marcelo@interon.com.br'
    smtp_object.starttls()
    #input('Whats yor password')
    #import getpass
    #User = getpass.getpass(prompt='user: ')
    #password = getpass.getpass(prompt='Password: ')
    #User = input("User: ")
    #password = input("Password: ")
    try:
        smtp_object.login(from_1,'')
        print('Logado')
    except Exception as e:
        print("Error na autenticação" + str(e))

    from_1  = 'marcelo@interon.com.br'

    text_msg = msg
    subject =subj
    msg = "Subject: "+ subject+'\n'+text_msg
    smtp_object.sendmail(from_1,[from_1,'suporte@interon.com.br'],msg)
    smtp_object.quit()
  
# inicio processo de backups 
  
dateagr1= dt.datetime.now()
dateagr=dateagr1.strftime("%Y%m%d%H%M%S")
bkpdb = str(dateagr)+'.sql'
os.system('D:/wampserver/bin/mariadb/mariadb10.2.8/bin/mysqldump  -u root --password="" mysql  > c:/tmp/banco/'+ bkpdb)

backupfiletmp = 'c:/tmp/'+str(dateagr)
shutil.make_archive(backupfiletmp,'zip','d:/wampserver/www')
backupfile=str(dateagr) +'.zip'
try:
    os.chdir("/tmp/banco")
    zip = ZipFile(backupfiletmp + '.zip', 'a') 
    zip.write(bkpdb)
    zip.close()
    os.remove(bkpdb)
except Exception as e:
    print("error on append file"+e)

ftp = ftplib.FTP()
host = "IP DO FTP"
port = 21
ftp.connect(host, port)
try:
     print ("Logging in...")
     ftp.login("USER FTP", "PWD FTP")
except:
     print("failed to login")
try:
    file = open(backupfiletmp+'.zip' ,'rb')                
    ftp.storbinary('STOR ' + backupfile, file)
    file.close() 
    os.chdir("c:/tmp/")
    os.remove(backupfile)
    databk = dateagr1.strftime("%d/%m/%Y, %H:%M:%S")
    enviaEmail('Backup efetuado com sucesso em: '+databk+'\n\no arquivo: '+backupfile+' Esta salvo no FTP!!!\n\n\n Att \n\n Suporte Vtiger','Backup Vtiger '+str(dateagr1.strftime("%d/%m/%Y")) )
except Exception as e:
    enviaEmail('Backup ERROR '+str(dateagr1.strftime("%d/%m/%Y")), 'Backup Vitger com erro \n' + str(e))

    
