from array import array
import random 


def get_n_random_numbers(n = 0, min_ = -5, max_ = 5):
    numbers = []
    for i in range(n):
        numbers.append(random.randint(min_, max_))
    return numbers

def my_bubble_sort(my_list):
    n = len(my_list)
    for i in range(n - 1, -1, -1):
        for j in range(0, i):
            if not(my_list[j] < my_list[j + 1]):
                temp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp
    return my_list

def my_linear_search(my_list, item_search):
    found = (-1, -1)  #default, eğer listede yoksa
    n = len(my_list)
    for indis in range(n):
        if my_list[indis] == item_search:
            found = (my_list[indis], indis)
            break
    return found

def my_binary_search(my_list, item_search):
    found = (-1, -1, 0)
    low = 0
    high = len(my_list) - 1
    s = 0
    while low <= high:
        mid = (low + high) // 2
        print(low, high, mid)
        s += 1
        if my_list[mid] == item_search:
            return my_list[mid], mid, s
        elif my_list[mid] > item_search:
            high = mid - 1
        else:
            low = mid + 1
    print(s)
    return found

def my_experimental_study(iterNum = 5):
    cost = []
    x_low = -10
    x_high = 10
    array_size = 10
    print("array size : ", array_size)
    for iter in range(iterNum):
        my_list = get_n_random_numbers(array_size, x_low, x_high)
        my_search_item = get_n_random_numbers(1, x_low, x_high)
        my_search_item = my_search_item[0]
    
        result = my_linear_search(my_list, my_search_item)
        if(result[1] == -1):
            cost.append(array_size)
        else:
            cost.append(result[1])
        print(result)
    
    return cost

