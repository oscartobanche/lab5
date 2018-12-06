#Oscar Tobanche
#Prof. Diego Aguirre
#manoj saha
#CS 2302
#this code implements a binary search tree of words.
from lab5sort import  min_heap_percolate_down, heap_sort

class MinHeap:

    def __init__(self):
        self.heap_array = []

    def percolate_up(self, node_index):
        while node_index > 0:
            # compute the parent node's index
            parent_index = (node_index - 1) // 2

            # check for a violation of the min heap property
            if self.heap_array[node_index] >= self.heap_array[parent_index]:
                # no violation, so percolate up is done.
                return
            else:
                # swap heap_array[node_index] and heap_array[parent_index]
                print(
                    "   percolate_up() swap: %d <-> %d" % (self.heap_array[parent_index], self.heap_array[node_index]))
                temp = self.heap_array[node_index]
                self.heap_array[node_index] = self.heap_array[parent_index]
                self.heap_array[parent_index] = temp

                # continue the loop from the parent node
                node_index = parent_index


    def percolate_down(self, node_index):
        child_index = 2 * node_index + 1
        value = self.heap_array[node_index]

        while child_index < len(self.heap_array):
            # Find the min among the node and all the node's children
            min_value = value
            min_index = 9999999
            i = 0
            while i < 2 and i + child_index < len(self.heap_array):
                if self.heap_array[i + child_index] < min_value:
                    min_value = self.heap_array[i + child_index]
                    min_index = i + child_index
                i = i + 1

            # check for a violation of the min heap property
            if min_value == value:
                return
            else:
                # swap heap_array[node_index] and heap_array[min_index]
                print("   percolate_down() swap: %d <-> %d" % (self.heap_array[node_index], self.heap_array[min_index]))
                temp = self.heap_array[node_index]
                self.heap_array[node_index] = self.heap_array[min_index]
                self.heap_array[min_index] = temp

                # continue loop from the min index node
                node_index = min_index
                child_index = 2 * node_index + 1
    def extract_min(self):
        if self.is_empty():
            return None
        min_elem = self.heap_array[0]
        self.heap_array[0] = self.heap_array[len(self.heap_array)]
        self.heap_array.pop(len(self.heap_array)-1)
        i = 0
        min_val = 0
        while ((2*i + 1) <= len(self.heap_array)-1):
            if ((2*i + 1) <= len(self.heap_array)-1) and self.heap_array[min_val]> self.heap_array[(2*i + 1)]:
                min_val = (2*i + 1)
            if ((2*i + 2) <= len(self.heap_array)-1) and self.heap_array[min_val]> self.heap_array[(2*i + 2)]:
                min_val = (2*i + 2)
            if min_val == i :
                return
            temp = self.heap_array[i]
            self.heap_array[i] = self.heap_array[min_val]
            self.heap_array[min_val] = temp
            i = min_val
        return min_elem
    def is_empty(self):
        return len(self.heap_array)== 0

    def insert(self, value):
        # add the new value to the end of the array.
        print("insert(%d):" % value)
        self.heap_array.append(value)

        # percolate up from the last index to restore heap property.
        self.percolate_up(len(self.heap_array) - 1)

    def remove(self):
        # save the min value from the root of the heap.
        print("remove():")
        min_value = self.heap_array[0]

        # move the last item in the array into index 0.
        replace_value = self.heap_array.pop()
        if len(self.heap_array) > 0:
            self.heap_array[0] = replace_value

            # percolate down to restore min heap property.
            self.percolate_down(0)

        # return the min value
        return min_value
# Program to test the heap class.
h = MinHeap()

input_list = [10, 2, 5, 18, 22]
print(heap_sort(input_list))
for item in input_list:
    h.insert(item)
    print('   --> array: %s\n' % h.heap_array)
while len(h.heap_array) > 0:
    removed_value = h.remove()
    print('   --> removed %d, array: %s\n' % (removed_value, h.heap_array))
print()
