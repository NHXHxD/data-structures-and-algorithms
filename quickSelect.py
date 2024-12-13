# find the kth largest element in an array
a = [2,5,3,6,8,4]
k = 1
k = len(a) - k
def quickSelect(l, r):
    pivot, p = a[r], l
    for i in range(l, r):
        if a[i] <= pivot:
            a[i], a[p] = a[p], a[i]
            p += 1
    a[r], a[p] = a[p], a[r]
    if k > p:
        return quickSelect(p + 1, r)
    elif k < p:
        return quickSelect(l, p - 1)
    else: 
        return a[p]
print(quickSelect(0,5))
