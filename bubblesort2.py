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
        bubble(L, i)
        """
        for j in range(len(L) - 1):
            if L[j] > L[j+1]:
                swap(L, j, j+1)
        """

def bubble(L, i):
    value = L[i]
    while i < len(L):
        if L[i] > L[j]:
            i += 1
        else:
            L[i] = value
            return
    return