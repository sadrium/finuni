#!/usr/bin/env python
# coding: utf-8

# Работа с текстовыми файлами. Открытие файла (функция open) и закрытие файла (метод close). Чтение текстового файла (методы read, readline, readlines). Перебор строк файла в цикле for. Запись в текстовый файл (метод write, функция print с параметром file).

# In[27]:


# 1
# Источник: https://www.w3resource.com/python-exercises/file/ + немножно придумала, чтобы сложнее было
# Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt. 
# In each one write a random number of letters of the next letter of the alphabet.
# Тут результат теста прикреплен папкой
import string
import random
alphabet = list(string.ascii_uppercase)
path2folder = input('Write path to folder with double \: ')
for each in range(len(alphabet)):
    with open(path2folder + '\\' + alphabet[each] + '.txt', 'w', encoding='utf-8') as f:
        if each != (len(alphabet) - 1):
            f.write((alphabet[each + 1] * random.randint(1, 10000)))
        else:
            f.write((alphabet[0] * random.randint(1, 10000)))
    f.close()


# In[ ]:


# 2
# Источник: https://www.pyforschool.com/assignment/file-handling.html + немножно придумала, чтобы сложнее былo
# Write a function in Python to count and display the total number of each word in a text file.
import re
def num_words(path2folder):
    with open(path2folder + '\\' + alphabet[each] + '.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    reg = re.compile('[^а-яА-Я0-9- ]')
    text = reg.sub('', text)
    words = set(text.split(' '))
    result = {}
    for each in words:
        result[each] = ' '.join(text).count(each)
    return result
path2folder = input('Write path to folder with double \: ')


# In[ ]:


# 3
# Источник: https://www.pyforschool.com/assignment/file-handling.html
# Write a function display_words() in python to read lines from a text file "story.txt",
# and display those words, which are less than 4 characters.
path2folder = input('Write path to folder with double \: ')
with open(path2folder + '\\' + alphabet[each] + '.txt', 'r', encoding='utf-8') as f:
    text = f.read()
reg = re.compile('[^а-яА-Я0-9- ]')
text = reg.sub('', text)
words = set(text.split(' '))
result = []
for each in words:
    if len(each) < 4:
        result.append(each)

