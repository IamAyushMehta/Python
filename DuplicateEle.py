arr = [3, 2, 5, 13, 45, 13]

for i in range(0, len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[j] == arr[i]:
            print("contains duplicate element", arr[i])
