{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "d288b190",
   "metadata": {},
   "source": [
    "Homework 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "f44923f3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  first_name  age           City\n",
      "0      Alice   25       New York\n",
      "1        Bob   30  San Francisco\n",
      "2    Charlie   35    Los Angeles\n",
      "3      David   40        Chicago\n",
      "  first_name  age           City\n",
      "0      Alice   25       New York\n",
      "1        Bob   30  San Francisco\n",
      "2    Charlie   35    Los Angeles\n",
      "Mean age: 32.5\n",
      "  first_name           City\n",
      "0      Alice       New York\n",
      "1        Bob  San Francisco\n",
      "2    Charlie    Los Angeles\n",
      "3      David        Chicago\n",
      "  first_name  age           City  Salary\n",
      "0      Alice   25       New York     702\n",
      "1        Bob   30  San Francisco     308\n",
      "2    Charlie   35    Los Angeles     964\n",
      "3      David   40        Chicago     450\n",
      "             age      Salary\n",
      "count   4.000000    4.000000\n",
      "mean   32.500000  606.000000\n",
      "std     6.454972  288.975201\n",
      "min    25.000000  308.000000\n",
      "25%    28.750000  414.500000\n",
      "50%    32.500000  576.000000\n",
      "75%    36.250000  767.500000\n",
      "max    40.000000  964.000000\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd \n",
    "import numpy as np\n",
    "\n",
    "data = {\n",
    "    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],\n",
    "    'Age': [25, 30, 35, 40],\n",
    "    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']\n",
    "}\n",
    "\n",
    "df = pd.DataFrame(data)\n",
    "\n",
    "\n",
    "df.rename(columns={'First Name':'first_name', 'Age':'age'}, inplace=True)\n",
    "print(df)\n",
    "\n",
    "print(df.head(3))\n",
    "\n",
    "mean_age = df['age'].mean()\n",
    "print(\"Mean age:\",mean_age)\n",
    "\n",
    "print(df[['first_name','City']])\n",
    "\n",
    "df['Salary'] = np.random.randint(100,1000,size=len(df))\n",
    "print(df)\n",
    "\n",
    "\n",
    "print(df.describe())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "66a74fa0",
   "metadata": {},
   "source": [
    "Homework 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "26adb41d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  Month  Sales  Expenses\n",
      "0   Jan   5000      3000\n",
      "1   Feb   6000      3500\n",
      "2   Mar   7500      4000\n",
      "3   Apr   8000      4500\n",
      "Max sales: 8000\n",
      "Max expenses: 4500\n",
      "Min sales: 5000\n",
      "Min expenses: 3000\n",
      "Mean sales: 6625.0\n",
      "Mean expenses: 3750.0\n"
     ]
    }
   ],
   "source": [
    "data = {\n",
    "    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],\n",
    "    'Sales': [5000, 6000, 7500, 8000],\n",
    "    'Expenses': [3000, 3500, 4000, 4500]\n",
    "}\n",
    "\n",
    "sales_and_expenses = pd.DataFrame(data)\n",
    "print(sales_and_expenses)\n",
    "\n",
    "max_sales = sales_and_expenses['Sales'].max()\n",
    "max_expenses = sales_and_expenses['Expenses'].max()\n",
    "\n",
    "print('Max sales:',max_sales)\n",
    "print('Max expenses:',max_expenses)\n",
    "\n",
    "min_sales = sales_and_expenses['Sales'].min()\n",
    "min_expenses = sales_and_expenses['Expenses'].min()\n",
    "\n",
    "print('Min sales:',min_sales)\n",
    "print('Min expenses:',min_expenses)\n",
    "\n",
    "avg_sales = sales_and_expenses['Sales'].mean()\n",
    "avg_expenses = sales_and_expenses['Expenses'].mean()\n",
    "\n",
    "print('Mean sales:',avg_sales)\n",
    "print('Mean expenses:',avg_expenses)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cb8a51f8",
   "metadata": {},
   "source": [
    "Homework 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "e11b0f6b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Maximum expense for each category\n",
      "Category\n",
      "Rent             1500\n",
      "Utilities         250\n",
      "Groceries         350\n",
      "Entertainment     180\n",
      "dtype: int64\n",
      "\n",
      "Minimum expense for each category\n",
      "Category\n",
      "Rent             1200\n",
      "Utilities         200\n",
      "Groceries         300\n",
      "Entertainment     150\n",
      "dtype: int64\n",
      "\n",
      "Average expense for each category\n",
      "Category\n",
      "Rent             1350.0\n",
      "Utilities         227.5\n",
      "Groceries         325.0\n",
      "Entertainment     165.0\n",
      "dtype: float64\n",
      "\n"
     ]
    }
   ],
   "source": [
    "data = {\n",
    "    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],\n",
    "    'January': [1200, 200, 300, 150],\n",
    "    'February': [1300, 220, 320, 160],\n",
    "    'March': [1400, 240, 330, 170],\n",
    "    'April': [1500, 250, 350, 180]\n",
    "}\n",
    "\n",
    "expenses = pd.DataFrame(data)\n",
    "\n",
    "expenses = expenses.set_index('Category')\n",
    "\n",
    "max_expense = expenses.max(axis=1)\n",
    "print('Maximum expense for each category')\n",
    "print(max_expense)\n",
    "print()\n",
    "\n",
    "min_expense = expenses.min(axis=1)\n",
    "print('Minimum expense for each category')\n",
    "print(min_expense)\n",
    "print()\n",
    "\n",
    "avg_expense = expenses.mean(axis=1)\n",
    "print('Average expense for each category')\n",
    "print(avg_expense)\n",
    "print()\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "99816ff7",
   "metadata": {},
   "outputs": [],
   "source": []
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
