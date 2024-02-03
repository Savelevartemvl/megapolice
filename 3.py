#считываем файл и создаём массив для работы
f = open("products_new.txt", encoding="UTF-8").read()
f = f.split('\n')
arr = []
for i in f:
    arr.append(i.split('\t'))

#основной цикл, работяющий до ввода слова "молоко"
s = input("Выберите категорию: ")
while s != 'молоко':
    p = ''
    c = 100000000.0
    for i in range(1, len(arr)-1):
        if (arr[i][0] > s and p == ''):  #если не наши категорию
            print('Такой категории не существует в нашей БД')
            break
        elif (arr[i][0] > s): # если просмотренная котегория закончилась
            print(f'В категории: "{s}" товар: "{p}" был куплен "{c}" раз')
            break
        elif(arr[i][0] == s and float(arr[i][4]) < c): #обновляем значения
            p = arr[i][1]
            c = float(arr[i][4])
    s = input("Выберите категорию: ")
#https://github.com/Savelevartemvl/megapolice/tree/main