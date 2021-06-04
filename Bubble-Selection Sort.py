import random 

def get_n_random_numbers(n = 0, min_ = -5, max_ = 5):
    numbers = []
    for i in range(n):
        numbers.append(random.randint(min_, max_))
    return numbers

def my_bubble_sort(my_list):
    n = len(my_list)
    comp_counter = 0
    swap_counter = 0
    for i in range(n - 1, -1, -1):
        for j in range(0, i):
            comp_counter += 1
            if not(my_list[j] < my_list[j + 1]):
                temp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp
                swap_counter += 1
    return swap_counter, comp_counter

def my_selection_sort(A = [64, 25, 12, 22, 11]):
    comp_counter = 0
    swap_counter = 0
    for i in range(len(A)):
        min_idx = i
        for j in range(i + 1, len(A)):
            comp_counter += 1
            if A[min_idx] > A[j]:
                min_idx = j
                swap_counter += 1
        A[i], A[min_idx], = A[min_idx], A[i]
    return swap_counter, comp_counter

my_list_1 = get_n_random_numbers(10, -1000, 1000)

"""
print("BUBBLE SORT")
print(my_list_1)
result = my_bubble_sort(my_list_1)
print(my_list_1, result)  #dizinin sıralı hali ve swap ve comparision sayısı

print("SELECTION SORT")
print(my_list_1)
result = my_selection_sort(my_list_1)
print(my_list_1, result)
"""

def my_empiric_study_sorting(numIter = 10, array_size = 10):
    result_bubble_selection_swap_counters = []
    for i in range(numIter):
        my_list_1 = get_n_random_numbers(array_size, -1000, 1000)
        my_list_2 = get_n_random_numbers(array_size, -1000, 1000)

        result_1 = my_bubble_sort(my_list_1)
        result_2 = my_selection_sort(my_list_2)

        result_bubble_selection_swap_counters.append((result_1[0], result_2[0]))
    return result_bubble_selection_swap_counters


print(my_empiric_study_sorting(100, 100))