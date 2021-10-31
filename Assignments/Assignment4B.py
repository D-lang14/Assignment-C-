''' 
Write a python program to store roll numbers of student in array 
who attended training program in random order.
Write a function for searching whether 
particular student attended training program or not,
USING BINARY SEARCH AND FIBONACCI SEARCH
'''


# Accepting the Roll Numbers of the Students

def acceptRollNo():
    rollNum = [];
    numberOfStudents = int(input("Enter the number of Student: "))
    for i in range(numberOfStudents):
        rollNum.append(int(input("Enter the Roll Number of Students[{0}]: ".format(i + 1))))
    return rollNum


# Displaying the Roll Numbers of the Students

def displayRollNo(rollNum):
    for i in range(len(rollNum)):
        print(rollNum[i],end=" ")


# Bubble Sort for sorting the list of Roll Numbers

def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if(arr[j]>arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]

    for i in range(len(arr)):
        print(arr[i])


# BINARY SEARCH for searching Roll Numbers

def binarySearch(arr, low, high, match):

    while(high >= low):
        
        mid = low + (high - 1) // 2

        if(arr[mid] == match):
            return mid 
        elif arr[mid] < match:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1
    

# Main

unsort_Roll = []
flag = 1

while flag == 1:
        print("\n---------------------MENU---------------------")
        print('''
1. Accept Student Roll Numbers
2. Display the Roll Numbers of Student
3. Sort Roll Numbers from the list
4. Searching Binary Search from the list
5. Exit\n
        ''')

        ch = int(input("Enter your choice (from 1 to 5) : "))

        if ch == 1:
            unsort_Roll = acceptRollNo()

        elif ch == 2:
            print("\nThese are the student roll numbers who have attended the training session: ")
            displayRollNo(unsort_Roll)

        elif ch == 3:
            print("Elements after performing Bubble Sort : ")
            bubbleSort(unsort_Roll)
        
        elif ch == 4:
            match = int(input("\nEnter the Roll_number which you want to find: "))
            result = binarySearch(unsort_Roll, 0, len(unsort_Roll)-1, match)
            # if(result == -1):
            #     print("Roll number not found")
            # else:
            #     print("Roll number found at location: "+ str(unsort_Roll.index(match)))

            if result != -1:
                 print("The Roll Number",match,"is found at position",result+1)
            else:
                 print("Roll Number",match,"not found!!")

        elif ch == 5:
            a=input("\nDo you want to continue (yes/no): ")
            if a=="yes":
                flag=1
            else:
                flag=0
                print("Done!")
        
        else:
            print("Please enter valid choice...")
            a=input("\nDo you want to continue (yes/no): ")
            if a=="yes":
                flag=1
            else:
                flag=0
                print("Done!")

#<-------------------------------------END OF PROGRAM------------------------------------->





    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   
# Fibonacci Search

# def fib(n):
#     if(n == 0): 
#         return 0
#     if(n == 1):
#         return 1
#     return (fib(n-1) + fib(n-2))

# k = 1
# for k in range(n):
#     p = fib(k-2)
#     q = fib(k-3)
#     mid = n - p + 1
#     k = k + 1
    
# def fibonacci(arr, match, mid, p , q):
#     if(match == arr[mid-1]):
#         return mid
#     if(match > arr[mid-1]):
#         if(p == 1):
#             return -1
#         else:
#             mid = mid + q
#             p = p - q
#             q = q - p 
#         return fibonacci(a, match, mid, p, q)
#     else:
#         if(q == 0):
#             return -1
#         else:
#             mid = mid - q
#             temp = p - q
#             p = q
#             q = temp
#         return fibonacci(a, match, mid, p, q)

# result2 = fibonacci(a, match, mid, p, q)
# if(result2 == -1):
#     print("Roll number not found")
# else:
#     print("Roll number is found at location: ",result2)






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
