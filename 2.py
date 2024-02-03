def srav(a, b):
    if a < b:
        return True
    else:
        return False

f = open("products_new.txt", encoding="UTF-8").read()
f = f.split('\n')
arr = []
for i in f:
    arr.append(i.split('\t'))

#print(arr)

i = 2
while i < len(arr)-1:
    if (srav(arr[i][0], arr[i-1][0])):
        while i == 1 or srav(arr[i][0], arr[i-1][0]) != False:
            a = arr[i-1]
            arr[i-1] = arr[i]
            arr[i] = a
            i -= 1
    i+=1

#print(arr)
print(f'В категории: "{arr[1][0]}" самый дорогой товар: "{arr[1][1]}" его цена за единицу товара составляет "{arr[1][3]}"')

file = open("products_new.txt", 'w')
for i in arr:
    file.write('\t'.join(i)+'\n')
#https://github.com/Savelevartemvl/megapolice/tree/main