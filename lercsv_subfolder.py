import os
import re
caminho = 'C:/Users/Marcelo/Desktop/inst/'
'''
Ler arquivos usando Regular expresions e opções para listar e varrer diretorios
um programa com 10 linhas varre 5 diretórios e 121 arquivos textos buscando se existe o link que continha http
'''

cont = 0
for folder,subfolder,files in os.walk(caminho):
    for f in files:
        caminho_completo = str(folder)+'\\'+''.join(f)
        f2 = open(caminho_completo,'r')
        exam_lines = f2.read()
        result = re.search(r'http\S+',exam_lines)
        if result != None:
            print(result.group())
        f2.close()


