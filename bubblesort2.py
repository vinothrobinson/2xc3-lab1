# ******************* Bubble sort code *******************
def swap(L, i, j):
    L[i], L[j] = L[j], L[i]


# Traditional Bubble sort
def bubble_sort(L):
    for i in range(len(L)):
        for j in range(len(L) - 1):
            if L[j] > L[j+1]:
                swap(L, j, j+1)


# Bubblesort optimization
def bubblesort2(L):
    for i in range(len(L)):
        temp = L[0]
        for j in range(len(L) - 1):
            if temp < L[j+1]:
                L[j] = temp
                temp = L[j+1]
                continue
            if temp > L[j+1]:
                L[j] = L[j+1]
                if (j+1) == len(L) - 1:
                    L[j+1] = temp