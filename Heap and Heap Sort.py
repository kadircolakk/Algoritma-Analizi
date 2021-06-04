def min_heapify(array, i):
    left = 2*i + 1
    right = 2*i + 2
    length = len(array) - 1
    smallest = i
    if left <= length and array[i] > array[left]:
        smallest = left
    if right <= length and array[smallest] >array[right]:
        smallest = right
    if smallest != i:
        array[i], array[smallest] = array[smallest], array[i]
        min_heapify(array, smallest)

def build_min_heap(array):
    for i in reversed(range(len(array)//2)):
        min_heapify(array, i)

def insertItemToHeap(my_heap, item):
    my_heap.append(item)
    n = len(my_heap)
    if(n//2 == n/2):
        parent_indis = (n//2) - 1
    else:
        parent_indis = (n//2)
    
    while parent_indis >= 1:
        min_heapify(my_heap, parent_indis - 1)
        parent_indis = parent_indis // 2


def removeItemFromHeap(my_heap):
    my_heap[0], my_heap[-1] = my_heap[-1], my_heap[0]
    s = my_heap.pop()
    min_heapify(my_heap, 0)
    return my_heap

my_array_1 = [8,10,3,4,7,15,1,2,16]

build_min_heap(my_array_1)

print(my_array_1)
