N = int(input())
cnt = 1
num = 666

while(1):
    if N == 1:
        print(666)
        break

    num += 1
    if '666' in str(num):
        cnt += 1
    if cnt == N:
        print(num)
        break