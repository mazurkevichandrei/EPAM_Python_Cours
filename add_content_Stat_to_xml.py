#Идея в следующем:

#Приложенеи предлагает выбрать способ добавления новостей: вручную либо импортировать из файла
#Затем после этого предлагает выбрать тип новости: Спорт либо Обычная новость
#Далее в переменную текста новости записывается введённый текст или импортированный
#Также при этом автоматически определяется заголовок новости(зависит от выбранного ранее типа) и дата написания либо импорта текста
#Запускается функция Publish, которая добавляет значение переменной в итоговый файл, с добавлением заголовка и времени публикации

#Форматирование из файла пока не добавил
#В сорсовом файле новости должны быть разделены пустой строкой для того чтобы добавиться в итоговый файл как разные публикации
#Удаление из сорсового файла после прочтения тоже пока не сделал
#Приложенный итоговый файл пустой для удобства тестирования

#Добавлена функция подсчёта статистики слов и букв в итоговом файле с записью в count_words.csv/stat_letters.csv

import datetime


class AddContent:
    def __init__(self, content, header):
        #Определение содержания новости
        self.content=content
        #Определение заголовка новости
        self.header=header
    def pubdate(self):
        #Определение времени публиувции, будет запускаться в момент ввода новости либо импорта из файла
        global publishtime
        publishtime = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
        return  publishtime

###  ЧТЕНИЕ ФАЙЛОВ ИЗ КОТОРЫХ БУДЕМ ДОБАВЛЯТЬ НОВОСТЬ  ###

#Читаем текст спортивной новости из файла:
def ReadSportFile():
    fromfile = open('sport_source.txt').read().split('\n\n')
    return fromfile
#Читаем текст обычной новости из файла:
def ReadNewsFile():
    fromfile = open('news_source.txt').read().split('\n\n')
    return fromfile

##########################################################

#Функция создания контента (srcdata примет значение контента введённого вручную или импортированного из файла, headtype передадим в зависимости от типа новости)
def createContent(srcdata, headtype):
        global news
        news = AddContent(srcdata, headtype)
        #Для определения времени добавления информации
        news.pubdate()

#Функция для записи новости в итоговый файл(используется для новости, написанной вручную и для новости из файла):
def Publish():
    #Открываем итоговый файл в режиме добавления
    target_file=open("data.txt","a")
    #Записываем в него заголовок новости(определён в зависимости от выбранного типа(Спорт или Обычная новость))
    target_file.write(news.header)
    target_file.write("\n")
    #Записываем текст новости(из файла или введённую вручную)
    target_file.write(news.content+"\n")
    #Записываем дату публикации, рассчитывается в момент ввода новости
    target_file.write("DATE OF PUBLISHING: "+publishtime+"\n")
    #Дублирование в консоль информации, добавленной в файл
    print(news.header)
    print(news.content)
    print("DATE OF PUBLISHING: "+publishtime+"\n")

#Итоговая функция для управления типом ввода и типом добавляемой новости:
def AddNews():
    global txt
    #Выбираем тип ввода новости
    inputtype = input("Источник новости (1 - Вручную, 2 - Импортировать из файла)\n")
    if inputtype == '1':
        #Выбираем тип новости
        newstype = input("Выберете тип новости (1 - Cпорт, 2 - Hовость):\n")
        if newstype == '1':
            createContent(input("Введите спортивную новость:\n"), '\nSPORT NEWS')
            Publish()
        elif newstype == '2':
            createContent(input("Введите новость:\n"), '\nNEWS')
            Publish()
    elif inputtype == '2':
        newstype = input("Выберете тип новости (1 - Cпорт, 2 - Hовость):\n")
        if newstype == '1':
            for item in ReadSportFile():
                createContent(item, '\nSPORT NEWS')
                Publish()
        elif newstype == '2':
            for item in ReadNewsFile():
                createContent(item, '\nNEWS')
                Publish()
######Функция статистики кол-ва слов в итоговом файле:
def wordsstattocsv():
    import re
    import csv
    fromfile = open('data.txt').read()
    #Делим исходный текст на абзацы:
    arr = fromfile.split('\n')
    #Массив, в который запишем каждый элемент текста(слово, дата, пробел и т.д.)
    commonarr = []
    #Массив, в который будем записывать только слова из исходного файла data.txt
    commonwords = []
    letters = []
    for item in arr:
        #Разделяем каждый абзац на слова..
        a = item.split(' ')
        for item in a:
            #..и каждое слово записываем в массив элементов исходного текста:
            commonarr.append(item.lower())
    # print(commonarr)
    #Проверяем commonarr на наличие цифр, пустых элементов, и забираем только слова:
    for item in commonarr:
        result = re.search(r'\D*', item)
        if (item != '') & (item == result.group(0)):
            commonwords.append(item)
    #print(commonwords)
    #print('\n')
    #Делим слова на буквы:
    for item in commonwords:
        word = list(item)
        for item in word:
            letters.append(item)
    #Общее количество букв:
    countletters = len(letters)
    map = {}
    # Считаем статистику слов:
    for item in commonwords:
        if item in map.keys():
            map[item] = map[item] + 1
        else:
            map[item] = 1
    # print(map)
    # Считаем статистику букв:
    mapletters = {}
    for item in letters:
        if item in mapletters.keys():
            mapletters[item] = mapletters[item] + 1
        else:
            mapletters[item] = 1
    #Запись статистики букв в XML:
    import xml.etree.ElementTree as ET
    data = ET.Element('data')
    for key, value in mapletters.items():
        letter = ET.SubElement(data, 'letter')
        count = ET.SubElement(data, 'count')
        letter.text = key
        count.text = mapletters[key].__str__()
    stat = ET.tostring(data)
    file = open('test.xml', "wb")
    file.write(stat)

continuework=''
#Запускаем итоговую функция управления добавлением новостей при запуске приложения
while continuework != 'N':
    AddNews()
    continuework = input("Продолжить? (Enter - Да; 'n' - Нет):\n").upper()
    #По завершению ввода новостей запускаем функцию статистики слов:
    if continuework.upper()=='N':
        wordsstattocsv()
        break