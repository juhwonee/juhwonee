num = input()
weight = 0
remo = 0
total = 0
weight1 = 0

for i in range(13):
    if num[i] == '*':
        remo = i
        break

if remo%2 == 0:
    weight = 1
else:
    weight = 3

for j in range(13):
    if num[j] == '*':
        continue
    if j%2 == 0:
        weight1 = 1
        total += int(num[j]) * weight1
    else:
        weight1 = 3
        total += int(num[j]) * weight1

for k in range(10):
    if (total + k * weight) % 10 == 0:
        print(k)
        break