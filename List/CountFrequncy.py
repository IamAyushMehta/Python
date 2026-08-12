lst = [1,5,2,4,3,7,8,9,1,2,5]

freq = []
for i in range(len(lst)): 
    count = 0
    for j in range(len(lst)):
        if lst[i] == lst[j] and lst[i] not in freq:
            count += 1
    freq.append(lst[i])
    print(lst[i], " = ", count)