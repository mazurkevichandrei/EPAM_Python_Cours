init_str='homEwork:\n\ntHis iz your homeWork, copy these Text to variable.\n\n\n\nYou NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.\n\n\n\nit iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.\n\n\n\nlast iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'
import re

#=====Функция для подсчёта пробельных символов в любом тексте:
def count_spaces (x):
    print('Coun_Space_symbols:')
    print(len(re.findall('\s', x)))

#=====Функция замены iz на is:
def fix_text(x):
    global init_str_lower
    init_str_lower = (x.lower()).replace(' iz ', ' is ')  # Устанавливаем все буквы в lower и меняем iz на is:
    return init_str_lower

#=====Функция деления строки на абзацы:
def split_string_to_articles(x):
    global split_str
    split_str=x.split('\n')#Делим строку на абзацы по \n
    print("Список абзацев:\n",split_str)
    return split_str

#=====Функция формирования предложение из последних слов каждого предложения первоначальной строки с заменой точки на пробел и первое слово с прописной буквы:
def create_additional_sent(x,y): #x - Из чего формируем предложение; y - Куда добавляем
    global end_of_sent
    end_of_sent=(' '.join(re.findall(r'\S*[.]',x)).replace('.',' ')).capitalize()
    end_of_sent=end_of_sent.replace('  ',' ')#Заменяем два пробела между словами на один
    end_of_sent=(end_of_sent+'.').replace(' .','.')#Ставим точку в конце предложения и избавляемся от пробела перед ней
    y.append(end_of_sent)#Добавляем предложение в массив абзацев

#=====Функция исправления регистра:
def fix_case(x):
    a=0
    i=0
    global result_item #Массив, в который будем складывать список абзацев
    result_item = []
    while a < len(x): #Делим абзацы на предложения по "точка+пробел":
        split_sent=split_str[a].split('. ')
        while i< len(split_sent):#Начинаем каждое предложение с большой буквы:
            split_sent[i]=split_sent[i].capitalize()
            i=i+1
        paragraph_item=('. '.join(split_sent))#Формируем строку из предложений одного обзаца
        result_item.append(paragraph_item)#Добавляем абзац как строку в массив
        i=0
        a=a+1
    return result_item

#=====Функция объединения элементов массива абзацев в строку:
def join_to_string(x):
    global result
    result=('\n'.join(x))#Объединяем элементы массива абзацев в строку
    print('\n==================\nПервоначальный текст, с исправленным регистром(Каждое предложение с прописной буквы + Новое предложение):\n',result)
    return result

#Запускаем функцию для подсчёта пробельных символов в первоначальном тексте:
count_spaces(init_str)
#Запускаем исправление текста:
fix_text(init_str)
#Запускаем деление на абзацы:
split_string_to_articles(init_str_lower)
#Запускаем исправленеи регистра:
fix_case(split_str)
#Запускаем формарование нового предложения:
create_additional_sent(init_str_lower,result_item)
#Запускаем объединение массива в строку:
join_to_string(result_item)
#Запускаем функцию подсчёта пробельных символов в итоговом тексте:
count_spaces(result)