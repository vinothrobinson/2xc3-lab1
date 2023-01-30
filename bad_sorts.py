"""
This file corresponds to the first graded lab of 2XC3.
Feel free to modify and/or add functions to this file.
"""
import math
import random
import timeit
import matplotlib.pyplot as plot
import function_info
import selection_sort2
import bubblesort2


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


def experiment1(n, k, functions):

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

    return total_times

def experiment3(n, k, functions):

    total_times = []
    for _ in range(len(functions)):
        total_times.append([])

    max_swaps = int(n*math.log(n, 2)/2)

    for i in range(max_swaps):
        L = create_near_sorted_list(n, k, i)

        for j in range(len(functions)):
            average = 0

            for _ in range(10):
                L_copy = L.copy()
                start = timeit.default_timer()
                functions[j].f(L_copy)
                end = timeit.default_timer()
                average += (end-start)

            average /= 10
            total_times[j].append(average)

    return total_times

def graph_exp1():
    for i in range(len(functions_exp1)):
        plot.plot(total_times_exp1[i], label = functions_exp1[i].name)
    plot.legend()
    plot.title("Sorting Algorithms: List Length vs. Time")
    plot.xlabel("List Length")
    plot.ylabel("Time (sec)")
    plot.show()

def graph_exp3():
    for i in range(len(functions_exp3)):
        plot.plot(total_times_exp3[i], label=functions_exp3[i].name)
    plot.legend()
    plot.title("Sorting Algorithms: Number of Swaps (sortedness) vs. Time")
    plot.xlabel("Number of Swaps")
    plot.ylabel("Time (sec)")
    plot.show()

functions_exp1 = [function_info.FunctionInfo(insertion_sort, "Insertion Sort"),
             function_info.FunctionInfo(insertion_sort2, "Insertion Sort 2"),
             function_info.FunctionInfo(bubble_sort, "Bubble Sort"),
             function_info.FunctionInfo(bubblesort2.bubblesort2, "Bubble Sort 2"),
             function_info.FunctionInfo(selection_sort, "Selection Sort"),
             function_info.FunctionInfo(selection_sort2.selection_sort2, "Selection Sort 2")]
#total_times_exp1 = experiment1(100, 100, functions_exp1)
functions_exp3 = [function_info.FunctionInfo(insertion_sort, "Insertion Sort"),
                  function_info.FunctionInfo(bubble_sort, "Bubble Sort"),
                  function_info.FunctionInfo(selection_sort, "Selection Sort")]
total_times_exp3 = experiment3(500, 500, functions_exp3)
graph_exp3()

# Graphing function performance on individual plots
# for i in range(len(functions)):
#     plot.plot(total_times[i])
#     plot.title(f"{functions[i].name}: List Length vs. Time")
#     plot.xlabel("List Length")
#     plot.ylabel("Time (sec)")
#     plot.show()

# Comparing function performance on same plot