{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "a1c3184c",
   "metadata": {},
   "source": [
    "\n",
    "1. Create a new database with a table named Roster that has three fields: Name, Species, and Age. The Name and Species columns should be text fields, and the Age column should be an integer field."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "47c6a140",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Table Roster is created successfully!\n"
     ]
    }
   ],
   "source": [
    "import sqlite3\n",
    "\n",
    "conn = sqlite3.connect(\"Pets.db\")\n",
    "cur = conn.cursor()\n",
    "\n",
    "cur.execute(\n",
    "\n",
    "    \"\"\"CREATE table roster(\n",
    "           Name TEXT,\n",
    "           Species TEXT,\n",
    "           Age INTEGER\n",
    "    )\"\"\"\n",
    ")\n",
    "\n",
    "print(\"Table Roster is created successfully!\")\n",
    "\n",
    "\n",
    "cur.executemany(\"\"\"\n",
    "INSERT INTO Roster (Name, Species, Age)\n",
    "VALUES (?, ?, ?)\n",
    "\"\"\", [\n",
    "    ('Benjamin Sisko', 'Human', 40),\n",
    "    ('Jadzia Dax', 'Trill', 300),\n",
    "    ('Kira Nerys', 'Bajoran', 29)\n",
    "])\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "conn.commit()\n",
    "conn.close()\n",
    " \n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b8d6f849",
   "metadata": {},
   "source": [
    "3. Update the Name of Jadzia Dax to be Ezri Dax"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "311adaea",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Name updated successfully!\n"
     ]
    }
   ],
   "source": [
    "import sqlite3\n",
    "\n",
    "conn = sqlite3.connect(\"Pets.db\")\n",
    "cur = conn.cursor()\n",
    "\n",
    "cur.execute(\"\"\"\n",
    "    UPDATE Roster\n",
    "    SET Name = 'Ezri Dax'\n",
    "    where name = 'Jadzia Dax'\n",
    "\"\"\")\n",
    "\n",
    "conn.commit()\n",
    "conn.close()\n",
    "\n",
    "print(\"Name updated successfully!\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7ededad5",
   "metadata": {},
   "source": [
    "4. Display the Name and Age of everyone in the table classified as Bajoran."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "af1d84dc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Name: Kira Nerys, Age: 29\n"
     ]
    }
   ],
   "source": [
    "import sqlite3\n",
    "\n",
    "conn = sqlite3.connect(\"Pets.db\")\n",
    "cur = conn.cursor()\n",
    "\n",
    "cur.execute(\"SELECT Name, Age from Roster where Species = 'Bajoran'\")\n",
    "results = cur.fetchall()\n",
    "\n",
    "for name, age in results:\n",
    "    print(f\"Name: {name}, Age: {age}\")\n",
    "\n",
    "conn.close()\n",
    "\n"
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
