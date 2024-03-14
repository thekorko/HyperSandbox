import random
import time
#binary search algorithm

#We will prove that binary search is faster than naive_search

#naive search: scan entire list and ask if its equal to the target
# if yes, return the index
# if no, then return -1
def naive_search(list, target):
    #example list = [1, 3, 10, 12]
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1

#binary search uses divide and conquer
#we will leverage the fact that our list is sorted
def binary_search(lista, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(lista) - 1
    #it's not in the list
    if high < low:
        return -1
    #example list = [1, 3, 5, 10, 12]
    midpoint = (low + high) // 2 #2
    if lista[midpoint] == target:
        return midpoint
    elif target < lista[midpoint]:
        return binary_search(lista, target, low, midpoint-1)
    else:
        # target > list[midpoint]
        return binary_search(lista, target, midpoint+1, high)
    
if __name__=='__main__':
    lista = [1, 3, 5, 10, 12]
    target = 10
    print(naive_search(lista, target))
    print(binary_search(lista, target))

    lenght = 10000
    #build a sorted list of lenght 10000
    sorted_list = set()
    while len(sorted_list) < lenght:
        sorted_list.add(random.randint(-3*lenght, 3*lenght))
    sorted_list = sorted(list(sorted_list))

    #testing naive_search 0.0005579293966293335 seconds
    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive search time: ", (end - start)/lenght, "seconds")

    #testing binary search 1.1598229408264161e-05 seconds
    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search time: ", (end - start)/lenght, "seconds")
    