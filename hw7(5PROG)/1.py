# 1) Словами (русского языка) являются лишь те, в которых есть хотя бы одна буква русского алфавита.
# 2) Словом (русского языка) с заглавной буквы является лишь то, которое является словом (русского алфавита) and первая из букв русского алфавита в этом слове является заглавной.
# Т.е. к словам с заглавной буквы я причисляю "(Далее...)", "2+2=Четыре", "abcdefg_АБРАКАДАБРА" и т.д.
f = open('file.txt', 'r', encoding = 'utf-8')
alphUP = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alphDOWN = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alph = alphUP + alphDOWN # приятнее иметь отдельную переменную, чем писать что-то типа (alphUP + alphDOWN).find(l[i][j])
allw = 0 # счётчик слов, содержащих букву русского алфавита
bigw = 0 # счётчик слов, в которых первой из букв русского алфавита идёт заглавная буква
fl = 0 # флажок, чтобы определить, файл состоит из пробелов или там есть хотя бы один символ
for line in f :
    l = line.split()
    for i in range(len(l)) : # не использую enumerate, потому что никак не использую индекс слова, хотя приходится писать [x][y]
        allw += 1 # по презумпции невиновности считаю, что в этом слове есть хотя бы одна буква русского алфавита
        if fl != 1 and l[i] != '' and l[i] != '\ufeff': # 1 условие - чтобы не переприсваивать переменную (хотя очень неприятно, что приходится делать каждый раз проверку)
                                                        # 2 условие - проверка на наличие хотя бы одного непробельного символа; 3 условие - когда сохраняешь текст в notepad++, он почему-то начинается с этого тега, но я не считаю его символом
            fl = 1
        if alphUP.find(l[i][0]) >= 0 : # Если первая буква заглавная, увеличиваем счётчик
            bigw += 1
        else : # Вдруг в начале идёт куча символов не из русского алфавита, а потом начинается слово с большой кириллической буквы, как в "2+2=Четыре"? Проверяем!
            j = 0
            while j < len(l[i]) and alph.find(l[i][j]) == -1 : # ищем индекс первого символа из русского алфавита в слове
                j += 1
            if j == len(l[i]) : # проверяем, а был ли мальчик!
                allw -= 1 # это в моём понимании не слово русского языка, а лишь бессмысленный набор символов или слово из другого языка
            elif alphUP.find(l[i][j]) >= 0 : 
                bigw += 1
if allw != 0 :
    print('The percentage of words, which start with uppercase equals to ', round(bigw / allw * 100, 3), '%', sep = '')
else :
    if fl == 0 :
        print('There are no words at all! Try to use another file.')
    else :
        print('There are some symbols, but no words in Russian. Try to use another file!')
f.close()
