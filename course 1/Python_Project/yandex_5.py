i = 0
read = 0
take = 0
string = input().split(' ')
array = [int(num) for num in string]
while ((take + array[1]) >= read):
    if (array[2] == 6 or array[2] == 7):
        i += 1
        read = read + i
        array[2] += 1
    else:
        i += 1
        read = read + i
        take = take + array[0]
        array[2] += 1
    if (array[2] == 8):
        array[2] = 1
print(i)
