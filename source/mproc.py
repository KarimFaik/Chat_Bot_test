import xml.etree.ElementTree as ET


def accresp(maintext): # функция предназаначенная для нахождения ответа на вопрос по ключевым словам

    answerid = -1 # id ответа, отрицательнео значение значит что id не найден
    with open('answer_data.xml', 'r', encoding='utf-8') as file: #открываем xml файл с ответами на чтение
        data = file.read()

    root = ET.fromstring(data) #структура с ответами

    keywords = [
        ['войти в эбс', 'вход в эбс'],
        ['доступ в базы'],
        ['когда сдать книгу', 'когда сдать учебник', 'куда сдавать учебник', 'куда сдавать книгу','как сдать книгу','как сдать учебник','сдать книгу','сдать учебник'],
        ['какие книги вернуть', 'задолженность', 'взял в'],
        ['подписать обходной лист'],
        ['потерял книгу', 'потерял книги', 'потеряла книги','потеряла книгу','при утере'],
        ['продлить книгу', 'продлить книги'],
        ['что такое унибц', 'что такое нб'],
        ['когда работает библиотека', 'как работает библиотека', 'время работы библиотеки'],
        ['записаться в унибц', 'записаться в библиотеку', 'записаться в нб'],
        ['сдать диссертацию'],
        ['можно взять в библеотеке главного корпуса'],
        ['удаленный доступ к'],
        ['что такое эбс'],
        ['электронную версию'],
        ['не успел сдать книгу'],
        ['читальный зал для мусульман', 'место для мусульман', 'уголок для масульман'],
        ['зарегистрироваться в туис']
    ] #ключевые слова разбитые по группам
    
    for k in range(len(keywords)-1): # простой цикл перебирающий список keywords поиндексно
        flag = 0 # флаг предназначенный для остановки работы цикла в случае нахождении верного ответа
        for text in keywords[k]: # перебираем строки ключевых слов
            txt = text[0:len(text)-1].split(' ') # разбиваем строки на отдельные ключевые слова
            for el in txt: # перебираем ключевые слова
                if el in maintext.lower(): # если ключевое слово есть в вопросе, то меняем флаг на 1
                    flag = 1
                else:
                    flag = 0 # если не находим ключевое слово меняем флаг на 0
                    break
            if flag != 0: # в случае успеха ломаем этот цикл
                break
        if flag != 0: # также ломаем цикл, и получаем id ответа
            answerid = k
            break
    if answerid >= 0: # в случае если id найден, достаем текст из полученный ранее из xml 
        for answer in root.findall('answer'):
            if int(answer.attrib['id']) == answerid + 1:
                return answer.text.strip()
    else:
        return "Простите, я не знаю ответ на ваш вопрос" # если соответсвующий ответ не найден, то даем знать об этом пользователю

def addfeedback(maintext,userid):
    
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse('feedback_data.xml',parser = parser)
    root = tree.getroot()
    first = root.find("feedback")
    attributes = {"from_user": str(userid)}
    child = ET.SubElement(root,"text",attributes)
    child.text = maintext
    ET.dump(tree)
    tree.write('feedback_data.xml',encoding="utf-8",xml_declaration=True)