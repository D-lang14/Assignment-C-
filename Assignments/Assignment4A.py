''' 
Write a python program to store roll numbers of student in array 
who attended training program in random order.
Write a function for searching whether 
particular student attended training program or not,
USING LINEAR SEARCH AND SENTINEL SEARCH.
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

match = int(input("\nEnter the roll_number which you wnat to find: "))


# LINEAR SEARCH 

def linearSearch(arr):
    n = len(arr)
    for i in range(n):
        if(arr[i] == match):
            print(arr[i])
        else:
            continue;

linearSearch(a)



