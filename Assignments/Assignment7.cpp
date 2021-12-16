/*
Department of Computer Engineering has student's club named 'Pinnacle Club'. 
Students of second, third and final year of department can be granted membership on request. 
Similarly one may cancel the membership of club. 
First node is reserved for president of club and last node is reserved for secretary of club. 
Write C++ program to maintain club member‘s information using singly linked list. 
Store student PRN and Name. Write functions to: 

a) Add and delete the members as well as president or even secretary. 
b) Compute total number of members of club 
c) Display members 
d) Two linked lists exists for two divisions. Concatenate two lists. 

*/

#include <iostream>
#include <string.h>
using namespace std;

// Node created
typedef struct node
{
	int prn;
	string name;
	node *next;
} node;

// Class list of Club members
class ClubList
{
	node *head, *temp;

public:
	ClubList()
	{
		head = NULL;
	}
	node *create(int prn, string name);
	void insertEnd();
	void insertBeg();
	void insertAt(int i);
	void deleteAt(int i);
	void display();
	int count();
	void reverse();
	void rev(node *t);
	node *readAt(int i);
	void concatenate(ClubList A, ClubList B);
	void operation();
};

// Create function
node *ClubList::create(int prn, string name)
{
	temp = new (node);
	if (temp == NULL)
	{
		cout << "Memory Allocation Failed!" << endl;
		return 0;
	}
	else
	{
		temp->prn = prn;
		temp->name = name;
		temp->next = NULL;
		return temp;
	}
}

// Insert At Beginning
void ClubList::insertBeg()
{
	int prn;
	string name;
	cout << "Enter PRN: ";
	cin >> prn;
	cout << "Enter Name: ";
	fflush(stdin);
	getline(cin, name);
	node *t = head;
	temp = create(prn, name);
	if (head == NULL)
	{
		head = temp;
		head->next = NULL;
	}
	else
	{
		temp->next = head;
		head = temp;
		cout << "We have a New President!" << endl;
	}
}

// Insert At End
void ClubList::insertEnd()
{
	int prn;
	string name;
	cout << "Enter PRN: ";
	cin >> prn;
	cout << "Enter Name: ";
	fflush(stdin);
	getline(cin, name);
	node *t = head;
	temp = create(prn, name);
	if (head == NULL)
	{
		head = temp;
		head->next = NULL;
	}
	else
	{
		while ((t->next) != NULL)
		{
			t = t->next;
		}
		temp->next = NULL;
		t->next = temp;
		cout << "We have a Scretary inserted at last!" << endl;
	}
}

// Insert at any particular position
void ClubList::insertAt(int i)
{
	int prn, position = i - 1, counter = 1;
	string name;
	node *ptr;
	node *t = head;
	while ((t->next) != NULL)
	{
		t = t->next;
		counter++;
	}
	t = head;
	if (i == 1)
	{
		insertBeg();
	}
	else if (position > counter || i <= 0)
	{
		cout << "Entered position is out of scope." << endl;
	}
	else
	{
		cout << "Enter PRN: ";
		cin >> prn;
		cout << "Enter Name: ";
		fflush(stdin);
		getline(cin, name);
		temp = create(prn, name);
		while (position--)
		{
			ptr = t;
			t = t->next;
		}
		temp->next = t;
		ptr->next = temp;
		cout << "Member Inserted at Position: " << i << endl;
	}
}

// Delete at particular position
void ClubList::deleteAt(int i)
{
	int prn, pos = i - 1, counter = 1;
	string name;
	node *ptrl, *ptrr;
	node *t = head;
	while ((t->next) != NULL)
	{
		t = t->next;
		counter++;
	}
	t = head;
	if (i == 1)
	{
		ptrl = head;
		head = head->next;
		delete ptrl;
	}
	else if (pos > counter || i <= 0)
	{
		cout << "Entered member doesn't exist." << endl;
	}
	else
	{
		while (pos--)
		{
			ptrl = t;
			t = t->next;
			ptrr = t->next;
		}
		ptrl->next = ptrr;
		delete t;
		cout << "Member Deleted at Position: " << i << endl;
	}
}

// Display function
void ClubList::display()
{
	temp = head;
	cout << "President: ";
	cout << temp->name << " || " << temp->prn << " -> ";
	if (temp->next != NULL)
	{
		temp = temp->next;
	}
	while (temp->next != NULL)
	{
		cout << temp->name << " || " << temp->prn << " -> ";
		temp = temp->next;
	}
	cout << "Secretary: ";
	cout << temp->name << " || " << temp->prn << " -> ";
	cout << "NULL" << endl;
}

// Counting the total members
int ClubList::count()
{
	temp = head;
	int count = 0;
	while (temp != NULL)
	{
		count++;
		temp = temp->next;
	}
	return count;
}

