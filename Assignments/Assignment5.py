'''
Write a pythonprogram to store first year percentage of students in array. 
Write function for sorting array of floating point numbers in ascending order using 
a) Selection Sort 
b) Bubble sort and display top five scores.
'''


import array as arr

def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if(arr[j]>arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]


a = arr.array('i', [])

k = int(input("Enter size of array:"))
for i in range(0, k):
    num = int(input("Enter %d array element:" % (i + 1)))
    a.append(num)

print("All array elements are:", end="")
for i in a:
    print(i, end=" ")

bubbleSort(a)   #Function calling

print("\nSorted Array")
for i in range(len(a)):
    print(a[i], end=" ")

# a = [5,3,1,9,8,2,4,7]
