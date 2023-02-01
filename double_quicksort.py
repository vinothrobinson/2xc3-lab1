def quicksort(L):
    copy = quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]


def quicksort_copy(L):
    if len(L) < 2:
        return L
    pivot = L[0]
    left, right = [], []
    for num in L[1:]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)
    return quicksort_copy(left) + [pivot] + quicksort_copy(right)


def quicksort_dual(L):
    copy = quicksort_copy_dual(L)
    for i in range(len(L)):
        L[i] = copy[i]


def quicksort_copy_dual(L):
    if len(L) < 2:
        return L
    pivot_l = L[0]
    pivot_r = L[1]
    if pivot_l > pivot_r:
        pivot_l, pivot_r = pivot_r, pivot_l
    left, middle, right = [], [], []
    for num in L[2:]:
        if num < pivot_l:
            left.append(num)
        elif num > pivot_r:
            right.append(num)
        else:
            middle.append(num)
    return quicksort_copy_dual(left) + [pivot_l] + quicksort_copy_dual(middle) + [pivot_r] + quicksort_copy_dual(right)


Ls = [[], [1], [1, 2], [2, 1], [1, 2, 3], [3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 6, 43, 9, 4, 1, 7, 4, 7, 3423, 56]]

for L in Ls:
    quicksort_dual(L)
    print(L)