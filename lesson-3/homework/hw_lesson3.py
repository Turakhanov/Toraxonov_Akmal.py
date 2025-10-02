{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "ff781112",
   "metadata": {},
   "source": [
    "1. Create and Access List Elements\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "fbfc06bf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "orange\n"
     ]
    }
   ],
   "source": [
    "fruits = [\"apple\",\"banana\", \"orange\",\"strawberry\",\"pear\" ]\n",
    "print(fruits[2])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d9a9597b",
   "metadata": {},
   "source": [
    "2. Concatenate Two Lists\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "5c3242f9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 4, 5, 6]\n"
     ]
    }
   ],
   "source": [
    "list1 = [1,2,3]\n",
    "list2 = [4,5,6]\n",
    "\n",
    "list1.extend(list2)\n",
    "print(list1)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "275968da",
   "metadata": {},
   "source": [
    "3. Extract Elements from a List\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "5ee384ab",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 6, 11]\n"
     ]
    }
   ],
   "source": [
    "num = [1,2,3,4,5,6,7,8,9,10,11]\n",
    "first = num[0]\n",
    "last = num[-1]\n",
    "middle = num[len(num)//2]\n",
    "\n",
    "new = [first,middle,last]\n",
    "print(new)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "28ce87c4",
   "metadata": {},
   "source": [
    "4. Convert List to Tuple\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "e9b5bdaf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('Inception', 'Interstellar', 'The Dark Knight', 'Tenet', 'Dune')\n"
     ]
    }
   ],
   "source": [
    "movies = [\"Inception\", \"Interstellar\", \"The Dark Knight\", \"Tenet\", \"Dune\"]\n",
    "\n",
    "tuple_movies = tuple(movies)\n",
    "\n",
    "print(tuple_movies)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "67f81399",
   "metadata": {},
   "source": [
    "5. Check Element in a List\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "f4fff2a8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Yes\n"
     ]
    }
   ],
   "source": [
    "cities = [\"London\", \"New York\", \"Paris\", \"Tokyo\", \"Berlin\"]\n",
    "\n",
    "if \"Paris\" in cities:\n",
    "    print(\"Yes\")\n",
    "else:\n",
    "    print(\"No\")    "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a78a86e2",
   "metadata": {},
   "source": [
    "6. Duplicate a List Without Using Loops\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "047f0dcf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]\n"
     ]
    }
   ],
   "source": [
    "numbers = [1,2,3,4,5]\n",
    "dup = numbers*2\n",
    "print(dup)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2b309086",
   "metadata": {},
   "source": [
    "7. Swap First and Last Elements of a List\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "9138fe99",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[5, 2, 3, 4, 1]\n"
     ]
    }
   ],
   "source": [
    "numbers = [1,2,3,4,5]\n",
    "numbers[0],numbers[-1]=numbers[-1],numbers[0]\n",
    "\n",
    "print(numbers)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "20c9ce14",
   "metadata": {},
   "source": [
    "8. Slice a Tuple\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "4c1b48f2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(4, 5, 6, 7)\n"
     ]
    }
   ],
   "source": [
    "numbers = (1,2,3,4,5,6,7,8,9,10)\n",
    "print(numbers[3:7])\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0b104f8e",
   "metadata": {},
   "source": [
    "9. Count Occurrences in a List\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "b47c2c2e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n"
     ]
    }
   ],
   "source": [
    "colors = [\"red\",\"blue\",\"green\",\"blue\",\"black\",\"brown\", \"blue\"]\n",
    "print(colors.count(\"blue\"))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b51ce524",
   "metadata": {},
   "source": [
    "10. Find the Index of an Element in a Tuple\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "18f43d6d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n"
     ]
    }
   ],
   "source": [
    "animals = (\"lion\",\"cat\",\"dog\",\"horse\")\n",
    "print(animals.index(\"lion\"))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4163d9cd",
   "metadata": {},
   "source": [
    "11. Merge Two Tuples\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "242d4eb7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(1, 2, 3, 4, 5, 6)\n"
     ]
    }
   ],
   "source": [
    "num1 = (1,2,3)\n",
    "num2 = (4,5,6)\n",
    "merge = num1+num2\n",
    "print(merge)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "05cfb825",
   "metadata": {},
   "source": [
    "12. Find the Length of a List and Tuple\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "c6b7f9e7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "List: 5\n",
      "Tuple: 7\n"
     ]
    }
   ],
   "source": [
    "l = [1,2,3,4,5]\n",
    "t = (1,2,3,4,5,6,7)\n",
    "print(\"List:\",len(l))\n",
    "print(\"Tuple:\",len(t))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8b6068a6",
   "metadata": {},
   "source": [
    "13. Convert Tuple to List\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "22056ac3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 4, 5, 6, 7]\n"
     ]
    }
   ],
   "source": [
    "t = (1,2,3,4,5,6,7)\n",
    "l = list(t)\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ac045fa7",
   "metadata": {},
   "source": [
    "14. Find Maximum and Minimum in a Tuple\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "e1c62010",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Max: 7\n",
      "Min: 1\n"
     ]
    }
   ],
   "source": [
    "t = (1,2,3,4,5,6,7)\n",
    "maximum = max(t)\n",
    "minimum = min(t)\n",
    "\n",
    "print(\"Max:\",maximum)\n",
    "print(\"Min:\",minimum)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d45998b7",
   "metadata": {},
   "source": [
    "15. Reverse a Tuple\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "c9d94a6e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('apple', 'world', 'hello', 'word')\n",
      "('apple', 'world', 'hello', 'word')\n"
     ]
    }
   ],
   "source": [
    "t = (\"word\",\"hello\",\"world\",\"apple\")\n",
    "print(tuple(reversed(t)))\n",
    "print(t[::-1])"
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
