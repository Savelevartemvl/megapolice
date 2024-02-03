f = open("tablica.txt", encoding="UTF-8").read()
f = f.split('\n')
arr = []
for i in f:
    arr.append(i.split('\t'))
arr[0].append('total')
for i in range(1, len(arr)):
    arr[i].append(float(arr[i][3])*float(arr[i][4]))

summa = 0
for i in range(1, len(arr)):
    if arr[i][0] == 'Закуски':
        summa += arr[i][5]
print(summa)
#https://github.com/Savelevartemvl/megapolice/tree/main