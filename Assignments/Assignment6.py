'''
Write a python program to store first year percentage of students in array. 
Write function for sorting array of floating point numbers in ascending order using quick sort and display top five scores.
'''

import array as arr

a = arr.array('f', [])

k = int(input("Enter the number of Students: "))
for i in range(0, k):
    a.append(float(input("Enter the First Year % of Student[{0}] : ".format(i))))


def partition(left, right, arr):
    index = left
    pivot = arr[index]

    while(left < right):
        while(left < len(arr) and arr[left] <= pivot):
            left += 1
        while(pivot < arr[right]):
            right -= 1

        if(left < right):
            arr[left], arr[right] = arr[right], arr[left]

    arr[right], arr[index] = arr[index], arr[right]
    return right


def quickSort(left, right, arr):
    if(left < right):
        p = partition(left, right, arr)

        quickSort(left, p-1, arr)
        quickSort(p+1, right, arr)


quickSort(0, len(a)-1, a)


print("\nSorted Marks List")
for i in range(0, len(a)):
    print("{0:.2f}\t".format(a[i]), end=" ")
print()
