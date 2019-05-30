'''
Ler PDF com PyPDF2

abrir o arquivo como 'rb'
usar o PpdfFileReader

looping em todas as paginas do pDF extraindo o texto
'''
import PyPDF2,re
f = open('c:/tmp/email.pdf','rb')
pdf = PyPDF2.PdfFileReader(f)
regmail = r'[\w\.-]+@[\w\.-]+'
EMAILS  = ''
for i in range(0,pdf.getNumPages()):
   if re.findall(regmail,pdf.getPage(i).extractText()):
       EMAILS = re.findall(r'[\w\.-]+@[\w\.-]+',pdf.getPage(i).extractText())

print(''.join(EMAILS))
