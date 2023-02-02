def merge(L, section_start, merge_size):
    if section_start + merge_size // 2 > len(L):
        return

    left = L[section_start:section_start + merge_size // 2]
    if section_start + merge_size >= len(L):
        right = L[section_start + merge_size // 2:]
    else:
        right = L[section_start + merge_size // 2:section_start + merge_size]
    r_i = l_i = L_i = 0
    merge_size = len(left) + len(right)

    while L_i < merge_size:
        if r_i >= len(right):
            L[section_start + L_i] = left[l_i]
            l_i += 1
        elif l_i >= len(left):
            L[section_start + L_i] = right[r_i]
            r_i += 1
        else:
            if left[l_i] < right[r_i]:
                L[section_start + L_i] = left[l_i]
                l_i += 1
            else:
                L[section_start + L_i] = right[r_i]
                r_i += 1
        L_i += 1


def bottom_up_mergesort(L):
    merge_size = 2
    while merge_size < len(L)*2:
        # Split L into chunks of merge_size, merge halves of chunks together
        section_start = 0
        while section_start < len(L):
            merge(L, section_start, merge_size)
            section_start += merge_size

        merge_size *= 2


# def perm(L1, L2):
#     for x in L1:
#         if L1.count(x) != L2.count(x):
#             return False
#     return True
#
#
# def is_sorted(L):
#     for i, j in zip(range(0, len(L) - 1), range(1, len(L))):
#         if j < i:
#             return False
#     return True
#
#
# Ls = [[], [1], [1, 2], [2, 1], [1, 2, 3], [3, 2, 1], [4, 76, 3, 23, 36, 7, 2, 1, 4, 7, 4, 13, 4, 67, 6]]
# for L in Ls:
#     print(L)
#     L2 = L.copy()
#     bottom_up_mergesort(L2)
#     print(L2)
#     print(f"Sorted? {is_sorted(L2)}")
#     print(f"Permutation? {perm(L, L2)}\n")