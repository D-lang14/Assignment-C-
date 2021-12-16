'''
In second year computer engineering class, group A student’s play cricket, 
group B students play badminton and group C students play football. 
Write a Python program using functions to compute following: - 

a) List of students who play both cricket and badminton 
b) List of students who play either cricket or badminton but not both 
c) Number of students who play neither cricket nor badminton 
d) Number of students who play cricket and football but not badminton. 
(Note- While realizing the group, duplicate entries should be avoided, Do not use SET built-in functions) 

'''

# Function for removing duplicate entries from the group

def removeDuplicate(dupli):
    list = []
    for i in dupli:
        if i not in list:
            list.append(i)
        else:
            n = input('Another name instead of duplicate: ')
            list.append(n)
    return list

# Function for finding intersection between two sets (A&B)

def intersection(list1,list2):
    list3=[]
    for val in list1:
        if val in list2:
            list3.append(val)
    return list3

# Function for finding union of two sets (A|B)

def union(list1,list2):
    list3=list1.copy()
    for val in list2:
        if val not in list3:
            list3.append(val)
    return list3

# Function for finding difference between two sets (A-B)

def diff(list1,list2):
    list3=[]
    for val in list1:
        if val not in list2:
            list3.append(val)
    return list3

# Function for finding symmetric difference of two sets (A^B)

def sym_diff(list1,lst2):
    lst3=[]
    D1=diff(list1,lst2)
    print("Difference between Cricket and Badminton (C-B) is: ", D1)
    D2=diff(lst2,list1)
    print("Difference between Badminton and Cricket (B-C) is: ", D2)
    lst3=union(D1,D2)
    return lst3

# Functon for finding List of students who play both cricket and badminton

def bothCricketAndBadminton(list1,lst2):
    lst3=intersection(list1,lst2)
    print("\n\nList of students who play both cricket and badminton is: ", lst3)
    return len(lst3)

# Function for finding List of students who play either cricket or badminton but not both

def eitherCricketOrBadminton(list1,lst2):
    lst3=sym_diff(list1,lst2)
    print("\nList of students who play either cricket or badminton but not both is: ",lst3)
    return len(lst3)

# Function for finding Number of students who play neither cricket nor badminton

def neitherCricketNorBadminton(list1,lst2,lst3):
    lst4=diff(list1,union(lst2,lst3))
    print("\n\nList of students who play neither cricket nor badminton is: ",lst4)
    return len(lst4)

# Function for finding Number of students who play cricket and football but not badminton

def cricketAndFootballButNotBadminton(list1,lst2,lst3):
    lst4=diff(intersection(list1,lst2),lst3)
    print("\n\nList of students who play cricket and football but not badminton is: ",lst4)
    return len(lst4)

# Main function

# Creating an empty list for SE COMP
SEComp = []
n = int(input("\nEnter number of students in SE Computer: "))
print("Enter the names of",n,"students (Please press ENTER after entering each students name):")
for i in range(0, n):
    ele = input()
    SEComp.append(ele)  # adding the element
print("Original list of students in SE Computer: " + str(SEComp))
SEComp = removeDuplicate(SEComp)
print("The list of students after removing duplicates: " +str(SEComp))


# Creating an empty list for Cricket
Cricket = []
n = int(input("\n\nEnter number of students who play cricket: "))
print("Enter the names of",n,"students who play cricket (Please press ENTER after entering each students name): ")
for i in range(0, n):
    ele = input()
    Cricket.append(ele)  # adding the element
print("Original list of students playing cricket is: " +str(Cricket))
Cricket = removeDuplicate(Cricket)
print("The list of students playing cricket after removing duplicates: " +str(Cricket))


# Creating an empty list for Football
Football = []
n = int(input("\n\nEnter number of students who play football: "))
print("Enter the name of",n,"students who play football (Please press ENTER after entering each students name): ")
for i in range(0, n):
    ele = input()
    Football.append(ele)  # adding the element
print("Original list of students playing football: " +str(Football))
Football = removeDuplicate(Football)
print("The list of students playing football after removing duplicates: " +str(Football))


# Creating an empty list for Badminton
Badminton = []
n = int(input("\n\nEnter number of students who play badminton: "))
print("Enter the name of",n,"students who play badminton (Please press ENTER after entering each students name): ")
for i in range(0, n):
    ele = input()
    Badminton.append(ele)  # adding the element
print("Original list of students playing badminton: " +str(Badminton))
Badminton = removeDuplicate(Badminton)
print("The list of students playing badminton after removing duplicates: " +str(Badminton))


# Menu Driven Program
flag=1
while flag==1:
    print("\n\n--------------------MENU--------------------\n")
    print("1. List of students who play both cricket and badminton")
    print("2. List of students who play either cricket or badminton but not both")
    print("3. List of students who play neither cricket nor badminton")
    print("4. Number of students who play cricket and football but not badminton")
    print("5. Exit\n")
    ch=int(input("Enter your Choice (from 1 to 5): "))

    if ch==1:
        print("Number of students who play both cricket and badminton: ", bothCricketAndBadminton(Cricket,Badminton))
        a = input("\n\nDo you want to continue (yes/no): ")
        if a == "yes":
            flag = 1
        else:
            flag = 0
            print("Done!")

    elif ch==2:
        print("Number of students who play either cricket or badminton but not both: ", eitherCricketOrBadminton(Cricket, Badminton))
        a = input("\n\nDo you want to continue (yes/no): ")
        if a == "yes":
            flag = 1
        else:
            flag = 0
            print("Done!")

    elif ch==3:
        print("Number of students who play neither cricket nor badminton: ", neitherCricketNorBadminton(SEComp,Cricket,Badminton))
        a = input("\n\nDo you want to continue (yes/no): ")
        if a == "yes":
            flag = 1
        else:
            flag = 0
            print("Done!")

    elif ch==4:
        print("Number of students who play cricket and football but not badminton: ", cricketAndFootballButNotBadminton(Cricket,Football,Badminton))
        a = input("\n\nDo you want to continue (yes/no): ")
        if a == "yes":
            flag = 1
        else:
            flag = 0
            print("Done!")

    elif ch==5:
        flag=0
        print("Done!")

    else:
        print("!!Wrong Choice!! ")
        a=input("\n\nDo you want to continue (yes/no): ")
        if a=="yes":
            flag=1
        else:
            flag=0
            print("Done!")

#<---------------------------------------------END OF PROGRAM--------------------------------------->

