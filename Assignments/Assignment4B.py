''' 
Write a python program to store roll numbers of student in array 
who attended training program in random order.
Write a function for searching whether 
particular student attended training program or not,
USING BINARY SEARCH AND FIBONACCI SEARCH
'''


import array as arr

a = arr.array('i', [])

n = int(input("Enter total number of roll_numbers registered are: "))
for i in range(0, n):
    num = int(input("Enter roll_number seqence %d : " % (i + 1)))
    a.append(num)

print("All roll_numbers are: ", end="")
for i in a:
    print(i, end=" ")

def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if(arr[j]>arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
bubbleSort(a)

print("\nSorted Array")
for i in range(len(a)):
    print(a[i], end=" ")

match = int(input("\nEnter the roll_number which you wnat to find: "))


# BINARY SEARCH

def binarySearch(arr, low, high, match):
    if(high >= low):
        
        mid = int((high + low) / 2)

        if(arr[mid] == match):
            return(mid)
        elif arr[mid] > match:
            return binarySearch(arr, mid + 1, high, match)
        else:
            return binarySearch(arr, low, mid - 1, match) 
    else:
        return(-1)
    
result = binarySearch(a, 0, len(a)-1, match)
if(result == -1):
    print("Element not found")
else:
    print("Element is found at location: ", result+1)





    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



# Binary Search 
# first give first element as low, last element as high and find mid
# 1.	Compare x with the middle element.
# 2.	If x matches with the middle element, we return the mid index
# 3.	Else If x is greater than the mid element, then x can only lie in the right half sub array after the mid element. So we recur for the right half.
# 4.	Else (x is smaller) recur for the left half.
# 2, 5, 8, 12, 16, 23, 38, 56, 72, 91  
# X= 23
# mid = 0 + 9 /2 
# 4
# mid= 16
# X= 23
# 23, 38, 56, 72, 91
# low = 23
# high = 91
# mid = (low + high) / 2
# mid = 56
# mid = a[2]
# x = 23
# 23, 38
# low = 23
# high = 38
# mid = 23
# x = 23
# Result = 23
# O(log n) -- Best
# O(n)     -- Worst

# Linear Search
# O(1) -- Best
# O(n) -- Worst

# Sentinal Search
# Fiboonnic Search
