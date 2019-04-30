#!/usr/bin/env python
# coding: utf-8


import string
alphabet = string.ascii_lowercase
print(alphabet)
print(list(alphabet))



# criptografar valor usando cipher
def encrypt(text,shift):
    alfabeto_correto= alphabet
    alphabetsize= len(alphabet)
    lista_invertida = []
    for i in alfabeto_correto[shift:alphabetsize]:
        lista_invertida.append(i)
    lista_invertida.extend(alfabeto_correto)
    lista_invertida = lista_invertida[0:alphabetsize]
    saida = []
    for i,j in enumerate(text.lower()):
        if j in alfabeto_correto:
            saida.append(lista_invertida[alfabeto_correto.index(j)])
        else:
            saida.append(j)
    saida = ''.join(saida)
    return saida



#descriptografar usando o mesmo padrao de criptografia
def decrypt(text,shift):
    alfabeto_correto= alphabet
    alphabetsize= len(alphabet)
    lista_invertida = []
    for i in alfabeto_correto[shift:alphabetsize]:
        lista_invertida.append(i)
    lista_invertida.extend(alfabeto_correto)
    lista_invertida = lista_invertida[0:alphabetsize]
    saida = []
    for i,j in enumerate(text.lower()):
        if j in lista_invertida:
            saida.append(alfabeto_correto[lista_invertida.index(j)])
        else:
            saida.append(j)
    saida = ''.join(saida)
    return saida


# usar um brutal_force para descobrir qual mensagem correta
def brutal_force(text):
    print('#' * 40)
    vlr = len(alphabet)
    for i in range(vlr):
        print('Using shift value of {}'.format(i))
        print(decrypt(text,i))
        print('#'*40)



brutal_force('trg guvf zrffntr gb gur znva freire')





