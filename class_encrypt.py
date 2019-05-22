#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import string
import random

class Encryption():
    def __init__(self, seeds):
        # quantidade seeds para criar o cipher
        self.seeds = seeds
        self.alphabet = string.ascii_lowercase
        self.alfabetoale = ''.join(map(str,random.sample(self.alphabet,26)))

    # criptografar valor usando cipher
    
    def encrypt(self,texto):
        self.texto = texto
        alfabeto_util = []
        for i in self.alfabetoale[self.seeds:len(self.alfabetoale)]:
            alfabeto_util.append(i)
        alfabeto_util.extend(self.alfabetoale)
        alfabeto_util = alfabeto_util[0:len(self.alfabetoale)]
        self.lista2 = []
        for i in self.texto:
            rnd = random.randint(0, 25)
            self.lista2.append(i)
            for j in alfabeto_util[rnd]:
                self.lista2.append(j)
        self.nomeinverso = ''.join(map(str, self.lista2[::-1]))
        alphabetsize = len(self.alphabet)
        saida = []
        for i, j in enumerate(self.nomeinverso.lower()):
            if j in alfabeto_util:
                try:
                    saida.append(alfabeto_util[self.alphabet.index(j)])
                except:
                    print("error", i, j)

            else:
               saida.append(j)
        saida = ''.join(saida)
        return saida

    def decrypt(self,texto,seeds):
        self.seedsdec = seeds
        self.texto = texto
        alphabetsize = len(self.alphabet)
        alfabeto_util = []
        for i in self.alfabetoale[self.seedsdec:len(self.alfabetoale)]:
            alfabeto_util.append(i)
        alfabeto_util.extend(self.alfabetoale)
        alfabeto_util = alfabeto_util[0:len(self.alfabetoale)]
        saida1 = []
        for i, j in enumerate(self.texto):
            if j in alfabeto_util:
                try:
                    saida1.append(self.alphabet[alfabeto_util.index(j)])
                except:
                    print("error", i, j)

            else:
               saida1.append(j)
        saida = ''.join(saida1)
        saida = saida1[::-1]
        nomecerto = []
        for i,j in enumerate(saida):
            if i % 2 ==0:
                nomecerto.append(j)
        return ''.join(map(str,nomecerto))

