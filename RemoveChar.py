s1 = "ayushmehta"
lst = []

for i in s1:
    if i not in lst:
        lst.append(i) 

for i in lst:
    count = 0
    for j in s1:
        if i == j:
            count += 1
    print(f"{i} : {count}")