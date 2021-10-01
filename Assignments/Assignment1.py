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
# Done by SCOC12 Disha Patil

totalStudents = int(input("Enter total number of students in a class: "))

classSectionC = input('Enter list of roll numbers: ')
# user_list = classSectionC.split()
# print('list: ', user_list)

cricket = input('Enter list of Group A who play only cricket: ')
# user_list = cricket.split()
# print('Cricket: ', user_list)

badminton = input('Enter list of Group B who play only badminton: ')
# user_list = badminton.split()
# print('Badminton: ', user_list)

football = input('Enter list of Group C who play only football: ')
# user_list = football.split()
# print('Football: ', user_list)

common = []
onlyCricket = []
onlyBadminton = []
onlyFootball = []
cricketBadminton = []
cricketFootball = []
neitherCricketNorBadminton = []
cricketFootballNotBadminton = []


# List of students who play both cricket and badminton 
def playBothCricketAndBadminton():
    for num1 in cricket:
        for num2 in badminton:
            if (num1 == num2):
                common.append(num1)
    print("List of students who play both cricket and badminton:", common)


# List of students who play either cricket or badminton but not both 
def eitherCricketOrBadmintonNotBoth():
    for i in cricket:
        flag = 0
        for j in badminton:
            if i == j:
                flag = 1
        if flag == 0:
            onlyCricket.append(i)
            
    print("List of students who play only cricket:", onlyCricket)

    for k in badminton:
        flan = 0
        for l in cricket:
            if k == l:
                flan = 1
        if flan == 0:
            onlyBadminton.append(k)
    
    print("List of students who play only badminton:", onlyBadminton)

# Number of students who play neither cricket nor badminton 
def neitherCricketnorBadminton():
    for i in cricket:
        cricketBadminton.append(i)
        for j in badminton:
            flag = 0
            for k in cricketBadminton:
                if j == k:
                    flag = 1
            if flag == 0:
                cricketBadminton.append(j)
    print("Number of students who play both cricket and badminton:", cricketBadminton)
    for num in classSectionC:
        flan = 0
        for no in cricketBadminton:
            if no == num:
                flan = 1
        if flan == 0:
            neitherCricketNorBadminton.append(num)
    print("Number of students who play neither cricket nor badminton:", neitherCricketNorBadminton)

# Number of students who play cricket and football but not badminton
def cricketFootballnotBadminton():
    for i in cricket:
        cricketFootball.append(i)
        for j in football:
            flag = 0
            for k in cricketFootball:
                if j == k:
                    flag = 1
            if flag == 0:
                cricketFootball.append(j)
    print("Number of students who play both cricket and Football:", cricketFootball)
    for m in cricketFootball:
        flan = 0
        for n in badminton:
            if (m == n):
                flan = 1
        if (flan == 0):
            cricketFootballNotBadminton.append(m)
    print("Number of students who play cricket and football but not badminton:", cricketFootballNotBadminton)

def mainMenu():
    print('''
1. List of students who play both cricket and badminton 
2. List of students who play either cricket or badminton but not both 
3. Number of students who play neither cricket nor badminton 
4. Number of students who play cricket and football but not badminton
    ''')
    ans = 'Y'
    while ans == 'Y':
        choice = int(input("Enter your choice: "))
        if choice == 1:
            playBothCricketAndBadminton()
            print()
            ans = input("Do you want to continue? (Y or N): ")

        elif choice == 2:
            eitherCricketOrBadmintonNotBoth()
            print()
            ans = input("Do you want to continue? (Y or N): ")

        elif choice == 3:
            neitherCricketnorBadminton()
            print()
            ans = input("Do you want to continue? (Y or N): ")

        elif choice == 4:
            cricketFootballnotBadminton()
            print()
            ans = input("Do you want to continue? (Y or N): ")

        else:
            print("Enter valid choice")
            ans = input("Do you want to continue? (Y or N): ")

mainMenu()


