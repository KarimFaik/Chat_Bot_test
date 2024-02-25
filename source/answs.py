import xml.etree.ElementTree as ET


def accresp(maintext):

    answerid = -1
    with open('data.xml', 'r', encoding='utf-8') as file:
        data = file.read()

    root = ET.fromstring(data)

    keywords = [
        ['войти в эбс', 'вход в эбс'],
        ['доступ в базы'],
        ['когда сдать книгу', 'когда сдать учебник', 'куда сдавать учебник', 'куда сдавать книг','куда сдать книг','куда сдать учебник'],
        ['какие книги вернуть', 'задолженность', 'взял в'],
        ['подписать обходной лист'],
        ['потерял книгу', 'потерял книги'],
        ['продлить книгу', 'продлить книги'],
        ['что такое унибц', 'что такое нб'],
        ['Когда работает библиотека', 'Как работает библиотека', 'Время работы библиотеки'],
        ['записаться в унибц', 'записаться в библиотеку', 'записаться в нб'],
        ['сдать диссертацию'],
        ['можно взять в библеотеке главного корпуса'],
        ['удаленный доступ к'],
        ['что такое эбс'],
        ['электронную версию'],
        ['не успел сдать книгу'],
        ['читальный зал для мусульман', 'место для мусульман', 'уголок для масульман'],
        ['зарегистрироваться в туис']
    ]
    
    for k in range(len(keywords)-1):
        flag = 0
        for text in keywords[k]:
            txt = text[0:len(text)-1].split(' ')
            for el in txt:
                if el in maintext.lower():
                    flag = 1
                else:
                    flag = 0
                    break
            if flag != 0:
                break
        if flag != 0:
            answerid = k
            break
    if answerid >= 0:
        for answer in root.findall('answer'):
            if int(answer.attrib['id']) == answerid + 1:
                return answer.text.strip()
    else:
        return "Простите, я не знаю ответ на ваш вопрос"
