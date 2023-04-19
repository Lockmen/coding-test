n = int(input())
li = []

for i in range(n):
    li.append(input().split())



li.sort(key=lambda x:-int(x[1]))
li.sort(key=lambda x:int(x[2]))
li.sort(key=lambda x:-int(x[3]))
li.sort(key=lambda x:(x[0]))

for j in li:
    print(j[0])




