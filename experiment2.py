def swap(L, i, j):
    L[i], L[j] = L[j], L[i]


def find_min_index(L, start, end):
    min_index = n
    for i in range(n+1, len(L)):
        if L[i] < L[min_index]:
            min_index = i
    return min_index


def selection_sort2(L):
    start, end = 0, len(L) - 1
    while (start < end):
        min_index = find_min_index(L, start, end)


    for i in range(len(L)):
        min_index = find_min_index(L, i)
        swap(L, i, min_index)