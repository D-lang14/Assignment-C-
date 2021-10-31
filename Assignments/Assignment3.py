'''
Write a python program to compute following computation on matrix:
A) Addition of two matrices
B) Subtration of two matrices
C) Multiplication of two matrices
D) Transpose of matrix

'''


# Accepting matrix elements

def accept(m, row, col):
    for i in range(row):
        c = []
        for j in range(col):
            no = int(input("Enter the values of matrix[" + str(i) + "][" + str(j) + "]:: "))
            c.append(no)
        print("--------------------------------")
        m.append(c)


# Displaying matrix elements

def show(m, row, col):
    for i in range(row):
        for j in range(col):
            print(m[i][j], end=' ')
        print()


# Adding the elements of matrix

def addMatrix(m1, m2, row, col):
    for i in range(row):
        for j in range(col):
            res[i][j] = m1[i][j] + m2[i][j]


# Subtracting the elements of matrix

def subtractMatrix(m1, m2, row, col):
    for i in range(row):
        for j in range(col):
            res[i][j] = m1[i][j] - m2[i][j]


# Multiplying the elements of matrix

def multipleMatrix(m1, m2, row, col):
    for i in range(row):
        for j in range(col):
            for k in range(col):
                res[i][j] = res[i][j] + m1[i][k] * m2[k][j]


# Transpose of a matrix

def transposeMatrix(m, row, col):
    for i in range(row):
        for j in range(col):
            res[i][j] = m[j][i]


# Main 

m1 = []
m = []
m2 = []
res = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]


print("For Matrix operation we require some inputs from you. ")
row1 = int(input("Enter no. of Rows in First Matrix: "))
col1 = int(input("Enter no. of Columns in First Matrix: "))
row2 = int(input("Enter no. of Rows in Second Matrix: "))
col2 = int(input("Enter no. of Columns in Second Matrix: "))


flag = 1

while flag == 1:
    print("\n\n--------------------MENU--------------------\n")
    print('''
1. Accept two Matrices from user: 
2. Show the Matrices values: 
3. Addition of two Matrices: 
4. Subtraction of two Matrices: 
5. Multiplication of two Matrices: 
6. Transpose of a Matrix: 
7. Exit    
    ''')

    ch = int(input("Enter your choice: "))
    if ch == 1:
        print("Enter the values for First Matrix: ")
        accept(m1, row1, col1)
        print("Enter the values for Second Matrix: ")
        accept(m2, row2, col2)
        a=input("\n\nDo you want to continue (yes/no): ")
        if a=="yes":
            flag=1
        else:
            flag=0
            print("Done!")

    elif ch == 2:
        print("The value of First Matrix is as follows: ")
        show(m1, row1, col1)
        print("The values of Second Matrix is as follows: ")
        show(m2, row2, col2)
        a=input("\n\nDo you want to continue (yes/no): ")
        if a=="yes":
            flag=1
        else:
            flag=0
            print("Done!")

    elif ch == 3:
        print("The Addition of two Matrix are as follows: ")
        if((row1 == row2) and (col1 == col2)):
            addMatrix(m1, m2, row1, col1)
            show(res, row1, col1)
        else:
            print("Sorry!! Adding is not possible...")
        a=input("\n\nDo you want to continue (yes/no): ")
        if a=="yes":
            flag=1
        else:
            flag=0
            print("Done!")

    elif ch == 4:
        print("The Subtraction of two Matrix are as follows: ")
        if((row1 == row2) and (col1 == col2)):
            subtractMatrix(m1, m2, row1, col1)
            show(res, row1, col1)
        else:
            print("Sorry!! Subtraction is not possible...")
        a=input("\n\nDo you want to continue (yes/no): ")
        if a=="yes":
            flag=1
        else:
            flag=0
            print("Done!")

    elif ch == 5:
        print("The Multiplication of two Matrix are as follows: ")
        if((row1 == row2) and (col1 == col2)):
            multipleMatrix(m1, m2, row1, col1)
            show(res, row1, col1)
        else:
            print("Sorry!! Multiplication is not possible...")
        a=input("\n\nDo you want to continue (yes/no): ")
        if a=="yes":
            flag=1
        else:
            flag=0
            print("Done!")

    elif ch == 6:
        print("Before transpose of Matrix the elements are as follows: ")
        show(m1, row1, col1)
        print("After applying Transpose on Matrix elements are as follows: ")
        transposeMatrix(m1, row1, col1)
        show(res, row1, col1)
        a=input("\n\nDo you want to continue (yes/no): ")
        if a=="yes":
            flag=1
        else:
            flag=0
            print("Done!")

    elif ch == 7:
        print("Done!")
        flag = 0
        
    else:
        print("Please enter valid choice...")
        a=input("\n\nDo you want to continue (yes/no): ")
        if a=="yes":
            flag=1
        else:
            flag=0
            print("Done!")

#<-------------------------------------END OF PROGRAM------------------------------------->

