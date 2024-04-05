#!/usr/bin/python


step_count = 1

# dump single sorting state to a file
# indexes is a list of indexes affected in given state
# array is array content at this step
def dump_state(indexes, array):
    global step_count
    steps_file.write(",".join([str(el) for el in indexes]) +"\n")
    for number in array:
        steps_file.write(str(number) +"\n")
    steps_file.write("---\n")
    step_count += 1
    f.close()

def bubble_sort(array):
    n = len(array)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if array[j] > array[j+1] :
                array[j], array[j+1] = array[j+1], array[j]
                dump_state([j, j+1], array)
    return array


def insertion_sort(array):
    l = len(array)
    for i in range(1, l):
        val = array[i]
        j = i
        dump_state([j], array)
        while j > 0 and array[j-1] > val:
            array[j] = array[j-1]
            dump_state([j], array)
            j -= 1
        array[j] = val
    return array

tested_sorting = insertion_sort

#load array from file
f = open("numbers.txt","r")
steps_file = open("steps.txt", "w")
input_array = []
for line in f:
    line = line.rstrip()
    if line:
        input_array.append(int(line))

f.close()


print(input_array)
print(tested_sorting(input_array))

steps_file.close()
