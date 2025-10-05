{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "a4500459",
   "metadata": {},
   "source": [
    "1. Modify String with Underscores\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "d747d066",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hel_lo\n",
      "ass_alom\n",
      "abc_abc_abc_deabcd_efabcd_efg_\n"
     ]
    }
   ],
   "source": [
    "def modify_string(txt):\n",
    "    vowels = \"aeiou\"\n",
    "    result = \"\"\n",
    "    count = 0\n",
    "\n",
    "    for i in range(len(txt)):\n",
    "        result += txt[i]\n",
    "        count += 1\n",
    "\n",
    "        if count == 3:\n",
    "            if txt[i] in vowels or (i+1 < len(txt) and txt[i+1] == \"_\"):\n",
    "                pass\n",
    "            else:\n",
    "                result += \"_\"\n",
    "            count = 0\n",
    "    return result\n",
    "\n",
    "print(modify_string(\"hello\"))\n",
    "print(modify_string(\"assalom\"))\n",
    "print(modify_string(\"abcabcabcdeabcdefabcdefg\"))    "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4186ccce",
   "metadata": {},
   "source": [
    "2. Integer Squares Exercise\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "2845b5c7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "1\n",
      "4\n",
      "9\n",
      "16\n"
     ]
    }
   ],
   "source": [
    "n = int(input(\"Enter the number:\"))\n",
    "\n",
    "for i in range(0,n):\n",
    "    print(i**2)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a5879bab",
   "metadata": {},
   "source": [
    "3. Loop-Based Exercises\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "29ff0517",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "6\n",
      "7\n",
      "8\n",
      "9\n",
      "10\n"
     ]
    }
   ],
   "source": [
    "i = 0\n",
    "while i<=10:\n",
    "    print(i)\n",
    "    i +=1"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5fcc7b90",
   "metadata": {},
   "source": [
    "Print the following pattern"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "99a4a6c7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 \n",
      "1 2 \n",
      "1 2 3 \n",
      "1 2 3 4 \n",
      "1 2 3 4 5 \n"
     ]
    }
   ],
   "source": [
    "for i in range(1,6):\n",
    "    for j in range(1,i+1):\n",
    "        print(j, end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c8ec2c24",
   "metadata": {},
   "source": [
    "Calculate sum of all numbers from 1 to a given number\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "14901197",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sum: 15\n"
     ]
    }
   ],
   "source": [
    "n = int(input(\"Enter number: \"))\n",
    "total = 0\n",
    "\n",
    "for i in range(1,n+1):\n",
    "    total += i\n",
    "print(\"Sum:\",total)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "08ea3f3c",
   "metadata": {},
   "source": [
    "Exercise 4: Print multiplication table of a given number\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "33d604e1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3*1 = 3\n",
      "3*2 = 6\n",
      "3*3 = 9\n",
      "3*4 = 12\n",
      "3*5 = 15\n",
      "3*6 = 18\n",
      "3*7 = 21\n",
      "3*8 = 24\n",
      "3*9 = 27\n",
      "3*10 = 30\n"
     ]
    }
   ],
   "source": [
    "n = int(input(\"Enter number: \"))\n",
    "\n",
    "for i in range(1,11):\n",
    "    print(f\"{n}*{i} = {n*i}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "86435809",
   "metadata": {},
   "source": [
    "Exercise 5: Display numbers from a list using a loop\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "97b89f24",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "75\n",
      "150\n",
      "145\n"
     ]
    }
   ],
   "source": [
    "numbers = [12, 75, 150, 180, 145, 525, 50]\n",
    "\n",
    "for num in numbers:\n",
    "    if num>500:\n",
    "        break\n",
    "    elif num>150:\n",
    "        continue\n",
    "    elif num%5 == 0:\n",
    "        print(num)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0c4fdc51",
   "metadata": {},
   "source": [
    "Exercise 6: Count the total number of digits in a number\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "dc29bd06",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n"
     ]
    }
   ],
   "source": [
    "num = int(input(\"Enter number: \"))\n",
    "count = 0\n",
    "\n",
    "while num>0:\n",
    "    num = num // 10\n",
    "    count += 1\n",
    "    \n",
    "print(count)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ff5d2136",
   "metadata": {},
   "source": [
    "Exercise 7: Print reverse number pattern\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "9a921842",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5 4 3 2 1 \n",
      "4 3 2 1 \n",
      "3 2 1 \n",
      "2 1 \n",
      "1 \n"
     ]
    }
   ],
   "source": [
    "rows = int(input(\"Enter number: \"))\n",
    "\n",
    "for i in range(rows,0,-1):\n",
    "    for j in range(i,0,-1):\n",
    "        print(j, end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "db9a7c07",
   "metadata": {},
   "source": [
    "Exercise 8: Print list in reverse order using a loop\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "5c58bc75",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "50\n",
      "40\n",
      "30\n",
      "20\n",
      "10\n"
     ]
    }
   ],
   "source": [
    "list1 = [10, 20, 30, 40, 50]\n",
    "\n",
    "for i in list1[::-1]:\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7e0415ef",
   "metadata": {},
   "source": [
    "Exercise 9: Display numbers from -10 to -1 using a for loop\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "2f857ad6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-10\n",
      "-9\n",
      "-8\n",
      "-7\n",
      "-6\n",
      "-5\n",
      "-4\n",
      "-3\n",
      "-2\n",
      "-1\n"
     ]
    }
   ],
   "source": [
    "for i in range(-10,0):\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "41736447",
   "metadata": {},
   "source": [
    "Exercise 10: Display message “Done” after successful loop execution\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "e7b5ec62",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "Done!\n"
     ]
    }
   ],
   "source": [
    "for i in range(5):\n",
    "    print(i)\n",
    "print(\"Done!\")    "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6ab7ec69",
   "metadata": {},
   "source": [
    "Exercise 11: Print all prime numbers within a range\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "c88b9261",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "29\n",
      "31\n",
      "37\n",
      "41\n",
      "43\n",
      "47\n"
     ]
    }
   ],
   "source": [
    "start = int(input(\"Enter start: \"))\n",
    "end = int(input(\"Enter end: \"))\n",
    "\n",
    "for num in range(start,end+1):\n",
    "    if num>1:\n",
    "        for i in range(2,int(num**0.5)+1):\n",
    "            if num % i == 0:\n",
    "                break\n",
    "        else: \n",
    "            print(num)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9718a3ae",
   "metadata": {},
   "source": [
    "Exercise 12: Display Fibonacci series up to 10 terms\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "0d26c3b1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Fibonacci sequence:\n",
      "0  1  1  2  3  5  8  13  21  34  "
     ]
    }
   ],
   "source": [
    "n = 10 \n",
    "\n",
    "a, b = 0, 1\n",
    "print(\"Fibonacci sequence:\")\n",
    "\n",
    "for i in range(n):\n",
    "    print(a, end=\"  \")\n",
    "    a, b = b, a + b\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "07593900",
   "metadata": {},
   "source": [
    "Exercise 13: Find the factorial of a given number\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "07cc6ffd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "120\n"
     ]
    }
   ],
   "source": [
    "n = int(input(\"Enter number: \"))\n",
    "factorial = 1\n",
    "\n",
    "for i in range(1,n+1):\n",
    "    factorial *= i\n",
    "print(factorial)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e440e6c0",
   "metadata": {},
   "source": [
    "4. Return Uncommon Elements of Lists\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "2808d524",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 2, 5]\n"
     ]
    }
   ],
   "source": [
    "list1 = [1, 1, 2, 3, 4, 2]\n",
    "list2 = [1, 3, 4, 5]\n",
    "\n",
    "uncommon = [x for x in list1 if x not in list2] + [x for x in list2 if x not in list1]\n",
    "print(uncommon)"
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
