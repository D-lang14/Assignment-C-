'''
Write a Python program to store marks scored in subject “Fundamental of Data Structure” 
by N students in the class. Write functions to compute following: 

a) The average score of class 

b) Highest score and lowest score of class 

c) Count of students who were absent for the test 

d) Display mark with highest frequency 

'''


# Average score of the class

def average(listofmarks):
    sum=0
    count=0
    for i in range(len(listofmarks)):
        if listofmarks[i]!=-999:
            sum+=listofmarks[i]
            count+=1
    avg=sum/count
    print("Total Marks : ", sum)
    print("Average Marks : {:0.2f}".format(avg))


# Highest score in the test for the class

def highestScore(listofmarks):
    for i in range(len(listofmarks)):
        if listofmarks[i]!=-999:
            max=listofmarks[0]
            break
    for i in range(1,len(listofmarks)):
        if listofmarks[i]>max:
            max=listofmarks[i]
    return(max)


# Lowest score in the test for the class

def lowestScore(listofmarks):
    for i in range(len(listofmarks)):
        if listofmarks[i]!=-999:
            min=listofmarks[0]
            break
    for i in range(1,len(listofmarks)):
        if listofmarks[i]<min:
            min=listofmarks[i]
    return(min)


# Counting the number of students absent for the test

def absentcount(listofmarks):
    count=0
    for i in range(len(listofmarks)):
        if listofmarks[i]==-999:
            count+=1
    return(count)


# Displaying marks with highest frequency

def maxFrequency(listofmarks):
    i=0
    Max=0
    print("Marks  |  Frequency")
    for j in listofmarks:
        if (listofmarks.index(j)==i):
            print(j,"    |  ",listofmarks.count(j))
            if listofmarks.count(j)>Max:
                Max=listofmarks.count(j)
                mark=j
        i=i+1
    return(mark,Max)


# Main 

marksinFDS=[]
numberofstudents=int(input("Enter total number of students: "))
for i in range(numberofstudents):
    marks=int(input("Enter marks of student "+str(i+1)+": "))
    marksinFDS.append(marks)

flag=1
while flag==1:
    print("\n\n--------------------MENU--------------------\n")
    print("1. Total and Average Marks of the Class")
    print("2. Highest and Lowest Marks in the Class")
    print("3. Number of Students absent for the test")
    print("4. Marks with Highest Frequency")
    print("5. Exit\n")
    ch=int(input("\nEnter your Choice (from 1 to 5): "))

    if ch==1:
        average(marksinFDS)
        a = input("\n\nDo you want to continue (yes/no): ")
        if a == "yes":
            flag = 1
        else:
            flag = 0
            print("Done!")

    elif ch==2:
        print("\nHighest Score in Class: ", highestScore(marksinFDS))
        print("Lowest Score in Class: ", lowestScore(marksinFDS))
        a = input("\n\nDo you want to continue (yes/no): ")
        if a == "yes":
            flag = 1
        else:
            flag = 0
            print("Done!")

    elif ch==3:
        print("\nNumber of Students absent in the test: ", absentcount(marksinFDS))
        a = input("\n\nDo you want to continue (yes/no): ")
        if a == "yes":
            flag = 1
        else:
            flag = 0
            print("Done!")

    elif ch==4:
        mark,fr = maxFrequency(marksinFDS)
        print("\nHighest frequency is of marks {0} that is {1} ".format(mark,fr))
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

#<-------------------------------------END OF PROGRAM------------------------------------->

