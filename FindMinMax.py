tp = (100,6,12,-1,754,9)

min = tp[0]
max = tp[0]

for i in range(len(tp)):
    if min > tp[i]:
        min = tp[i]

    if max < tp[i]:
        max = tp[i]
        
print("min : ",min)
print("max : ",max)