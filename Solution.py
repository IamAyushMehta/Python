def bubbleSort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) -1 -i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def selectionSort(arr):
    for i in range(len(arr) - 1):
        smallest = i
        for j in range(i+1,len(arr)):
            if arr[smallest] > arr[j]:
                smallest = j
        arr[smallest], arr[i] = arr[i], arr[smallest]

    return arr

def insertionSort(arr):
    for i in range(len(arr)):
        curr = arr[i]
        prev = i-1
        while(prev >= 0 and arr[prev] > curr):
            arr[prev + 1] = arr[prev]
            prev -= 1
        arr[prev + 1] = curr
    return arr;
lst = [5,4,8,7,9,1]
# print(bubbleSort(lst))
# print(selectionSort(lst))
# print(insertionSort(lst))