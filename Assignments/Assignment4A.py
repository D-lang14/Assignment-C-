''' 
Write a python program to store roll numbers of student in array 
who attended training program in random order.
Write a function for searching whether 
particular student attended training program or not,
USING LINEAR SEARCH AND SENTINEL SEARCH.
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


# LINEAR SEARCH for searching Roll Numbers of Students

def linearSearch(arr, match):
    n = len(arr)
    for i in range(n):
        if(arr[i] == match):
            return arr[i]
        else:
            continue
    return -1

# Main

unsort_Roll = []
flag = 1

while flag == 1:
        print("\n---------------------MENU---------------------")
        print('''
1. Accept Student Roll Numbers
2. Display the Roll Numbers of Student
3. Enter the Roll Number to be searched
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
            match = int(input("\nEnter the Roll_number which you want to find: "))

        elif ch == 4:
            result = linearSearch(unsort_Roll, match)
            if(result == -1):
                print("Roll number not found")
            else:
                print("Roll number found at location: "+ str(unsort_Roll.index(match)))

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

#<-------------------------------------------END OF PROGRAM------------------------------------->

