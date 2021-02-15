import datetime

class AddContent:
    def __init__(self, content, header):
        self.content=content
        self.header=header
    def pubdate(self):
        global publishtime
        publishtime = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
        return  publishtime

def Publish():
    target_file=open("data.txt","a")
    target_file.write(news.header)
    target_file.write("\n")
    target_file.write(news.content+"\n")
    target_file.write("DATE OF PUBLISHING: "+publishtime+"\n")
    print(news.header)
    print(news.content)
    print("DATE OF PUBLISHING: "+publishtime+"\n")

def AddNews():
    global txt
    global news
    newstype = input("Выберете тип новости (1 - Cпорт, 2 - Hовость):\n")
    if newstype == '1':
        txt = input("Введите спортивную новость:\n")
        news = AddContent(txt, '\n===SPORT_NEWS===')
        news.pubdate()
        Publish()
    elif newstype == '2':
        txt = input("Введите текст новости:\n")
        news = AddContent(txt, '\n===NEWS===')
        news.pubdate()
        Publish()

continuework=''
while continuework != 'N':
    AddNews()
    continuework = input("Продолжить? (Enter - Да; 'n' - Нет):\n").upper()
