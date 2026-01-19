L = int(input())
word = input()
M = 1234567891
r = 31

answer = 0
alphabet = "abcdefghijklmnopqrstuvwxyz"

for i in range(len(word)):
    num = alphabet.index(word[i]) + 1
    answer += num * (r ** i)

print(answer % M)
