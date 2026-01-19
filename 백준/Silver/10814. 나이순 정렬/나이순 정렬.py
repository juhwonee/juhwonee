N = int(input())
people = []

for idx in range(N):
    age, name = input().split()
    people.append((int(age), idx, name))

people.sort()

for age, idx, name in people:
    print(age, name)
