"""
This file corresponds to the first graded lab of 2XC3.
Feel free to modify and/or add functions to this file.
"""
import random
import timeit
import matplotlib.pyplot as plot
import function_info
import selection_sort2


# Create a random list length "length" containing whole numbers between 0 and max_value inclusive
def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]


# Creates a near sorted list by creating a random list, sorting it, then doing a random number of swaps
def create_near_sorted_list(length, max_value, swaps):
    L = create_random_list(length, max_value)
    L.sort()
    for _ in range(swaps):
        r1 = random.randint(0, length - 1)
        r2 = random.randint(0, length - 1)
        swap(L, r1, r2)
    return L


# I have created this function to make the sorting algorithm code read easier
def swap(L, i, j):
    L[i], L[j] = L[j], L[i]


# ******************* Insertion sort code *******************

# This is the traditional implementation of Insertion Sort.
def insertion_sort(L):
    for i in range(1, len(L)):
        insert(L, i)


def insert(L, i):
    while i > 0:
        if L[i] < L[i-1]:
            swap(L, i-1, i)
            i -= 1
        else:
            return


# This is the optimization/improvement we saw in lecture
def insertion_sort2(L):
    for i in range(1, len(L)):
        insert2(L, i)


def insert2(L, i):
    value = L[i]
    while i > 0:
        if L[i - 1] > value:
            L[i] = L[i - 1]
            i -= 1
        else:
            L[i] = value
            return
    L[0] = value


# ******************* Bubble sort code *******************

# Traditional Bubble sort
def bubble_sort(L):
    for i in range(len(L)):
        for j in range(len(L) - 1):
            if L[j] > L[j+1]:
                swap(L, j, j+1)


# ******************* Selection sort code *******************

# Traditional Selection sort
def selection_sort(L):
    for i in range(len(L)):
        min_index = find_min_index(L, i)
        swap(L, i, min_index)


def find_min_index(L, n):
    min_index = n
    for i in range(n+1, len(L)):
        if L[i] < L[min_index]:
            min_index = i
    return min_index

# ******************* Testing Functions *******************


def experiment(n, k, functions):
    total_times = []
    for _ in range(len(functions)):
        total_times.append([])
    trial_times = []

    for i in range(n):

        for _ in range(len(functions)):
            trial_times.append(0)

        test_lists = []

        TRIAL_NUM = 100
        for _ in range(TRIAL_NUM):
            test_lists.append(create_random_list(i, k))
            for _ in range(1, len(functions)):
                test_lists.append(test_lists[0].copy())

            for j in range(len(functions)):
                start = timeit.default_timer()
                functions[j].f(test_lists[j])
                end = timeit.default_timer()
                trial_times[j] += end - start

        for j in range(0, len(functions)):
            total_times[j].append(trial_times[j] / TRIAL_NUM)

    for i in range(len(functions)):
        print(f"{functions[i].name}: {trial_times[i] / n}")

    for i in range(len(functions)):
        plot.plot(total_times[i])
        plot.title(f"{functions[i].name}: List Length vs. Time")
        plot.xlabel("List Length")
        plot.ylabel("Time (sec)")
        plot.show()


functions = [function_info.FunctionInfo(insertion_sort, "Insertion Sort"),
             function_info.FunctionInfo(bubble_sort, "Bubble Sort"),
             function_info.FunctionInfo(selection_sort, "Selection Sort"),
             function_info.FunctionInfo(selection_sort2.selection_sort2, "Selection Sort 2")]
experiment(100, 10, functions)
