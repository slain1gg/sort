def bin_search(a, x):
    l = 0
    r = len(a)-1
    while l <= r:
        mid = (l+r)//2
        if a[mid] == x:
            return mid
        if x <= a[mid]:
            r = mid - 1
        else:
            l = mid + 1
    return l


def bin_sort(a):
    n = len(a)
    for i in range(1, n):
        place_for_insert = bin_search(a[:i+1], a[i])
        elem_for_insert = a[i]
        if i != place_for_insert:
            for j in range(i, place_for_insert-1, -1):
                a[j] = a[j-1]
            a[place_for_insert]=elem_for_insert
    return a

a = [9,8,7,6,5,4,3,2,1]
print(bin_sort(a))
