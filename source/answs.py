import xml.etree.ElementTree as ET


def accresp(maintext):

    with open('data.xml', 'r', encoding='utf-8') as file:
        data = file.read()

    root = ET.fromstring(data)

    keywords = [
        ['войти в эбс', 'вход в эбс'],
        ['доступ в базы'],
        ['когда сдать книгу', 'когда сдать учебник', 'куда сдавать учебник', 'куда сдавать книг'],
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

    for idx, keyword_group in enumerate(keywords):
        for keyword in keyword_group:
            if keyword.lower() in maintext.lower():
                for answer in root.findall('answer'):
                    if int(answer.attrib['id']) == idx + 1:
                        return answer.text.strip()
    return "Простите, я не знаю ответ на ваш вопрос"
