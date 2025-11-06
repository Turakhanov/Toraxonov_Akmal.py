{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "78dde7cc",
   "metadata": {},
   "source": [
    "1. Task: JSON Parsing\n",
    "write a Python script that reads the students.jon JSON file and prints details of each student."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "03ba52f9",
   "metadata": {},
   "outputs": [],
   "source": [
    "import json\n",
    "\n",
    "with open(r\"C:\\Users\\Asus\\Documents\\Visual Studio 2017\\MAAB\\Python\\Datasets\\students.json\",\"r\") as file:\n",
    "    students = json.load(file)\n",
    "\n",
    "\n",
    "for s in students:\n",
    "    print(\"Name: \", s[\"name\"])\n",
    "    print(\"Age:\", s[\"age\"])\n",
    "    print(\"Major\", s[\"major\"])\n",
    "    print(\"-\"*20)\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c52dcb11",
   "metadata": {},
   "source": [
    "2. Task: Weather API\n",
    "Use this url : https://openweathermap.org/\n",
    "Use the requests library to fetch weather data for a specific city(ex. your hometown: Tashkent) and print relevant information (temperature, humidity, etc.)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "02f689e7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "City not found or API error:  Invalid API key. Please see https://openweathermap.org/faq#error401 for more info.\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "\n",
    "api_key = \"fc50fac22d2ba82c4787d0632e180a64\"\n",
    "\n",
    "city = input(\"Enter city name:\")\n",
    "url = \"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric\"\n",
    "response = requests.get(url)\n",
    "data = response.json()\n",
    "\n",
    "if data[\"cod\"] != 200:\n",
    "    print(\"City not found or API error: \", data[\"message\"])\n",
    "else:\n",
    "    temperature = data[\"main\"][\"temp\"]\n",
    "    humidity = data[\"main\"][\"humidity\"]\n",
    "    weather_desc = data[\"weather\"][0][\"description\"]\n",
    "    wind_speed = data[\"wind\"][\"speed\"]\n",
    "\n",
    "    print(\"Weather in city: \", city)\n",
    "    print(\"Temperature: \", temperature,\"C\")\n",
    "    print(\"Humidity: \", humidity,\"%\")\n",
    "    print(\"Weather description: \", weather_desc)\n",
    "    print(\"Wind speed: \",wind_speed,\"m/s\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6fb4a009",
   "metadata": {},
   "source": [
    "3. Task: JSON Modification\n",
    "Write a program that allows users to add new books, update existing book information, and delete books from the books.json JSON file.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "71c2a3fa",
   "metadata": {},
   "outputs": [],
   "source": [
    "import json\n",
    "import os\n",
    "\n",
    "if os.path.exists(\"books.json\"):\n",
    "    with open(\"books.json\",\"r\") as file:\n",
    "        books = json.load(file)\n",
    "else:\n",
    "    books = []\n",
    "\n",
    "def add_book():\n",
    "    title = input(\"Enter book title:\")\n",
    "    author = input(\"Enter book author:\")\n",
    "    year = int(input(\"Enter publication year:\"))\n",
    "    books.append({\"title\":title, \"author\":author, \"year\":year})\n",
    "    print(f\"{title} added successfully!\")\n",
    "\n",
    "def update_book():\n",
    "    title = input(\"Enter the title of the book to update:\")\n",
    "    for book in books:\n",
    "        if book[\"title\"].lower()==title.lower():\n",
    "            book[\"author\"] = input(\"Enter new author:\")\n",
    "            book[\"year\"] = input(\"Enter new publication year\")\n",
    "            print(f\"{title} is updated successfully!\")\n",
    "\n",
    "def delete_book():\n",
    "    title = input(\"Enter the title of the book to delete: \")\n",
    "    for i, book in enumerate(books):\n",
    "        if book[\"title\"].lower() == title.lower():\n",
    "            books.pop(i)\n",
    "            print(f\"{title} is deleted successfully\")\n",
    "\n",
    "def menu():\n",
    "    if not books:\n",
    "        print(\"No books available!\")\n",
    "        return\n",
    "    print(\"\\n List of books\")\n",
    "    for book in books:\n",
    "        print(f\"Book title: {book['title']}, Author: {book['author']}, Year: {book['year']}.\")\n",
    "\n",
    "def save_books():\n",
    "    with open(\"books.json\",\"w\") as file:\n",
    "        json.dump(books,file,indent=4)\n",
    "\n",
    "\n",
    "while True:\n",
    "    print(\"\\n--- Book Manager ---\")\n",
    "    print(\"1. Show all books\")\n",
    "    print(\"2. Add a book\")\n",
    "    print(\"3. Update a book\")\n",
    "    print(\"4. Delete a book\")\n",
    "    print(\"5. Exit\")\n",
    "    \n",
    "    choice = input(\"Enter your choice: \")\n",
    "    \n",
    "    if choice == \"1\":\n",
    "        menu()\n",
    "    elif choice == \"2\":\n",
    "        add_book()\n",
    "        save_books()\n",
    "    elif choice == \"3\":\n",
    "        update_book()\n",
    "        save_books()\n",
    "    elif choice == \"4\":\n",
    "        delete_book()\n",
    "        save_books()\n",
    "    elif choice == \"5\":\n",
    "        print(\"Exiting program...\")\n",
    "        break\n",
    "    else:\n",
    "        print(\"Invalid choice. Please try again.\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c53a9fb9",
   "metadata": {},
   "source": [
    "4. Task: Movie Recommendation System\n",
    "Use this url http://www.omdbapi.com/ to fetch information about movies.\n",
    "Create a program that asks users for a movie genre and recommends a random movie from that genre."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "d5458a7a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "🎬 Recommended Movie for Genre: Action\n",
      "Title: Affurmative Action\n",
      "Year: 2019\n",
      "Genre: Documentary, Short, Comedy\n",
      "IMDB Rating: 5.4\n",
      "Plot: An exploration of workplace diversity through \"meet the team\" pages.\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "import random\n",
    "\n",
    "api_key = \"2bfa6205\"\n",
    "genre = input(\"Enter movie genre (Action, Drama, Horror): \").capitalize()\n",
    "movies = []\n",
    "\n",
    "for year in range(2010,2025):\n",
    "    url = f\"http://www.omdbapi.com/?apikey={api_key}&type=movie&y={year}&s={genre}\"\n",
    "    response = requests.get(url)\n",
    "    data = response.json()\n",
    "\n",
    "    if data.get(\"Search\"):\n",
    "        movies.extend(data[\"Search\"])\n",
    "\n",
    "if not movies:\n",
    "    print(\"No movies found on this genre. Try another one!\")\n",
    "\n",
    "else:\n",
    "    movie = random.choice(movies)\n",
    "    movie_title = movie[\"Title\"]\n",
    "    imdb_id = movie[\"imdbID\"]\n",
    "    \n",
    "\n",
    "    details_url = f\"http://www.omdbapi.com/?apikey={api_key}&i={imdb_id}\"\n",
    "    details_response = requests.get(details_url)\n",
    "    details = details_response.json()\n",
    "\n",
    "    print(f\"\\n🎬 Recommended Movie for Genre: {genre}\")\n",
    "    print(f\"Title: {details['Title']}\")\n",
    "    print(f\"Year: {details['Year']}\")\n",
    "    print(f\"Genre: {details['Genre']}\")\n",
    "    print(f\"IMDB Rating: {details['imdbRating']}\")\n",
    "    print(f\"Plot: {details['Plot']}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cdad6784",
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
