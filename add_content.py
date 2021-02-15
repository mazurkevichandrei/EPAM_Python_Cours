import datetime

class AddContent:
    def __init__(self, content, header):
        self.content=content
        self.header=header
    def pubdate(self):
        publishtime = datetime.date.today()
        print("DATE OF PUBLISHING: ",publishtime,"\n")

def Publish():
    print(news.header)
    print(news.content)
    news.pubdate()

def AddNews():
    global txt
    global news
    newstype = input("Выберете тип новости (1 - Cпорт, 2 - Hовость):\n")
    if newstype == '1':
        txt = input("Введите спортивную новость:\n")
        news = AddContent(txt, '\n===SPORT_NEWS===')
        Publish()
    elif newstype == '2':
        txt = input("Введите текст новости:\n")
        news = AddContent(txt, '\n===NEWS===')
        Publish()

continuework=''
while continuework != 'N':
    AddNews()
    continuework = input("Продолжить? (Enter - Да; 'n' - Нет):\n").upper()
