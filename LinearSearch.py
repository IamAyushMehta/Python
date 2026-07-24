arr = [23, 54, 76, 13, 7, 45, 15]

for i in range(0, len(arr)):
    if arr[i] % 3 == 0 and arr[i] % 5 == 0:
        print("Found at index:", i, "Value:", arr[i])
        break
else:
    print("not found")
