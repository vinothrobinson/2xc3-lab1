def swap(L, i, j):
    L[i], L[j] = L[j], L[i]


def find_min_index(L, lo, hi):
    min_index = lo
    for i in range(lo + 1, hi+1):
        if L[i] < L[min_index]:
            min_index = i
    return min_index


def find_max_index(L, lo, hi):
    max_index = lo
    for i in range(lo + 1, hi+1):
        if L[i] > L[max_index]:
            max_index = i
    return max_index


def selection_sort2(L):
    lo, hi = 0, len(L) - 1
    while lo < hi:
        min_index = find_min_index(L, lo, hi)
        swap(L, lo, min_index)
        lo += 1

        max_index = find_max_index(L, lo, hi)
        swap(L, max_index, hi)
        hi -= 1