'''
Write a Python program to compute following operations on String: 

a) To display word with the longest length 

b) To determines the frequency of occurrence of particular character in the string 

c) To check whether given string is palindrome or not 

d) To display index of first appearance of the substring 

e) To count the occurrences of each word in a given string 

'''


print("Basic Matrix Operation using Python")
m1 = []
m = []
m2 = []
res = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]

print("Welcome all in assignment no.03 from Group A")
print("For Matrix operation we require some input fron you. ")
row1 = int(input("Enter no. of rows in first matrix: "))
col1 = int(input("Enter no. of columns in first matrix: "))
row2 = int(input("Enter no. of rows in second matrix: "))
col2 = int(input("Enter no. of columns in second matrix: "))

def main():
    print('''
1. Accept two matrics from user: 
2. Show the Matrics avalues: 
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
        main()
    elif ch == 2:
        print("The value of first matrix is as follows: ")
        show(m1, row1, col1)
        print("The values of second matrix is as follows: ")
        show(m2, row2, col2)
        main()
    elif ch == 3:
        print("The adding of two matrix are as follows: ")
        if((row1 == row2) and (col1 == col2)):
            addMatrix(m1, m2, row1, col1)
            show(res, row1, col1)
        else:
            print("Sorry!! Adding is not possible...")
        main()
    elif ch == 4:
        print("The subtraction of two matrix are as follows: ")
        if((row1 == row2) and (col1 == col2)):
            subtractMatrix(m1, m2, row1, col1)
            show(res, row1, col1)
        else:
            print("Sorry!! Subtraction is not possible...")
        main()
    elif ch == 5:
        print("The multiplication of two matrix are as follows: ")
        if((row1 == row2) and (col1 == col2)):
            multipleMatrix(m1, m2, row1, col1)
            show(res, row1, col1)
        else:
            print("Sorry!! Multiplication is not possible...")
        main()
    elif ch == 6:
        print("Before transpose of Matix the element in matrix are as follows: ")
        show(m1, row1, col1)
        print("After applying Transpose on Matrix eleements are as follows: ")
        transposeMatrix(m1, row1, col1)
        show(res, row1, col1)
        main()
    elif ch == 7:
        exit
    else:
        print("Please enter valid choice...")

def accept(m, row, col):
    for i in range(row):
        c = []
        for j in range(col):
            no = int(input("Enter the values of matrix[" + str(i) + "][" + str(j) + "]:: "))
            c.append(no)
        print("--------------------------------")
        m.append(c)

def show(m, row, col):
    for i in range(row):
        for j in range(col):
            print(m[i][j], end=' ')
        print()

def addMatrix(m1, m2, row, col):
    for i in range(row):
        for j in range(col):
            res[i][j] = m1[i][j] + m2[i][j]

def subtractMatrix(m1, m2, row, col):
    for i in range(row):
        for j in range(col):
            res[i][j] = m1[i][j] - m2[i][j]

def multipleMatrix(m1, m2, row, col):
    for i in range(row):
        for j in range(col):
            for k in range(col):
                res[i][j] = res[i][j] + m1[i][k] * m2[k][j]

def transposeMatrix(m, row, col):
    for i in range(row):
        for j in range(col):
            res[i][j] = m[j][i]

main()
