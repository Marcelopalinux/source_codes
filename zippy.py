'''import zipfile as zip

f = open('teste.txt','w+')
f.write('teste gravacao\ntestegravacao 2 linha\n teste gravacao terceira linha')
f.close()

comp_file = zip.ZipFile('my_compressed_info.zip', 'w')
comp_file.write('teste.txt',compress_type=zip.ZIP_DEFLATED)
comp_file.close()



'''
# shutil facilita muito na movimentação de arquivos e ZIPAR e UNZIPAR os mesmos
# compactar e descompactar como dizemos aqui no brasil.
import shutil

#shutil.make_archive('my_compressed','zip','D:\docs_dbmaker')

shutil.unpack_archive('my_compressed.zip', 'c:\dbmaker','zip')