def quickSort(arr, s, e):
    if e - s + 1 <= 1:
        return arr
    p = arr[e]
    left = s

    for i in range(s, e):
        if arr[i] < p:
            temp = arr[i]
            arr[i] = arr[left]
            arr[left] = temp
            left += 1
    
    arr[e] = arr[left]
    arr[left] = p

    quickSort(arr, s, left - 1)
    quickSort(arr, left + 1, e)
    return arr

arr = [6,2,4,1,3]
quickSort(arr, 0, 4)
print(arr)