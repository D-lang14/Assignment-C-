'''
Write a pythonprogram to store first year percentage of students in array. 
Write function for sorting array of floating point numbers in ascending order using 
a) Selection Sort 
b) Bubble sort and display top five scores.
'''
# Example
# a = [5,3,1,9,8,2,4,7]


# SELECTION SORT of elements

def selectionSort(arr):
    for i in range(len(arr)):
        minIdx = i 
        for j in range(i+1, len(arr)):
            if(arr[minIdx] > arr[j]):
                minIdx = j
        arr[minIdx],arr[i] = arr[i], arr[minIdx]

    print("Marks of students after performing Selection Sort on the list : ")
    for i in range(len(marks)):
        print(marks[i])


# BUBBLE SORT of elements

def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            if(arr[j]>arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]

    print("Marks of students after performing Bubble Sort on the list :")
    for i in range(len(marks)):
        print(marks[i])


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
                
    print("Marks of students after performing Improved Bubble Sort on the list :")
    for i in range(len(marks)):
        print(marks[i])


# Displaying top five marks

def topFiveMarks(marks):
    print("Top",len(marks),"Marks are : ")
    print(*marks[::-1],"\n")


# Main

marks=[]
n = int(input("Enter number of students whose marks are to be displayed : "))
print("Enter marks for",n,"students (Press ENTER after every students marks): ")
for i in range(0, n):
    element = int(input())
    marks.append(element) 

print("The marks of",n,"students are : ")
print(marks)

flag=1;
while flag==1:
    print("\n---------------MENU---------------")
    print('''
1. Selection Sort of the marks
2. Bubble Sort of the marks
3. Improved Bubble Sort of the marks
4. Exit
    ''')

    ch=int(input("\n\nEnter your choice (from 1 to 4) : "))

    if ch==1:
        selectionSort(marks)
        a=input("\nDo you want to display top marks from the list (yes/no) : ")
        if a=='yes':
            topFiveMarks(marks)
        else:
            print("\nDone!")
            flag=0

    elif ch==2:
        bubbleSort(marks)
        a = input("\nDo you want to display top five marks from the list (yes/no) : ")
        if a == 'yes':
            topFiveMarks(marks)
        else:
            print("\nDone!")
            flag = 0

    elif ch == 3:
        improvedBubbleSort(marks)
        a = input("\nDo you want to display top five marks from the list (yes/no) : ")
        if a == 'yes':
            topFiveMarks(marks)
        else:
            print("\nDone!")
            flag = 0

    elif ch == 4:
        a=input("\nDo you want to continue (yes/no): ")
        if a=="yes":
            flag=1
        else:
            flag=0
            print("Done!")

    else:
        print("\nEnter a valid choice!!")
        a=input("\nDo you want to continue (yes/no): ")
        if a=="yes":
            flag=1
        else:
            flag=0
            print("Done!")

#<----------------------------------------END OF PROGRAM---------------------------------------->

