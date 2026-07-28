s = input("enter string : ")

for i in s:
    count = 0
    for j in s:
        if i == j:
            count += 1

    print(f"'{i}' : {count}")