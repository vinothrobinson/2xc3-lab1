def dual_quicksort(L):
    copy = dual_quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]


def dual_quicksort_copy(L):
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
    return dual_quicksort_copy(left) + [pivot_l] + dual_quicksort_copy(middle) + [pivot_r] + dual_quicksort_copy(right)
