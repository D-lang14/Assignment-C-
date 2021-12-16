/*
In SE Computer Engineering class set A of students like vanilla ice cream and 
set B of students like Butterscotch ice cream. 
Write C++ program to store two sets using linked list. 
Compute and display: 

1. Set of students who like either vanilla or butterscotch or both 
2. Set of students who like both vanilla and butterscotch 
3. Set of students who like only vanilla but not butterscotch 
4. Set of students who like only vanilla but not butterscotch 
5. Number of students who like neither vanilla nor butterscotch 

*/

#include <iostream>
using namespace std;

// Structure Node
typedef struct node
{
	int roll;
	struct node *next;
} node;

// Create Node function which creates a single node
node *createnode()
{
	int i, n;
	node *p, *head, *t;

	head = NULL;

	// Taking input of total number of students
	cout << "\nEnter the no of students: ";
	cin >> n;
	for (i = 0; i < n; i++)
	{
		// Dynamically allocating memory
		p = new node;

		// Taking roll numbers of students as input
		cout << "\nEnter the students roll numbers: ";
		cin >> p->roll;

		p->next = NULL;

		if (head == NULL)
			head = p;
		else
		{
			t = head;
			while (t->next != NULL)
				t = t->next;
			t->next = p;
		}
	}
	return head;
}

// Display function to display linked list
void display(node *head)
{
	node *p;
	int count = 0;
	p = head;
	while (p != NULL)
	{
		cout << "\t" << p->roll << "->";
		p = p->next;
		count++;
	}
	cout << "\tNULL";
	cout << "\n\tTotal no of students: " << count << endl;
}

// Union Function
int Union(node *headv, node *headb)
{
	node *v, *b;
	int flag = 0, count = 0;
	v = headv;

	while (v != NULL)
	{
		cout << "\t" << v->roll << "->";
		v = v->next;
		count++;
	}

	for (b = headb; b != NULL; b = b->next)
	{
		flag = 0;

		for (v = headv; v != NULL; v = v->next)
		{
			if (b->roll == v->roll)
			{
				flag = 1;
				break;
			}
		}

		if (flag != 1)
		{
			cout << "\t" << b->roll << "->";
			count++;
		}
	}
	cout << "\tNULL";
	cout << "\ncount: " << count;
	return count;
}

// Intersection Function
void intersection(node *headv, node *headb)
{
	node *v, *b;
	int flag = 0;
	for (b = headb; b != NULL; b = b->next)
	{
		flag = 0;
		for (v = headv; v != NULL; v = v->next)
		{
			if (b->roll == v->roll)
			{
				flag = 1;
				break;
			}
		}
		if (flag == 1)
			cout << "\t" << b->roll << "->";
	}
	cout << "\tNULL";
}

void OnlyVanilla(node *headv, node *headb)
{
	node *v, *b;
	int flag = 0;

	for (v = headv; v != NULL; v = v->next)
	{
		flag = 0;
		for (b = headb; b != NULL; b = b->next)
		{
			if (v->roll == b->roll)
			{
				flag = 1;
				break;
			}
		}

		if (flag != 1)
		{
			cout << "\t" << v->roll << "->";
		}
	}
	cout << "\tNULL";
}

void OnlyButterscotch(node *headv, node *headb)
{
	node *v, *b;
	int flag = 0;

	for (b = headb; b != NULL; b = b->next)
	{
		flag = 0;
		for (v = headv; v != NULL; v = v->next)
		{
			if (v->roll == b->roll)
			{
				flag = 1;
				break;
			}
		}

		if (flag != 1)
		{
			cout << "\t" << b->roll << "->";
		}
	}
	cout << "\tNULL";
}

