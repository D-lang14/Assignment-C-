'''
Write a python program to store first year percentage of students in array. 
Write function for sorting array of floating point numbers in ascending order using quick sort and display top five scores.
'''


# Accepting the percentage of the Students

def acceptPercentage():
    percentage = [];
    numberOfStudents = int(input("Enter the number of Student: "))
    for i in range(numberOfStudents):
        percentage.append(float(input("Enter the Percentage(float) of Students[{0}]: ".format(i + 1))))
    return percentage


# Displaying the percentage of the Students

def displayPercentage(percentage):
    for i in range(len(percentage)):
        print(percentage[i],end=" ")


# Performing partition of the Data

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


# Performing Quick Sort on the Data

def quickSort(arr, left, right):
    while left < right :
        p = partition(left, right, arr)
        quickSort(arr, left, p-1)
        quickSort(arr, p+1, right)
        return arr
    
# Displaying Top Five Percentages of Students

def displayTopFive(percentage):
    print("Top Five Percentages are : ")
    if len(percentage) < 5:
        start, stop = len(percentage) - 1, -1
    else:
        start, stop = len(percentage) - 1, len(percentage) - 6

    for i in range(start, stop, -1):
        print(percentage[i],"\n")


# Main 

unsortedPercentage = []
sortedPercentage = []
flag = 1

while flag == 1:
    print("\n--------------------MENU--------------------")
    print('''
1. Accept the Percentage of Students
2. Display the Percentages of Students
3. Perform Quick Sort on the Data
4. Exit
    ''')

    ch = int(input("Enter your choice (from 1 to 4) : "))

    if ch == 1:
        unsortedPercentage = acceptPercentage()

    elif ch == 2:
        displayPercentage(unsortedPercentage)

    elif ch == 3:
        print("Percentages of Students after performing Quick Sort : ")
        sortedPercentage = quickSort(unsortedPercentage,0,len(unsortedPercentage)-1)
        displayPercentage(sortedPercentage)

        a = input("Do you want to display the Top 5 Percentages of Students (yes/no) : ")
        if a == 'yes':
            displayTopFive(sortedPercentage)

    elif ch == 4:
        a=input("\n\nDo you want to continue (yes/no): ")
        if a=="yes":
            flag=1
        else:
            flag=0
            print("Done!")

    else:
        print("Invalid Choice!!")
        a=input("\n\nDo you want to continue (yes/no): ")
        if a=="yes":
            flag=1
        else:
            flag=0
            print("Done!")


#<------------------------------------END OF PROGRAM------------------------------------>

