f = open("products_new.txt", encoding="UTF-8").read()
f = f.split('\n')
arr = []
for i in f:
    arr.append(i.split('\t'))

s = input("Выберите категорию: ")
while s != 'молоко':
    p = ''
    c = 100000000.0
    for i in range(1, len(arr)-1):
        if (arr[i][0] > s and p == ''):
            print('Такой категории не существует в нашей БД')
            break
        elif (arr[i][0] > s):
            print(f'В категории: "{s}" товар: "{p}" был куплен "{c}" раз')
            break
        elif(arr[i][0] == s and float(arr[i][4]) < c):
            p = arr[i][1]
            c = float(arr[i][4])
    s = input("Выберите категорию: ")
#https://github.com/Savelevartemvl/megapolice/tree/main