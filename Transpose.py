lst = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

result = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for i in range(len(lst)):
    for j in range(len(lst[0])):
        result [i][j] = lst[j][i]
    
for i in result:
    print(i)