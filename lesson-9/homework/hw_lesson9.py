{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "e7059b0f",
   "metadata": {},
   "source": [
    "1. Circle Class\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "bbeb0fb7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Area: 78.5\n",
      "Perimeter: 31.400000000000002\n"
     ]
    }
   ],
   "source": [
    "class Circle():\n",
    "    def __init__(self,r):\n",
    "        self.r = r\n",
    "    \n",
    "    def area(self):\n",
    "        return 3.14*(self.r**2)\n",
    "    def perimeter(self):\n",
    "        return 3.14*self.r*2\n",
    "    \n",
    "radius = float(input(\"Enter radius\"))\n",
    "c = Circle(r)\n",
    "\n",
    "print(\"Area:\", c.area())\n",
    "print(\"Perimeter:\", c.perimeter())\n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "99b670f4",
   "metadata": {},
   "source": [
    "2. Person Class\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "b6226079",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Akmal is from USA and 16 years old!\n"
     ]
    }
   ],
   "source": [
    "from datetime import date, datetime\n",
    "\n",
    "class Person():\n",
    "    def __init__(self, name, country, birth_year):\n",
    "        self.name = name\n",
    "        self.country = country\n",
    "        self.birth_year = datetime.strptime(birth_year,\"%Y-%m-%d\").date()\n",
    "\n",
    "    def age(self):\n",
    "        today = date.today()\n",
    "        age = today.year-self.birth_year.year\n",
    "        if (today.month,today.day)<(self.birth_year.month, self.birth_year.day):\n",
    "            age -=1\n",
    "        return age\n",
    "    \n",
    "name = input(\"Enter your name:\")\n",
    "country = input(\"Your country:\")\n",
    "dob = input(\"Your date of birth:\")\n",
    "\n",
    "person = Person(name, country, dob)\n",
    "\n",
    "print(f\"{person.name} is from {person.country} and {person.age()} years old!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f602aba0",
   "metadata": {},
   "source": [
    "3. Calculator Class\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "269d0a39",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Results:\n",
      "Addition:  12\n",
      "Subtruction:  12\n",
      "Multiplication:  0\n",
      "Division:  None\n"
     ]
    }
   ],
   "source": [
    "class Calculator():\n",
    "    def __init__(self,a,b):\n",
    "        self.a=a\n",
    "        self.b=b\n",
    "    def add(self):\n",
    "        return self.a+self.b\n",
    "    def subtract(self):\n",
    "        return self.a-self.b\n",
    "    def multiply(self):\n",
    "        return self.a*self.b\n",
    "    def divide(self):\n",
    "        if self.b==0:\n",
    "            \"Division by zero impossible!\"\n",
    "        else: \n",
    "            return self.a/self.b\n",
    "\n",
    "        \n",
    "a = int(input(\"Enter a\"))\n",
    "b = int(input(\"Enter b\"))\n",
    "\n",
    "calc = Calculator(a,b)\n",
    "\n",
    "print(\"Results:\")\n",
    "print(\"Addition: \",calc.add())\n",
    "print(\"Subtruction: \",calc.subtract())\n",
    "print(\"Multiplication: \",calc.multiply())\n",
    "print(\"Division: \", calc.divide())\n",
    "      \n",
    "\n",
    "\n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a17c9ca0",
   "metadata": {},
   "source": [
    "4. Shape and Subclasses\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "a81bad0f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Area: 30\n",
      "Perimeter 22\n",
      "Area: 254.34\n",
      "Perimeter 56.52\n"
     ]
    }
   ],
   "source": [
    "class Shape():\n",
    "    def area(self):\n",
    "        return 0\n",
    "    def perimeter(self):\n",
    "        return 0\n",
    "    \n",
    "class Rectangle(Shape):\n",
    "    def __init__(self,w,h):\n",
    "        self.w = w\n",
    "        self.h = h\n",
    "    def area(self):\n",
    "        return self.w*self.h\n",
    "    def perimeter(self):\n",
    "        return (self.w+self.h)*2\n",
    "\n",
    "class Circle(Shape):\n",
    "    def __init__(self,r):\n",
    "        self.r=r\n",
    "    def area(self):\n",
    "        return self.r**2*3.14\n",
    "    def perimeter(self):\n",
    "        return self.r*2*3.14\n",
    "    \n",
    "shapes = [Rectangle(5,6),Circle(9)]\n",
    "\n",
    "for s in shapes:\n",
    "    print(F\"Area: {s.area()}\")\n",
    "    print(f\"Perimeter {s.perimeter()}\")\n",
    "    \n",
    "\n",
    "        \n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8be7f50d",
   "metadata": {},
   "source": [
    "5. Binary Search Tree Class\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "52a02e1d",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Node:\n",
    "    def __init__(self, key):\n",
    "        self.key = key\n",
    "        self.left = None\n",
    "        self.right = None\n",
    "\n",
    "\n",
    "class BinarySearchTree:\n",
    "    def __init__(self):\n",
    "        self.root = None\n",
    "\n",
    "    def insert(self, key):\n",
    "        if self.root is None:\n",
    "            self.root = Node(key)\n",
    "        else:\n",
    "            self._insert(self.root, key)\n",
    "\n",
    "    def _insert(self, current, key):\n",
    "        if key < current.key:\n",
    "            if current.left is None:\n",
    "                current.left = Node(key)\n",
    "            else:\n",
    "                self._insert(current.left, key)\n",
    "        elif key > current.key:\n",
    "            if current.right is None:\n",
    "                current.right = Node(key)\n",
    "            else:\n",
    "                self._insert(current.right, key)\n",
    "        # If key == current.key, we ignore duplicates\n",
    "\n",
    "    def search(self, key):\n",
    "        return self._search(self.root, key)\n",
    "\n",
    "    def _search(self, current, key):\n",
    "        if current is None:\n",
    "            return False\n",
    "        if key == current.key:\n",
    "            return True\n",
    "        elif key < current.key:\n",
    "            return self._search(current.left, key)\n",
    "        else:\n",
    "            return self._search(current.right, key)\n",
    "\n",
    "    def inorder(self):\n",
    "        result = []\n",
    "        self._inorder(self.root, result)\n",
    "        return result\n",
    "\n",
    "    def _inorder(self, node, result):\n",
    "        if node:\n",
    "            self._inorder(node.left, result)\n",
    "            result.append(node.key)\n",
    "            self._inorder(node.right, result)\n",
    "\n",
    "\n",
    "# Example usage\n",
    "bst = BinarySearchTree()\n",
    "\n",
    "# Insert elements\n",
    "elements = [50, 30, 70, 20, 40, 60, 80]\n",
    "for e in elements:\n",
    "    bst.insert(e)\n",
    "\n",
    "# Display traversal\n",
    "print(\"Inorder Traversal:\", bst.inorder())\n",
    "\n",
    "# Search example\n",
    "key = int(input(\"Enter a number to search: \"))\n",
    "if bst.search(key):\n",
    "    print(f\"{key} found in the tree.\")\n",
    "else:\n",
    "    print(f\"{key} not found in the tree.\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7ca9025d",
   "metadata": {},
   "source": [
    "6. Stack Data Structure\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "025bc333",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Stack after pushing elements:  [10, 20, 30, 40]\n",
      "Top element:  40\n",
      "Popped element:  40\n",
      "Stack after popping:  [10, 20, 30]\n",
      "Is stack empty? False\n",
      "Stack size:  3\n"
     ]
    }
   ],
   "source": [
    "class Stack():\n",
    "    def __init__(self):\n",
    "        self.items = []\n",
    "    \n",
    "    def push(self,item): # add item to the stack\n",
    "        self.items.append(item)\n",
    "\n",
    "    def pop(self):  # remove and return top element\n",
    "        if not self.is_empty():\n",
    "            return self.items.pop()\n",
    "        else:\n",
    "            return \"Stack is empty\"\n",
    "    \n",
    "    def peek(self): # return top element without removing it\n",
    "        if not self.is_empty():\n",
    "            return self.items[-1]\n",
    "        else:\n",
    "            return \"Stack is empty\"\n",
    "        \n",
    "    def is_empty(self): # check if the stack is empty\n",
    "        return len(self.items)==0\n",
    "    \n",
    "    def size(self): # returns the size of the stack\n",
    "        return len(self.items)\n",
    "    \n",
    "stack = Stack()\n",
    "\n",
    "stack.push(10)\n",
    "stack.push(20)\n",
    "stack.push(30)\n",
    "stack.push(40)\n",
    "print(\"Stack after pushing elements: \", stack.items)\n",
    "\n",
    "print(f\"Top element: \",stack.peek())\n",
    "print(f\"Popped element: \", stack.pop())\n",
    "print(f\"Stack after popping: \", stack.items)\n",
    "print(f\"Is stack empty?\", stack.is_empty())\n",
    "print(f\"Stack size: \",stack.size())\n",
    "\n",
    "\n",
    "    \n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1ab00bb1",
   "metadata": {},
   "source": [
    "7. Linked List Data Structure\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "39d81fe2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Linked list after insertion:\n",
      "10 -> 20 -> 30 -> None\n",
      "Linked list after deleting 20:\n",
      "10 -> 30 -> None\n"
     ]
    }
   ],
   "source": [
    "class Node:\n",
    "    def __init__(self, data):\n",
    "        self.data = data        # store the data\n",
    "        self.next = None        # pointer to the next node (initially empty)\n",
    "\n",
    "\n",
    "class LinkedList:\n",
    "    def __init__(self):\n",
    "        self.head = None        # the start (head) of the linked list\n",
    "\n",
    "    def insert(self, data):\n",
    "        new_node = Node(data)   # create a new node with given data\n",
    "        if self.head is None:   # if list is empty, new node becomes head\n",
    "            self.head = new_node\n",
    "        else:\n",
    "            current = self.head\n",
    "            # move to the last node\n",
    "            while current.next:\n",
    "                current = current.next\n",
    "            # add the new node at the end\n",
    "            current.next = new_node\n",
    "\n",
    "    def delete(self, data):\n",
    "        current = self.head\n",
    "        previous = None\n",
    "\n",
    "        # find the node to delete\n",
    "        while current and current.data != data:\n",
    "            previous = current\n",
    "            current = current.next\n",
    "\n",
    "        # if data not found\n",
    "        if current is None:\n",
    "            print(\"Data not found in the list.\")\n",
    "            return\n",
    "\n",
    "        # if the node to delete is the first node\n",
    "        if previous is None:\n",
    "            self.head = current.next\n",
    "        else:\n",
    "            # skip the current node\n",
    "            previous.next = current.next\n",
    "\n",
    "    def display(self):\n",
    "        current = self.head\n",
    "        while current:\n",
    "            print(current.data, end=\" -> \")\n",
    "            current = current.next\n",
    "        print(\"None\")\n",
    "\n",
    "\n",
    "# Example usage\n",
    "ll = LinkedList()\n",
    "ll.insert(10)\n",
    "ll.insert(20)\n",
    "ll.insert(30)\n",
    "print(\"Linked list after insertion:\")\n",
    "ll.display()\n",
    "\n",
    "ll.delete(20)\n",
    "print(\"Linked list after deleting 20:\")\n",
    "ll.display()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c8a27b09",
   "metadata": {},
   "source": [
    "8. Shopping Cart Class\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "25e69972",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Shopping():\n",
    "    def __init__(self):\n",
    "        self.items=[]\n",
    "        self.total_price =0\n",
    "\n",
    "    def add(self,item,price):\n",
    "        self.items.append(item)\n",
    "        self.total_price += price\n",
    "        return f\"{item} qoshildi!\"\n",
    "\n",
    "    \n",
    "    def remove(self,item,price):\n",
    "        self.items.remove(item)\n",
    "        self.total_price -= price\n",
    "        return f\"{item} ochirildi\"\n",
    "    \n",
    "    def calculate(self):\n",
    "        print(\"Items:\",self.items)\n",
    "        print(\"Total price: \",self.total_price)\n",
    "\n",
    "\n",
    "shop = Shopping()\n",
    "print(shop.add(\"Apple\",20_000))\n",
    "print(shop.add(\"Banana\",30_000))\n",
    "print(shop.add(\"Orange\",40_000))\n",
    "print(shop.add(\"Pear\",50_000))\n",
    "print(shop.add(\"Lemon\",70_000))\n",
    "print(shop.calculate())\n",
    "\n",
    "print(shop.remove(\"Lemon\",70_000))\n",
    "print(shop.calculate())\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "333521a2",
   "metadata": {},
   "source": [
    "9. Stack with Display\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f6572fe6",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Stack:\n",
    "    def __init__(self):\n",
    "        self.items = []\n",
    "\n",
    "    def push(self, item):\n",
    "        self.items.append(item)\n",
    "        print(f\"{item} added to stack\")\n",
    "\n",
    "    def pop(self):\n",
    "        if not self.items:\n",
    "            print(\"Stack is empty! Nothing to pop.\")\n",
    "        else:\n",
    "            removed = self.items.pop()\n",
    "            print(f\"{removed} removed from stack\")\n",
    "\n",
    "    def display(self):\n",
    "        if not self.items:\n",
    "            print(\"Stack is empty!\")\n",
    "        else:\n",
    "            print(\"Stack elements:\", self.items)\n",
    "\n",
    "\n",
    "# Example usage\n",
    "stack = Stack()\n",
    "\n",
    "stack.push(10)\n",
    "stack.push(20)\n",
    "stack.push(30)\n",
    "\n",
    "stack.display()\n",
    "\n",
    "stack.pop()\n",
    "stack.display()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ca24fc74",
   "metadata": {},
   "source": [
    "10. Queue Data Structure\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "4a521f08",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10 added to the queue\n",
      "20 added to the queue\n",
      "30 added to the queue\n",
      "Queue elements: [10, 20, 30]\n",
      "10 removed from the queue\n",
      "Queue elements: [20, 30]\n"
     ]
    }
   ],
   "source": [
    "class Queue:\n",
    "    def __init__(self):\n",
    "        self.items = []\n",
    "\n",
    "    def enqueue(self, item):\n",
    "        self.items.append(item)\n",
    "        print(f\"{item} added to the queue\")\n",
    "\n",
    "    def dequeue(self):\n",
    "        if not self.items:\n",
    "            print(\"Queue is empty! Nothing to remove.\")\n",
    "        else:\n",
    "            removed = self.items.pop(0)\n",
    "            print(f\"{removed} removed from the queue\")\n",
    "\n",
    "    def display(self):\n",
    "        if not self.items:\n",
    "            print(\"Queue is empty!\")\n",
    "        else:\n",
    "            print(\"Queue elements:\", self.items)\n",
    "\n",
    "\n",
    "# Example usage\n",
    "queue = Queue()\n",
    "\n",
    "queue.enqueue(10)\n",
    "queue.enqueue(20)\n",
    "queue.enqueue(30)\n",
    "\n",
    "queue.display()\n",
    "\n",
    "queue.dequeue()\n",
    "queue.display()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "13f33dbc",
   "metadata": {},
   "source": [
    "11. Bank Class\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "173a5355",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Akmal hisobida 200000 sum pul bor!\n",
      "Akmal hisobida 500000 sum pul bor\n",
      "Balanse yetarli emas\n",
      "None\n",
      "Akmal hisobida 100000 sum pul bor\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "class Bank_Account():\n",
    "    def __init__(self,ism,balans):\n",
    "        self.ism=ism\n",
    "        self.balans=balans\n",
    "    \n",
    "    def deposit(self,miqdor):\n",
    "        self.balans += miqdor\n",
    "        return f\"{self.ism} hisobida {self.balans} sum pul bor\"\n",
    "    \n",
    "    def withdraw(self,miqdor):\n",
    "        if self.balans < miqdor:\n",
    "            print(F\"Balanse yetarli emas\")\n",
    "        else:\n",
    "            self.balans -= miqdor\n",
    "            print(f\"{self.ism} hisobida {self.balans} sum pul bor\")\n",
    "\n",
    "    def get_balance(self):\n",
    "        return f'{self.ism} hisobida {self.balans} sum pul bor!'\n",
    "    \n",
    "account = Bank_Account(\"Akmal\",200000)\n",
    "\n",
    "print(account.get_balance())\n",
    "print(account.deposit(300000))\n",
    "print(account.withdraw(600000))\n",
    "print(account.withdraw(400000))\n",
    "        "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