// Concatenate two list of members
void ClubList::concatenate(ClubList A, ClubList B)
{
	node *last, *last1;
	node *t = A.head;
	while (t != NULL)
	{
		int prn = t->prn;
		string name = t->name;
		temp = create(prn, name);
		if (head == NULL)
		{
			head = temp;
			head->next = NULL;
			last = head;
		}
		else
		{
			last->next = t;
			last = t;
		}
		t = t->next;
	}
	last->next = B.head;
	t = B.head;
	while (t != NULL)
	{
		int prn = t->prn;
		string name = t->name;
		temp = create(prn, name);

		last->next = temp;
		last = temp;

		t = t->next;
	}
	last->next = NULL;
}

// Accepting members, president and secretary's name and prn number
void ClubList::operation()
{
	while (1)
	{
		int choice;
		cout << "\n -------------------------------Operation Menu------------------------------- ";
		cout << "\n1. Add ";
		cout << "\n2. Delete ";
		cout << "\n3. Member's Count";
		cout << "\n4. Display ";
		cout << "\n5. Reverse the List";
		cout << "\n0. Prev Menu" << endl;
		cout << "\n\nEnter your choice (0 to 5): ";
		cin >> choice;
		switch (choice)
		{
		case 1:
		{
			char choice;
			cout << "\n -------------------------------Add Member Menu------------------------------- ";
			cout << "\nA. Add President ";
			cout << "\nB. Add Secretary ";
			cout << "\nC. Add Member" << endl;
			cout << "\n\nEnter your choice (A to C) or (a to c): ";
			cin >> choice;
			switch (choice)
			{
			case 'A':
			case 'a':
			{
				insertBeg();
				break;
			}
			case 'B':
			case 'b':
			{
				insertEnd();
				break;
			}
			case 'C':
			case 'c':
			{
				insertAt(2);
				break;
			}
			}
			break;
		}
		case 2:
		{
			char choice;
			cout << "\n -------------------------------Delete Member Menu------------------------------- ";
			cout << "\nA. Delete President ";
			cout << "\nB. Delete Secretary ";
			cout << "\nC. Delete Member" << endl;
			cout << "\n\nEnter your choice (A to C) or (a to c): ";
			cin >> choice;
			switch (choice)
			{
			case 'A':
			{
				deleteAt(1);
				cout << "Club must have a President. Enter Details" << endl;
				insertBeg();
				break;
			}
			case 'B':
			{
				deleteAt(count());
				cout << "Club must have a Secretary. Enter Details" << endl;
				insertEnd();
				break;
			}
			case 'C':
			{
				int j;
				cout << "Enter Position for Deletion" << endl;
				cin >> j;
				deleteAt(j);
				break;
			}
			}
			break;
		}
		case 3:
		{
			cout << "Count: " << count() << endl;
			break;
		}
		case 4:
		{
			if (head == NULL)
			{
				cout << "NULL" << endl;
				break;
			}
			else
			{
				display();
				break;
			}
		}
		case 5:
		{
			reverse();
			break;
		}
		case 0:
		{
			cout << "\n\nDone!";
			return;
		}
		}
	}
}

// Reverse Recursion
void ClubList::rev(node *t)
{
	if (t->next != NULL)
	{
		rev(t->next);
	}
	if (t == head)
		cout << "Secretary: " << t->prn << " || " << t->name << endl;
	else if (t->next == NULL)
		cout << "President: " << t->prn << " || " << t->name << " -> ";
	else
		cout << "Member: " << t->prn << " || " << t->name << " -> ";
}

// Reverseing function
void ClubList::reverse()
{
	rev(head);
}

// Read at function
node *ClubList::readAt(int i)
{
	node *t = head;
	int c = count();
	while (c--)
	{
		t = t->next;
	}
}

// Main Menu
int main()
{
	ClubList listA, listB, concatf;
	int choice;
	char cont = 'y';
  
	while (cont == 'y')
	{
		cout << "\n -------------------------------Menu------------------------------- ";
		cout << "\n1. Member List A ";
		cout << "\n2. Member List B ";
		cout << "\n3. Concatenate --> Member ListA and Member ListB";
		// cout << "\n4. Concatenate --> Member ListB and Member ListA";
		cout << "\n0. Exit" << endl;
		cout << "\n\nEnter your choice (0-4): ";
		cin >> choice;
		switch (choice)
		{
		case 1:
			cout << "\nMemeber List A:" << endl;
			listA.operation();
			break;
        
		case 2:
			cout << "\nMemeber List B:" << endl;
			listB.operation();
			break;
        
		case 3:
			concatf.concatenate(listA, listB);
			concatf.display();
			cout << "\nDo you want to continue (y or n) ?: ";
			cin >> cont;
			if (cont == 'y')
				continue;
			break;
        
		case 4:
			concatf.concatenate(listB, listA);
			concatf.display();
			cout << "\nDo you want to continue (y or n) ?: ";
			cin >> cont;
			if (cont == 'y')
				continue;
			break;
        
		case 0:
			cout << "\n\nDone!";
			return 0;
		}
	}
}
