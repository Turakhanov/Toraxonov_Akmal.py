{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "1dbadd78",
   "metadata": {},
   "source": [
    "1. def is_leap(year): \"\"\" Determines whether a given year is a leap year.\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "8441835a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Leap year!\n"
     ]
    }
   ],
   "source": [
    "year = int(input(\"Enter year:\"))\n",
    "if (year%4==0 and year%100!=0) or (year%400==0):\n",
    "    print(\"Leap year!\")\n",
    "else:\n",
    "    print(\"Not leap year!\")    "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6cb3a3d0",
   "metadata": {},
   "source": [
    "2. Conditional Statements Exercise\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "69fd5175",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Wierd\n"
     ]
    }
   ],
   "source": [
    "n = int(input(\"Enter n:\"))\n",
    "\n",
    "if n%2==1:\n",
    "    print(\"Wierd\")\n",
    "elif (n%2==0) and (2<=n<=5):\n",
    "    print(\"Not Wierd\")\n",
    "elif (n%2==0) and (6<=n<=20):\n",
    "    print(\"Wierd\")\n",
    "elif (n%2==0) and (n<20):\n",
    "    print(\"Not Wierd\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "32eca759",
   "metadata": {},
   "source": [
    "3. Given two integer numbers a and b. Find even numbers between this numbers. a and b are inclusive. Don't use loop.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "9991c3d2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[4, 6, 8, 10]\n",
      "[2, 4, 6, 8]\n",
      "[4, 6, 8, 10]\n",
      "[2, 4, 6, 8]\n"
     ]
    }
   ],
   "source": [
    "def even_numbers(a,b):\n",
    "    if a%2==0:\n",
    "        return list(range(a,b+1,2))\n",
    "    else:\n",
    "        return list(range(a+1,b+1,2))\n",
    "    \n",
    "print(even_numbers(3,10))\n",
    "print(even_numbers(2,8))\n",
    "\n",
    "def even_numbers2(a,b):\n",
    "    return list(range(a+(a%2),b+1,2))\n",
    "\n",
    "print(even_numbers2(3,10))\n",
    "print(even_numbers2(2,8))"
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
