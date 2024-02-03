# megapolice

# Общее

f = open("tablica.txt", encoding="UTF-8").read()
f = f.split('\n')
arr = []
for i in f:
    arr.append(i.split('\t'))
-- открывает и сохраняет в массив данные из файла


file = open("products_new.txt", 'w')
for i in arr:
    file.write('\t'.join(i)+'\n')
-- сохраняет новую таблицу

# Задача №1

#создаём новый столбец, в который будем записывать total
arr[0].append('total')
for i in range(1, len(arr)):
    arr[i].append(str(float(arr[i][3])*float(arr[i][4])))

-- для каждой строки добавляет новое значение в конец равное произведению Count и Price per unit

# Задача №2

i = 2
while i < len(arr)-1:
    if (srav(arr[i][0], arr[i-1][0])):
        while i == 1 or srav(arr[i][0], arr[i-1][0]) != False:
            a = arr[i-1]
            arr[i-1] = arr[i]
            arr[i] = a
            i -= 1
    i+=1

-- основной цикл сортировки (пузырьком)

def srav(a, b):
    if a < b:
        return True
    else:
        return False

-- функция сравнения двух строк

# Задание №3

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

-- основной цикл обработки запросов