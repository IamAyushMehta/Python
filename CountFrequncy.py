lst = [1, 1, 1, 2]
freq = []
for i in lst:
    count = 0
    for j in lst:
        if i == j:
            count += 1
    freq.append(f"{i} : {count}")

print(sorted(lst))
freq = sorted(set(freq))
for i in freq:
    print(i)


def freqCount(lst, tar):
    count = 0
    for i in lst:
        if tar == i:
            count += 1
    return f"{tar} : {count}"


lst1 = set(lst)
for i in lst1:
    print(freqCount(lst, i))
