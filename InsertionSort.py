def insertionSort(arr):
    for i in range(1, len(arr)):
        curr = arr[i]
        prev = i-1
        while(prev >= 0 and arr[prev] > curr):
            arr[prev + 1] = arr[prev]
            prev -= 1
        arr[prev + 1] = curr
    return arr

lst = [5,4,3,2,1]
print(insertionSort(lst))