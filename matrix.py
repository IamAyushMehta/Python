row = int(input("enter rows : "))
col = int(input("enter cols : "))

matrix = []

for i in range(row):
    row = []
    for j in range(col):
        row.append(int(input("enter in row : ")))
    print()
    matrix.append(row)

for i in matrix:
    print(i)