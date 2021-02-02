init_str='homEwork:\n\ntHis iz your homeWork, copy these Text to variable.\n\n\n\nYou NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.\n\n\n\nit iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.\n\n\n\nlast iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'
import re
#Ищем и считаем пробельные символы в исходном тексте:
print("=====================\nCoun_Space_symbols_in_initial_Text:\n",len(re.findall('\s',init_str)))

init_str_lower=(init_str.lower()).replace(' iz ',' is ')#Устанавливаем все буквы в lower и меняем iz на is:
split_str=init_str_lower.split('\n')#Делим строку на абзацы по \n
print("Список абзацев:\n",split_str)
a=0
i=0
result_item=[]#Массив, в который будем складывать список абзацев
while a < len(split_str): #Делим абзацы на предложения по "точка+пробел":
    split_sent=split_str[a].split('. ')
    while i< len(split_sent):#Начинаем каждое предложение с большой буквы:
        split_sent[i]=split_sent[i].capitalize()
        i=i+1
    paragraph_item=('. '.join(split_sent))#Формируем строку из предложений одного обзаца
    result_item.append(paragraph_item)#Добавляем абзац как строку в массив
    i=0
    a=a+1

#Формируем предложение из последних слов каждого предложения первоначальной строки с заменой точки на пробел и первое слово с прописной буквы:
end_of_sent=(' '.join(re.findall(r'\S*[.]',init_str_lower)).replace('.',' ')).capitalize()
end_of_sent=end_of_sent.replace('  ',' ')#Заменяем два пробела между словами на один
end_of_sent=(end_of_sent+'.').replace(' .','.')#Ставим точку в конце предложения и избавляемся от пробела перед ней
result_item.append(end_of_sent)#Добавляем предложение в массив абзацев

result=('\n'.join(result_item))#Объединяем элементы массива абзацев в строку
print('\n==================\nПервоначальный текст, с исправленным регистром(Каждое предложение с прописной буквы + Новое предложение):\n',result)
#Ищем и считаем пробельные символы в конечном тексте:
print("=====================\nCoun_Space_symbols_in_Result_text:\n",len(re.findall('\s',result)))

#Формируем предложенеи из последних слов каждого предложения первоначальной строки с заменой точки на пробел и первое слово с прописной буквы:
# end_of_sent=(' '.join(re.findall(r'\S*[.]',init_str_lower)).replace('.',' ')).capitalize()
# print('\nSentence from last words of text sentences:\n',end_of_sent+'.')