cols,rows = map(int,input().split())
chac = list(map(int, input().split()))

tile = [0 for __ in range(cols)]
for i in range(cols):
    tile[i] = list(map(int, input().split()))

steps = [(-1, 0),(1,0), (0,-1), (0,1)]
a = 0
b = 0

result = 1

next_col = chac[0]
next_row = chac[1]


for step in steps:
    while tile[next_col][next_row] == 1:
        next_col += step[0]
        next_row += step[1]
        if tile[next_col][next_row] == 0:
            result = result + 1




print(result)









