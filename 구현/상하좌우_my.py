n = int(input())
data = list (map(str, input().split()))


cal = 1
row = 1

for i in range(len(data)):
    if data[i] == "L":
        row  = row - 1
    if row == 0:
        row = 1
    elif row == n + 1:
        row = n


    if data[i] == "R":
        row = row + 1
    if row == 0:
        row = 1
    elif row == n + 1:
        row = n


    if data[i] == "U":
        cal = cal - 1
    if cal == 0:
        cal = 1
    elif cal == n + 1:
        cal = n

    if data[i] == "D":
        cal = cal + 1
    if cal == 0:
        cal = 1
    elif cal == n + 1:
        cal = n


print(f'{cal} {row}')






