'''
Write a pythonprogram to store first year percentage of students in array. 
Write function for sorting array of floating point numbers in ascending order using 
a) Selection Sort 
b) Bubble sort and display top five scores.
'''

import array as arr

a = arr.array('f', [])

k = int(input("Enter the number of Students: "))
for i in range(0, k):
    a.append(float(input("Enter the First Year % of Student[{0}] : ".format(i))))


    
    
# BUBBLE SORT

def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if(arr[j]>arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]

bubbleSort(a)   #Function calling

print("\nSorted Marks List using Bubble Sort")
for i in range(len(a)):
    print(a[i], end=" ")


    


# IMPROVED VERSION OF BUBBLE SORT

def improvedBubbleSort(arr):
    n = len(arr)
    flag = 1
    for i in range(1, n):
        if(i < n & flag == 1):
            flag = 0
        for j in range(n-i):
            if(arr[j]>arr[j+1]):
                flag = 1
                arr[j], arr[j+1] = arr[j+1], arr[j]

improvedBubbleSort(a) 

print("\nSorted Marks List using Improved Version of Bubble Sort")
for i in range(len(a)):
    print(a[i], end=" ")


    

# SELECTION SORT

def selectionSort(arr):
    for i in range(len(arr)):
        k = i 
        for j in range(i+1, len(arr)):
            if(arr[k] > arr[j]):
                k = j
        arr[k],arr[i] = arr[i], arr[k]

selectionSort(a)

print("\nSorted Marks List using Selection Sort")
for i in range(len(a)):
    print(a[i], end=" ")


# a = [5,3,1,9,8,2,4,7]
