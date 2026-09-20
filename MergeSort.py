def mergeSort(arr, low, high):
    if low >= high:
        return
    mid = low + (high - low) // 2
    mergeSort(arr, low, mid)
    mergeSort(arr, mid + 1, high)
    merge(arr, low, mid, high)


def merge(arr, low, mid, high):
    temp = []
    i = low
    j = mid + 1

    while i <= mid and j <= high:
        if arr[i] < arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    while i <= mid:
        temp.append(arr[i])
        i += 1

    while j <= high:
        temp.append(arr[j])
        j += 1

    for x in range(len(temp)):
        arr[low + x] = temp[x]


lst = [5, 4, 3, 2, 1]
mergeSort(lst, 0, len(lst) - 1)
print(lst)
