lst = [1,4,2,87,26,6]

smallest = lst[0]
largest = lst[0]

for i in range(len(lst)):

    if largest < lst[i]:
        largest = lst[i]

    if  smallest > lst[i]:
        smallest = lst[i]


print("smallest : ",smallest)
print("largest : ",largest)
