import math
import timeit
import matplotlib.pyplot as plot
import bad_sorts
import improved_bad_sorts
import good_sorts
import double_quicksort
import iterative_mergesort
import function_info
# ******************* Testing Functions *******************
# This function was used to test experiments 1, 2, 4, 6, 7, and 8
def testing_function1(n, k, functions):
    total_times = []
    TRIAL_NUM2 = 100
    for _ in range(len(functions)):
        total_times.append([])

    for i in range(n):
        L = bad_sorts.create_random_list(i, k)

        for j in range(len(functions)):
            average = 0

            for _ in range(TRIAL_NUM2):
                L_copy = L.copy()
                start = timeit.default_timer()
                functions[j].f(L_copy)
                end = timeit.default_timer()
                average += (end - start)

            average /= TRIAL_NUM2
            total_times[j].append(average)

    for i in range(len(functions)):
        print(f"{functions[i].name}: {total_times[i][-1]}")

    return total_times

# This function was used to test experiment 3
def testing_function2(n, k, functions):
    total_times = []
    for _ in range(len(functions)):
        total_times.append([])

    max_swaps = int(n*math.log(n, 2)/2)

    for i in range(max_swaps):
        L = bad_sorts.create_near_sorted_list(n, k, i)

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

# This function was used to test experiment 5
def testing_function3(n, k, functions):
    total_times = []
    for _ in range(len(functions)):
        total_times.append([])

    for i in range(n):
        L = bad_sorts.create_near_sorted_list(n, k, i)

        for j in range(len(functions)):
            average = 0

            for _ in range(200):
                L_copy = L.copy()
                start = timeit.default_timer()
                functions[j].f(L_copy)
                end = timeit.default_timer()
                average += (end-start)

            average /= 200
            total_times[j].append(average)

    return total_times

# Plots on same graph, with x-axis of list length, used for
# experiments 1, 2, 4, 6, 7, and 8
def multi_graph(times, functions):
    for i in range(len(functions)):
        plot.plot(times[i], label=functions[i].name)
    plot.legend()
    plot.title("Sorting Algorithms: List Length vs. Time")
    plot.xlabel("List Length")
    plot.ylabel("Time (sec)")
    plot.show()


# Plots on same graph, with x-axis of list sortedness, used for
# experiments 3 and 5.
def swaps_graph(times, functions):
    for i in range(len(functions)):
        plot.plot(times[i], label=functions[i].name)
    plot.legend()
    plot.title("Sorting Algorithms: Number of Swaps (sortedness) vs. Time")
    plot.xlabel("Number of Swaps")
    plot.ylabel("Time (sec)")
    plot.show()

"""
Below is the code we ran for testing each experiment, we commented
out the lines used to test the code for each experiment (the total_times_exp#
and the graphing function that was used). To test these experiments, simply
uncomment the correct testing function. Note that the test functions for experiment
2 are split into two parts, one to test bubble sort and one to test selection sort
"""
functions_exp1 = [function_info.FunctionInfo(bad_sorts.selection_sort, "Selection Sort"),
                  function_info.FunctionInfo(bad_sorts.insertion_sort, "Insertion Sort"),
                  function_info.FunctionInfo(bad_sorts.bubble_sort, "Bubble Sort")]
# total_times_exp1 = testing_function1(250, 250, functions_exp1)
# multi_graph(total_times_exp1, functions_exp1)

functions_exp2a = [function_info.FunctionInfo(bad_sorts.bubble_sort, "Bubble Sort"),
                   function_info.FunctionInfo(improved_bad_sorts.bubblesort2, "Bubble Sort 2")]
# total_times_exp2a = testing_function1(250, 250, functions_exp2a)
# multi_graph(total_times_exp2a, functions_exp2a)

functions_exp2b = [function_info.FunctionInfo(bad_sorts.selection_sort, "Selection Sort"),
                   function_info.FunctionInfo(improved_bad_sorts.selection_sort2, "Selection Sort 2")]
# total_times_exp2b = testing_function1(250, 250, functions_exp2b)
# multi_graph(total_times_exp2b, functions_exp2b)

functions_exp3 = [function_info.FunctionInfo(bad_sorts.insertion_sort, "Insertion Sort"),
                  function_info.FunctionInfo(bad_sorts.bubble_sort, "Bubble Sort"),
                  function_info.FunctionInfo(bad_sorts.selection_sort, "Selection Sort")]
#total_times_exp3 = testing_function2(500, 500, functions_exp3)
#swaps_graph(total_times_exp3, functions_exp3)

functions_exp4 = [function_info.FunctionInfo(good_sorts.quicksort, "Quick Sort"),
                  function_info.FunctionInfo(good_sorts.mergesort, "Merge Sort"),
                  function_info.FunctionInfo(good_sorts.heapsort, "Heap Sort")]
#total_times_exp4 = testing_function1(250, 250, functions_exp3)
#multi_graph(total_times_exp4, functions_exp4)

functions_exp5 = [function_info.FunctionInfo(good_sorts.quicksort, "Quick Sort"),
                  function_info.FunctionInfo(good_sorts.mergesort, "Merge Sort"),
                  function_info.FunctionInfo(good_sorts.heapsort, "Heap Sort")]
#total_times_exp5 = testing_function3(100, 100, functions_exp5)
#swaps_graph(total_times_exp5, functions_exp5)

functions_exp6 = [function_info.FunctionInfo(good_sorts.quicksort, "Quicksort"),
                  function_info.FunctionInfo(double_quicksort.dual_quicksort, "Dual Pivot Quicksort")]
# total_times_exp6 = testing_function1(250, 250, functions_exp6)
# multi_graph(total_times_exp6, functions_exp6)

functions_exp7 = [function_info.FunctionInfo(good_sorts.mergesort, "Mergesort"),
                  function_info.FunctionInfo(iterative_mergesort.bottom_up_mergesort, "Bottom-up Mergesort")]
# total_times_exp7 = testing_function1(1000, 1000, functions_exp7)
# multi_graph(total_times_exp7, functions_exp7)

functions_exp8 = [function_info.FunctionInfo(good_sorts.mergesort, "Mergesort"),
                  function_info.FunctionInfo(good_sorts.quicksort, "Quicksort"),
                  function_info.FunctionInfo(bad_sorts.insertion_sort, "Insertion Sort")]
total_times_exp8 = testing_function1(35, 35, functions_exp8)
multi_graph(total_times_exp8, functions_exp8)