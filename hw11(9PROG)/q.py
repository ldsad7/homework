# Вариант №6

import re

# зил: загрузил(ся), загрузила(сь), загрузили(сь), загрузило(сь),
# зит: загрузит(ся),загрузите(сь), загрузить(ся),
# зивши: загрузивши(сь), загрузивший(ся), загрузившим(ся), загрузившими(ся), загрузившие(ся), загрузивших(ся),
# зивше: загрузившего(ся), загрузившему(ся), загрузившем(ся), загрузившей(ся), загрузившее(ся), загрузившею(ся),
# зивша: загрузившая(ся),
# зившу: загрузившую(ся),
# зив: загрузив,
# зи: загрузишь(ся), загрузи(сь), загрузим(ся),
# зя: загрузят(ся)

# загру(з(ят(ся)?|и(шь(ся)?|(сь)?|м(ся)?|л((ся)?|а(сь)?|и(сь)?|о(сь)?)|т((ся)?|е(сь)?|ь(ся)?)|в(ш(ую(ся)?|ая(ся)?|е(го(ся)?|му?(ся)?|й(ся)?|е(ся)?|ю(ся)?)|и((сь)?|й(ся)?|м(и)?(ся)?|е(ся)?|х(ся)?)?))|ж(у(сь)?|ен(а|о|ы)?|ён|(е|ё)нн(ая|ую|о(м(у)?|ю|е|го|й)|ы(м(и)?|й|е|х))) 

# ж(e|ё)нны: загруж(е|ё)нный, загруж(е|ё)нным, загруж(е|ё)нные, загруж(е|ё)нных, загруж(е|ё)нными 
# ж(e|ё)нно: загруж(е|ё)нному, загруж(е|ё)нною, загруж(е|ё)нное, загруж(е|ё)нного, загруж(е|ё)нной,  загруж(е|ё)нном, 
# ж(e|ё)нну: загруж(е|ё)нную, 
# ж(e|ё)нна: загруж(е|ё)нная,
# ж(e|ё)н: загруж(е|ё)н,
# жу:загружу(сь),
# жен(а|о|ы): загружена, загружено, загружены

# функция, считывающая файл
def reading(name):
    f = open(name, 'r', encoding = 'utf-8')
    words = f.read().replace('\n', ' ').split()
    f.close()
    return words

# функция, очищающая слова в массиве
def cleaning(words):
    for i, word in enumerate(words) :
        words[i] = word.lower().strip('.,/1234567890@#$%^&*><~`|\}{][!?():;-_=+"\'')
    return words

# функция, распечатывающая формы глагола "загрузить"
def printing(words):
    for word in words:
        if re.search('загру(з(ят(ся)?|и(шь(ся)?|(сь)?|м(ся)?|л((ся)?|а(сь)?|и(сь)?|о(сь)?)|т((ся)?|е(сь)?|ь(ся)?)|в(ш(ую(ся)?|ая(ся)?|е(го(ся)?|му?(ся)?|й(ся)?|е(ся)?|ю(ся)?)|и((сь)?|й(ся)?|м(и)?(ся)?|е(ся)?|х(ся)?)))?))|ж(у(сь)?|ен(а|о|ы)?|ён|(е|ё)нн(ая|ую|о(м(у)?|ю|е|го|й)|ы(м(и)?|й|е|х))))$', word):       
            print(word)

def main():
    words = cleaning(reading(input('Введите, пожалуйста, название файла:\n')))
    printing(words)



main()
