#!/usr/bin/env python
# coding: utf-8

import requests
import bs4

res = requests.get('https://pt.wikipedia.org/wiki/Ronaldinho_Ga%C3%BAcho')


soap = bs4.BeautifulSoup(res.text,'lxml')

img1 = soap.select('.image')[0]

img2 = img1.find_all('img')

imagem_ronaldinho = 'http:'+img2[0]['src']

imagem_ronaldinho


resronaldo = requests.get(imagem_ronaldinho)

file_gaucho = open('gaucho3.png','wb')

file_gaucho.write(resronaldo.content)


file_gaucho.close()

# <img src="gaucho3.png">
