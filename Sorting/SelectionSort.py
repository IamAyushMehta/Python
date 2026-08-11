lst = [5,4,3,2,1]
def selectionSort():
    for i in range(len(lst) - 1):
        small = i
        for j in range(i+1, len(lst)):
            if lst[small] > lst[j]:
                small = j
        lst[small], lst[i] = lst[i], lst[small]
    return lst

print(selectionSort())