// Main Function
int main()
{
	node *headv, *headb;
	int m, count;
	headv = headb = NULL;
	cout << "\nEnter the total no of students: ";
	cin >> m;
	headv = NULL;
	int choice;
	char cont = 'y';
	while (cont == 'y')
	{
		cout << "\n-------------------Students List-------------------";
		cout << "\n\t1] Create ";
		cout << "\n\t2] Display ";
		cout << "\n\t3] Either vanilla or butterscotch or both ";
		cout << "\n\t4] Both vanilla or butterscotch";
		cout << "\n\t5] Only vanilla but not butterscotch";
		cout << "\n\t6] Only butterscotch but not vanilla";
		cout << "\n\t7] No of students who like neither vanilla nor butterscotch";
		cout << "\n\t8] Exit";
		cout << "\nEnter your choice: ";
		cin >> choice;
		switch (choice)
		{
		case 1:
			cout << "\n\tStudents who like vanilla: \n";
			headv = createnode();
			cout << "\n\tStudents who like butterscotch: \n";
			headb = createnode();

			cout << "\nDo you want to continue (y or n) ?: ";
			cin >> cont;
			if (cont == 'y')
				continue;

			break;
		case 2:
			cout << "\n-------------------Displaying Total Students------------------";
			cout << "\n\tStudents who like vanilla: \n";
			display(headv);
			cout << "\n\tStudents who like butterscotch: \n";
			display(headb);

			cout << "\nDo you want to continue (y or n) ?: ";
			cin >> cont;
			if (cont == 'y')
				continue;

			break;
		case 3:
			cout << "\n\tStudents who like either vanilla or butterscotch: \n";
			count = Union(headv, headb);

			cout << "\nDo you want to continue (y or n) ?: ";
			cin >> cont;
			if (cont == 'y')
				continue;

			break;
		case 4:
			cout << "\n\tStudents who like both vanilla or butterscotch: \n";
			intersection(headv, headb);

			cout << "\nDo you want to continue (y or n) ?: ";
			cin >> cont;
			if (cont == 'y')
				continue;

			break;
		case 5:
			cout << "\n\tStudents who like only vanilla but not butterscotch: \n";
			OnlyVanilla(headv, headb);

			cout << "\nDo you want to continue (y or n) ?: ";
			cin >> cont;
			if (cont == 'y')
				continue;

			break;
		case 6:
			cout << "\n\tStudents who like only butterscotch but not vanilla: \n";
			OnlyButterscotch(headv, headb);

			cout << "\nDo you want to continue (y or n) ?: ";
			cin >> cont;
			if (cont == 'y')
				continue;

			break;
		case 7:
			cout << "\n\tNo. of Students who like neither vanilla nor butterscotch\n"
				 << m - count;

			cout << "\nDo you want to continue (y or n) ?: ";
			cin >> cont;
			if (cont == 'y')
				continue;

			break;
		case 8:
			cout << "\nDone!!";

			cout << "\nDo you want to continue (y or n) ?: ";
			cin >> cont;
			if (cont == 'y')
				continue;
			exit(0);
		}
	}
	return 0;
}

// OUTPUT:

/*

Enter the total no of students: 8

-----------Students List-----------
        1] Create
        2] Display
        3] Students who like either vanilla or butterscotch or both
        4] Students who like both vanilla or butterscotch
        5] Students who like only vanilla but not butterscotch
        6] Students who like only butterscotch but not vanilla
        7] No of students who like neither vanilla nor butterscotch
        8] Exit
Enter your choice: 1

        Students who like vanilla:

Enter the no of students: 4

Enter the students roll numbers: 1

Enter the students roll numbers: 2

Enter the students roll numbers: 3

Enter the students roll numbers: 4

        Students who like butterscotch:

Enter the no of students: 4

Enter the students roll numbers: 3

Enter the students roll numbers: 4

Enter the students roll numbers: 5

Enter the students roll numbers: 6

Do you want to continue (y or n) ?: y

-----------Students List-----------
        1] Create
        2] Display
        3] Students who like either vanilla or butterscotch or both
        4] Students who like both vanilla or butterscotch
        5] Students who like only vanilla but not butterscotch
        6] Students who like only butterscotch but not vanilla
        7] No of students who like neither vanilla nor butterscotch
        8] Exit
Enter your choice: 2

-------------------Displaying Total Students------------------
        Students who like vanilla:
        1->     2->     3->     4->     NULL
        Total no of students: 4

        Students who like butterscotch:
        3->     4->     5->     6->     NULL
        Total no of students: 4

Do you want to continue (y or n) ?: y

-----------Students List-----------
        1] Create
        2] Display
        3] Students who like either vanilla or butterscotch or both
        4] Students who like both vanilla or butterscotch
        5] Students who like only vanilla but not butterscotch
        6] Students who like only butterscotch but not vanilla
        7] No of students who like neither vanilla nor butterscotch
        8] Exit
Enter your choice: 3

        Students who like either vanilla or butterscotch:
        1->     2->     3->     4->     5->     6->     NULL
count: 6
Do you want to continue (y or n) ?: y

-----------Students List-----------
        1] Create
        2] Display
        3] Students who like either vanilla or butterscotch or both
        4] Students who like both vanilla or butterscotch
        5] Students who like only vanilla but not butterscotch
        6] Students who like only butterscotch but not vanilla
        7] No of students who like neither vanilla nor butterscotch
        8] Exit
Enter your choice: 4

        Students who like both vanilla or butterscotch:
        3->     4->     NULL
Do you want to continue (y or n) ?: y

-----------Students List-----------
        1] Create
        2] Display
        3] Students who like either vanilla or butterscotch or both
        4] Students who like both vanilla or butterscotch
        5] Students who like only vanilla but not butterscotch
        6] Students who like only butterscotch but not vanilla
        7] No of students who like neither vanilla nor butterscotch
        8] Exit
Enter your choice: 5

        Students who like only vanilla but not butterscotch:
        1->     NULL    2->     NULL    NULL    NULL
Do you want to continue (y or n) ?: y

-----------Students List-----------
        1] Create
        2] Display
        3] Students who like either vanilla or butterscotch or both
        4] Students who like both vanilla or butterscotch
        5] Students who like only vanilla but not butterscotch
        6] Students who like only butterscotch but not vanilla
        7] No of students who like neither vanilla nor butterscotch
        8] Exit
Enter your choice: 6

        Students who like only butterscotch but not vanilla:
        NULL    NULL    5->     NULL    6->     NULL
Do you want to continue (y or n) ?: y

-----------Students List-----------
        1] Create
        2] Display
        3] Students who like either vanilla or butterscotch or both
        4] Students who like both vanilla or butterscotch
        5] Students who like only vanilla but not butterscotch
        6] Students who like only butterscotch but not vanilla
        7] No of students who like neither vanilla nor butterscotch
        8] Exit
Enter your choice: 7

        No. of Students who like neither vanilla nor butterscotch
2
Do you want to continue (y or n) ?: y

-----------Students List-----------
        1] Create
        2] Display
        3] Students who like either vanilla or butterscotch or both
        4] Students who like both vanilla or butterscotch
        5] Students who like only vanilla but not butterscotch
        6] Students who like only butterscotch but not vanilla
        7] No of students who like neither vanilla nor butterscotch
        8] Exit
Enter your choice: 8

Done!!
Do you want to continue (y or n) ?: y

-----------Students List-----------
        1] Create
        2] Display
        3] Students who like either vanilla or butterscotch or both
        4] Students who like both vanilla or butterscotch
        5] Students who like only vanilla but not butterscotch
        6] Students who like only butterscotch but not vanilla
        7] No of students who like neither vanilla nor butterscotch
        8] Exit
Enter your choice: 1

        Students who like vanilla:

Enter the no of students: 5

Enter the students roll numbers: 1

Enter the students roll numbers: 2

Enter the students roll numbers: 3

Enter the students roll numbers: 4

Enter the students roll numbers: 5

        Students who like butterscotch:

Enter the no of students: 5

Enter the students roll numbers: 3

Enter the students roll numbers: 4

Enter the students roll numbers: 5

Enter the students roll numbers: 6

Enter the students roll numbers: 7

Do you want to continue (y or n) ?: y

-----------Students List-----------
        1] Create
        2] Display
        3] Students who like either vanilla or butterscotch or both
        4] Students who like both vanilla or butterscotch
        5] Students who like only vanilla but not butterscotch
        6] Students who like only butterscotch but not vanilla
        7] No of students who like neither vanilla nor butterscotch
        8] Exit
Enter your choice: 2

-------------------Displaying Total Students------------------
        Students who like vanilla:
        1->     2->     3->     4->     5->     NULL
        Total no of students: 5

        Students who like butterscotch:
        3->     4->     5->     6->     7->     NULL
        Total no of students: 5

Do you want to continue (y or n) ?: y

-----------Students List-----------
        1] Create
        2] Display
        3] Students who like either vanilla or butterscotch or both
        4] Students who like both vanilla or butterscotch
        5] Students who like only vanilla but not butterscotch
        6] Students who like only butterscotch but not vanilla
        7] No of students who like neither vanilla nor butterscotch
        8] Exit
Enter your choice: 3

        Students who like either vanilla or butterscotch:
        1->     2->     3->     4->     5->     6->     7->     NULL
count: 7
Do you want to continue (y or n) ?: y

-----------Students List-----------
        1] Create
        2] Display
        3] Students who like either vanilla or butterscotch or both
        4] Students who like both vanilla or butterscotch
        5] Students who like only vanilla but not butterscotch
        6] Students who like only butterscotch but not vanilla
        7] No of students who like neither vanilla nor butterscotch
        8] Exit
Enter your choice: 4

        Students who like both vanilla or butterscotch:
        3->     4->     5->     NULL
Do you want to continue (y or n) ?: y

-----------Students List-----------
        1] Create
        2] Display
        3] Students who like either vanilla or butterscotch or both
        4] Students who like both vanilla or butterscotch
        5] Students who like only vanilla but not butterscotch
        6] Students who like only butterscotch but not vanilla
        7] No of students who like neither vanilla nor butterscotch
        8] Exit
Enter your choice: 5

        Students who like only vanilla but not butterscotch:
        1->     NULL    2->     NULL    NULL    NULL    NULL
Do you want to continue (y or n) ?: y

-----------Students List-----------
        1] Create
        2] Display
        3] Students who like either vanilla or butterscotch or both
        4] Students who like both vanilla or butterscotch
        5] Students who like only vanilla but not butterscotch
        6] Students who like only butterscotch but not vanilla
        7] No of students who like neither vanilla nor butterscotch
        8] Exit
Enter your choice: 6

        Students who like only butterscotch but not vanilla:
        NULL    NULL    NULL    6->     NULL    7->     NULL
Do you want to continue (y or n) ?: y

-----------Students List-----------
        1] Create
        2] Display
        3] Students who like either vanilla or butterscotch or both
        4] Students who like both vanilla or butterscotch
        5] Students who like only vanilla but not butterscotch
        6] Students who like only butterscotch but not vanilla
        7] No of students who like neither vanilla nor butterscotch
        8] Exit
Enter your choice: 7

        No. of Students who like neither vanilla nor butterscotch
1
Do you want to continue (y or n) ?: y

-----------Students List-----------
        1] Create
        2] Display
        3] Students who like either vanilla or butterscotch or both
        4] Students who like both vanilla or butterscotch
        5] Students who like only vanilla but not butterscotch
        6] Students who like only butterscotch but not vanilla
        7] No of students who like neither vanilla nor butterscotch
        8] Exit
Enter your choice: 8

Done!!
Do you want to continue (y or n) ?: n

*/
