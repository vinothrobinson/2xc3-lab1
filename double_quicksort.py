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
