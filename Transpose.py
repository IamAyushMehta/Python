rows = int(input("enter rows : "))
cols = int(input("enter cols : "))

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input("enter row : ")))
    print()
    matrix.append(row)

col = len(matrix[0])
row = len(matrix)


transpose = []
for i in range(col):
    new_row = []
    for j in range(row):
        new_row.append(matrix[j][i])
    transpose.append(new_row)

for i in transpose:
    print(i)