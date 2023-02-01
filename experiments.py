import math
import timeit
import bad_sorts
import improved_bad_sorts
import function_info
import matplotlib.pyplot as plot
import good_sorts
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
            test_lists.append(bad_sorts.create_random_list(i, k))
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


def graph_exp1(times, functions):
    for i in range(len(functions)):
        plot.plot(times[i])
        plot.title(f"{functions[i].name}: List Length vs. Time")
        plot.xlabel("List Length")
        plot.ylabel("Time (sec)")
        plot.show()


def graph_exp2(times, functions):
    for i in range(len(functions)):
        plot.plot(times[i], label=functions[i].name)
    plot.legend()
    plot.title("Sorting Algorithms: List Length vs. Time")
    plot.xlabel("List Length")
    plot.ylabel("Time (sec)")
    plot.show()


def graph_exp3(times, functions):
    for i in range(len(functions)):
        plot.plot(times[i], label=functions[i].name)
    plot.legend()
    plot.title("Sorting Algorithms: Number of Swaps (sortedness) vs. Time")
    plot.xlabel("Number of Swaps")
    plot.ylabel("Time (sec)")
    plot.show()


functions_exp1 = [function_info.FunctionInfo(bad_sorts.selection_sort, "Selection Sort"),
                  function_info.FunctionInfo(bad_sorts.insertion_sort, "Insertion Sort"),
                  function_info.FunctionInfo(bad_sorts.bubble_sort, "Bubble Sort")]
total_times_exp1 = experiment1(100, 100, functions_exp1)
graph_exp1(total_times_exp1, functions_exp1)


functions_exp2 = [function_info.FunctionInfo(bad_sorts.insertion_sort, "Insertion Sort"),
                  function_info.FunctionInfo(bad_sorts.insertion_sort2, "Insertion Sort 2"),
                  function_info.FunctionInfo(bad_sorts.bubble_sort, "Bubble Sort"),
                  function_info.FunctionInfo(improved_bad_sorts.bubblesort2, "Bubble Sort 2"),
                  function_info.FunctionInfo(bad_sorts.selection_sort, "Selection Sort"),
                  function_info.FunctionInfo(improved_bad_sorts.selection_sort2, "Selection Sort 2")]
total_times_exp2 = experiment1(100, 100, functions_exp2)
graph_exp2(total_times_exp2, functions_exp2)

functions_exp3 = [function_info.FunctionInfo(bad_sorts.insertion_sort, "Insertion Sort"),
                  function_info.FunctionInfo(bad_sorts.bubble_sort, "Bubble Sort"),
                  function_info.FunctionInfo(bad_sorts.selection_sort, "Selection Sort")]
total_times_exp3 = experiment3(500, 500, functions_exp3)
graph_exp3(total_times_exp3, functions_exp3)
