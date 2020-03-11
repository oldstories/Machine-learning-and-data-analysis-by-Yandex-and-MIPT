serv_count = int(input())
errs = []
err_sum = 0
for i in range(serv_count):
    tmp = input().split(' ')
    err = int(tmp[0])
    chance = int(tmp[1])
    err_sum += err * chance
    errs.append([err, chance])

for i in errs:
    print(i[0] * i[1] / err_sum)
