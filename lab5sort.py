#Oscar Tobanche
#Prof. Diego Aguirre
#manoj saha
#CS 2302
#this code implements a binary search tree of words.
def min_heap_percolate_down(node_index, heap_list, list_size):
    child_index = 2 * node_index + 1
    value = heap_list[node_index]

    while child_index < list_size:
        # Find the min among the node and all the node's children
        min_value = value
        min_index = -1
        i = 0
        while i < 2 and i + child_index <\
                list_size:
            if heap_list[i + child_index] > min_value:
                min_value = heap_list[i + child_index]
                min_index = i + child_index
            i = i + 1

        if min_value == value:
            return

        # Swap heap_list[node_index] and heap_list[min_index]
        temp = heap_list[node_index]
        heap_list[node_index] = heap_list[min_index]
        heap_list[min_index] = temp

        node_index = min_index
        child_index = 2 * node_index + 1


# Sorts the list of numbers using the heap sort algorithm
def heap_sort(numbers):
    # Heapify numbers list
    i = len(numbers) // 2 - 1
    while i >= 0:
        min_heap_percolate_down(i, numbers, len(numbers))
        i = i - 1

    i = len(numbers) - 1
    while i > 0:
        # Swap numbers[0] and numbers[i]
        temp = numbers[0]
        numbers[0] = numbers[i]
        numbers[i] = temp

        min_heap_percolate_down(0, numbers, i)
        i = i - 1


# Main program to test the heap sort algorithm.
numbers = [10, 2, 5, 18, 22]
print("UNSORTED:", numbers)

heap_sort(numbers)
print("SORTED:  ", numbers)
