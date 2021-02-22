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
            createContent(input("Введите спортивную новость:\n"), '\n===SPORT_NEWS===')
            Publish()
        elif newstype == '2':
            createContent(input("Введите новость:\n"), '\n===NEWS===')
            Publish()
    elif inputtype == '2':
        newstype = input("Выберете тип новости (1 - Cпорт, 2 - Hовость):\n")
        if newstype == '1':
            for item in ReadSportFile():
                createContent(item, '\n===SPORT_NEWS===')
                Publish()
        elif newstype == '2':
            for item in ReadNewsFile():
                createContent(item, '\n===NEWS===')
                Publish()

continuework=''
#Запускаем итоговую функция управления добавлением новостей при запуске приложения
while continuework != 'N':
    AddNews()
    continuework = input("Продолжить? (Enter - Да; 'n' - Нет):\n").upper()