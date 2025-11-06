{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "5dae6b83",
   "metadata": {},
   "source": [
    "[datetime] = 2025-10-16 23:00:00\n",
    "[date] = 2025-10-16\n",
    "[timedelta] = represents time difference between two dates or times\n",
    "\n",
    "# Creating my own date or datetime\n",
    "\n",
    "birthday = datetime(2008,03,30,10,30) --> year, month, day, hour, minute\n",
    "\n",
    "# The [timedelta] class lets you move time forward or backward.\n",
    "\n",
    "        tomorrow = now + timedelta(days=1)\n",
    "        yesterday = now - timedelta(days=1)\n",
    "        print(tomorrow, yesterday)\n",
    "\n",
    "# [strftime()] converts a datetime into a readable format:\n",
    "\n",
    "        print(now.strftime(\"%Y-%m-%d %H:%M:%S\"))\n",
    "\n",
    "\n",
    "        date_str = \"2008-07-15\"\n",
    "        birthday = datetime.strptime(date_str, \"%Y-%m-%d\")\n",
    "\n",
    "\n",
    "## Timezones and the pytz Module\n",
    "\n",
    "To handle time differences between countries, we use the [pytz] module.\n",
    "\n",
    "# List of available timezones:\n",
    "        \n",
    "        for tz in pytz.all_timezones[:10]:  # just show first 10\n",
    "        print(tz)\n",
    "\n",
    "\n",
    "# Get current time in a specific timezone:\n",
    "\n",
    "        tz_uz = pytz.timezone('Asia/Tashkent')\n",
    "        now_uz = datetime.now(tz_uz)\n",
    "        print(\"Uzbekistan:\", now_uz)\n",
    "\n",
    "\n",
    "# Converting time from one timezone to another:\n",
    "        tz_us = pytz.timezone('America/New_York')\n",
    "        now_us = now_uz.astimezone(tz_us)\n",
    "        print(\"New York:\", now_us)\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5a0ec017",
   "metadata": {},
   "source": [
    "| Pattern | Meaning                        | Example Match                                     |\n",
    "| ------- | ------------------------------ | ------------------------------------------------- |\n",
    "| `\\d`    | digit (0–9)                    | 5                                                 |\n",
    "| `\\w`    | letter, digit, or underscore   | A, b, 1, _                                        |\n",
    "| `.`     | any character (except newline) | a, #, 3                                           |\n",
    "| `+`     | one or more times              | \\d+ → 123, 5                                      |\n",
    "| `*`     | zero or more times             | \\d* → \"\", \"12\"                                    |\n",
    "| `?`     | zero or one time               | colou?r → color or colour                         |\n",
    "| `^`     | start of string                | ^Hello → matches only if text starts with “Hello” |\n",
    "| `$`     | end of string                  | world$ → matches if text ends with “world”        |\n",
    "| `[]`    | character set                  | [A-Z] → any uppercase letter                      |\n",
    "| `{n,m}` | repeat n–m times               | \\d{4} → 4 digits                                  |\n",
    "| `()`    | group of characters            | (\\d{2})-(\\d{2})-(\\d{4})                           |\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d1ba1f0e",
   "metadata": {},
   "source": [
    "The 4 Main Functions:\n",
    "\n",
    "re.match(pattern, text)\n",
    "    Checks if the beginning of the text matches the pattern.\n",
    "        re.match(r\"cat\", \"catfish\")  # ✅\n",
    "        re.match(r\"fish\", \"catfish\") # ❌\n",
    "\n",
    "re.search(pattern, text)\n",
    "    Finds the first match anywhere in the text.\n",
    "        re.search(r\"fish\", \"catfish\")  # ✅ found at the end\n",
    "\n",
    "re.findall(pattern, text)\n",
    "    Finds all matches and returns them as a list.\n",
    "        re.findall(r\"\\d+\", \"There are 3 cats and 15 dogs\")\n",
    "        # → ['3', '15']\n",
    "\n",
    "re.sub(pattern, replacement, text)\n",
    "    Replaces all matches with something else.\n",
    "        re.sub(r\"\\d\", \"*\", \"My number is 12345\")\n",
    "        # → 'My number is *****'"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6b372bc9",
   "metadata": {},
   "source": [
    "| Method               | Description                       | Example                                       |\n",
    "| -------------------- | --------------------------------- | --------------------------------------------- |\n",
    "| `.lower()`           | All lowercase                     | `\"HELLO\".lower()` → `\"hello\"`                 |\n",
    "| `.upper()`           | All uppercase                     | `\"hi\".upper()` → `\"HI\"`                       |\n",
    "| `.title()`           | Capitalize each word              | `\"data science\".title()` → `\"Data Science\"`   |\n",
    "| `.strip()`           | Remove spaces from both sides     | `\"  hello  \".strip()` → `\"hello\"`             |\n",
    "| `.replace(old, new)` | Replace words                     | `\"hi cat\".replace(\"cat\", \"dog\")` → `\"hi dog\"` |\n",
    "| `.startswith()`      | Checks start                      | `\"Python\".startswith(\"Py\")` → `True`          |\n",
    "| `.endswith()`        | Checks end                        | `\"test.txt\".endswith(\".txt\")` → `True`        |\n",
    "| `.find()`            | Returns index of first occurrence | `\"banana\".find(\"a\")` → `1`                    |\n",
    "| `.count()`           | Counts occurrences                | `\"banana\".count(\"a\")` → `3`                   |\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4fced6ff",
   "metadata": {},
   "source": [
    "| Symbol  | Meaning         | Example                         |\n",
    "| ------- | --------------- | ------------------------------- |\n",
    "| `+`     | one or more     | `\\d+` → “15” ✅                  |\n",
    "| `*`     | zero or more    | `\\d*` → \"\", \"123\" ✅             |\n",
    "| `?`     | zero or one     | `colou?r` → “color”, “colour” ✅ |\n",
    "| `{n}`   | exactly n       | `\\d{4}` → “2025” ✅              |\n",
    "| `{n,m}` | between n and m | `\\d{2,4}` → “25”, “2025” ✅      |\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "199491d5",
   "metadata": {},
   "source": [
    "| Symbol | Meaning       | Example                                           |\n",
    "| ------ | ------------- | ------------------------------------------------- |\n",
    "| `^`    | start of text | `^Hello` matches only if text starts with “Hello” |\n",
    "| `$`    | end of text   | `world$` matches only if text ends with “world”   |\n",
    "| `\\b`   | word boundary | `\\bcat\\b` matches “cat” but not “catfish”         |\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e89e5c59",
   "metadata": {},
   "source": [
    "| Pattern    | Meaning          | Matches   |\n",
    "| ---------- | ---------------- | --------- |\n",
    "| `[A-Z]`    | uppercase letter | A, B, C … |\n",
    "| `[a-z]`    | lowercase letter | a, b, c … |\n",
    "| `[0-9]`    | digit            | 0–9       |\n",
    "| `[A-Za-z]` | any letter       | A, b, X   |\n",
    "| `[^0-9]`   | NOT a digit      | a, !, -   |\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "006ec398",
   "metadata": {},
   "source": [
    "1. Age Calculator: Ask the user to enter their birthdate. Calculate and print their age in years, months, and days.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "513fbfd7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You are 17 years, 6 months and 18 days\n"
     ]
    }
   ],
   "source": [
    "from datetime import datetime, date, timedelta\n",
    "\n",
    "n = input(\"Enter your birth date: \\n\"\n",
    "                        \",for example(YY-MM-DD)\")\n",
    "\n",
    "bdate = datetime.strptime(n,\"%Y-%m-%d\").date()\n",
    "\n",
    "today = date.today()\n",
    "\n",
    "years = today.year - bdate.year\n",
    "months = today.month - bdate.month\n",
    "days = today.day - bdate.day\n",
    "\n",
    "if days < 0:\n",
    "        months -= 1\n",
    "        last_month = (today.replace(day=1) - timedelta(days=1)).day\n",
    "        days += last_month\n",
    "\n",
    "if months < 0:\n",
    "        years -= 1\n",
    "        months += 12\n",
    "\n",
    "print(f\"You are {years} years, {months} months and {days} days\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9fa47fc2",
   "metadata": {},
   "source": [
    "2. Days Until Next Birthday: Similar to the first exercise, but this time, calculate and print the number of days remaining until the user's next birthday.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "c6ef734d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "There are 163 days until your next birthday\n"
     ]
    }
   ],
   "source": [
    "from datetime import datetime, date\n",
    "\n",
    "n = input(\"Enter your birth date: \\n\"\n",
    "                        \",for example(YY-MM-DD)\")\n",
    "\n",
    "bdate = datetime.strptime(n,\"%Y-%m-%d\").date()\n",
    "\n",
    "today = date.today()\n",
    "\n",
    "next_bdate = date(today.year, bdate.month, bdate.day)\n",
    "\n",
    "if next_bdate < today:\n",
    "    next_bdate = date(today.year+1, bdate.month, bdate.day)\n",
    "\n",
    "days_remain = (next_bdate-today).days\n",
    "\n",
    "print(f\"There are {days_remain} days until your next birthday\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "48a48b9b",
   "metadata": {},
   "source": [
    "3. Meeting Scheduler: Ask the user to enter the current date and time, as well as the duration of a meeting in hours and minutes. Calculate and print the date and time when the meeting will end.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1e9f8fd1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Meeting will end on 2025-10-06 04:00\n"
     ]
    }
   ],
   "source": [
    "from datetime import datetime, timedelta\n",
    "\n",
    "current_date_str = input(\"Enter current date and time (YY-MM-DD HH:MM):\\n\")\n",
    "current_datetime = datetime.strptime(current_date_str, \"%Y-%m-%d %H:%M\")\n",
    "\n",
    "duration_h = int(input(\"Enter meeting duration hour: \\n\"))\n",
    "duration_m = int(input(\"Enter meeting duration minutes \\n\"))\n",
    "\n",
    "meeting_duration = timedelta(hours=duration_h, minutes=duration_m)\n",
    "end_datetime = current_datetime + meeting_duration\n",
    "\n",
    "print(f\"Meeting will end on {end_datetime.strftime(\"%Y-%m-%d %H:%M\")}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "792aab32",
   "metadata": {},
   "source": [
    "4. Timezone Converter: Create a program that allows the user to enter a date and time along with their current timezone, and then convert and print the date and time in another timezone of their choice.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "2f3dbe34",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The time in Europe/London will be 2025-11-05 23:04\n"
     ]
    }
   ],
   "source": [
    "from datetime import datetime\n",
    "from zoneinfo import ZoneInfo\n",
    "import tzdata\n",
    "\n",
    "date_str = input(\"Enter the date and time (YYYY-MM-DD HH:MM)\")\n",
    "local_datetime = datetime.strptime(date_str,\"%Y-%m-%d %H:%M\")\n",
    "\n",
    "current_tz = input(\"Enter current timezone (e.g., Asia/Tashkent): \")\n",
    "target_tz = input(\"Enter target timezone (e.g., America/NewYork) \")\n",
    "\n",
    "local_datetime = local_datetime.replace(tzinfo=ZoneInfo(current_tz))\n",
    "target_datetime = local_datetime.astimezone(ZoneInfo(target_tz))\n",
    "\n",
    "print(f\"The time in {target_tz} will be {target_datetime.strftime('%Y-%m-%d %H:%M')}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ac18d42d",
   "metadata": {},
   "source": [
    "5. Countdown Timer: Implement a countdown timer. Ask the user to input a future date and time, and then continuously print the time remaining until that point in regular intervals (e.g., every second).\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7e245dcb",
   "metadata": {},
   "outputs": [],
   "source": [
    "from datetime import datetime\n",
    "import time\n",
    "\n",
    "target_str2 = input(\"Enter the target date and time (YYYY-MM-DD HH:MM):\")\n",
    "target_datetime2 = datetime.strptime(target_str2,\"%Y-%m-%d %H:%M\")\n",
    "\n",
    "while True:\n",
    "    current_datetime = datetime.now()\n",
    "    time_left = target_datetime2 - current_datetime\n",
    "\n",
    "    if time_left.total_seconds() <= 0:\n",
    "        print(\"Time is up!\")\n",
    "        break\n",
    "\n",
    "    days = time_left.days\n",
    "    seconds = time_left.seconds\n",
    "    hours = seconds//3600\n",
    "    minutes = (seconds % 3600) // 60\n",
    "    seconds = seconds % 60\n",
    "\n",
    "    print(f\"Time remaining: {days} days, {hours} hours, {minutes} minutes and {seconds} seconds\", end='\\r')\n",
    "    time.sleep(1)\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "10130fa5",
   "metadata": {},
   "source": [
    "6. Email Validator: Write a program that validates email addresses. Ask the user to input an email address, and check if it follows a valid email format.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "c883784a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Valid email\n"
     ]
    }
   ],
   "source": [
    "import re\n",
    "\n",
    "email = input(\"Enter your email: \")\n",
    "\n",
    "pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$'\n",
    "\n",
    "if re.match(pattern,email):\n",
    "    print(\"Valid email\")\n",
    "else:\n",
    "    print(\"Invalid email\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e69321e3",
   "metadata": {},
   "source": [
    "7. Phone Number Formatter: Create a program that takes a phone number as input and formats it according to a standard format. For example, convert \"1234567890\" to \"(123) 456-7890\".\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "3b6f07f5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Your phone number:  (97) 122-73-57\n"
     ]
    }
   ],
   "source": [
    "phone = input(\"Enter your 9 digit phone number: \")\n",
    "\n",
    "if len(phone) != 9 or not phone.isdigit():\n",
    "    print(\"Please enter valid 9 digit phone\")\n",
    "else:\n",
    "    mobile_code = phone[:2]\n",
    "    first_three = phone[2:5]\n",
    "    middle_two = phone[5:7]\n",
    "    last_two = phone[7:]\n",
    "\n",
    "    formatted_phone = f\"({mobile_code}) {first_three}-{middle_two}-{last_two}\"\n",
    "    print(\"Your phone number: \", formatted_phone)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9ef0fcf5",
   "metadata": {},
   "source": [
    "8. Password Strength Checker: Implement a password strength checker. Ask the user to input a password and check if it meets certain criteria (e.g., minimum length, contains at least one uppercase letter, one lowercase letter, and one digit).\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "e3e08051",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Strong Password!\n"
     ]
    }
   ],
   "source": [
    "password = input(\"Enter your password: \")\n",
    "\n",
    "if len(password) <8:\n",
    "    print(\"Weak password. Password must be atleast 8 characters long.\")\n",
    "elif not any(char.isupper() for char in password):\n",
    "    print(\"Weak password. Password must contain at least 1 uppercase letter.\")\n",
    "elif not any(char.islower() for char in password):\n",
    "    print(\"Weak password. Password must contain at least 1 lowercase letter.\")\n",
    "elif not any(char.isdigit() for char in password):\n",
    "    print(\"Weak password. Password must contain at least 1 digit.\")\n",
    "\n",
    "else:\n",
    "    print(\"Strong Password!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "01b5b2ce",
   "metadata": {},
   "source": [
    "9. Word Finder: Develop a program that finds all occurrences of a specific word in a given text. Ask the user to input a word, and then search for and print all occurrences of that word in a sample text.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "1d852b28",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The word: hard was not found!\n"
     ]
    }
   ],
   "source": [
    "sample_text = \"\"\"\n",
    "Python is a powerful programming language. \n",
    "Many developers use Python for web development, data analysis, and automation. \n",
    "Learning Python can be fun and rewarding.\n",
    "\"\"\"\n",
    "\n",
    "word_to_find = input(\"Enter the word to find: \").lower()\n",
    "\n",
    "words = sample_text.lower().split()\n",
    "occurences = [i for i, w in enumerate(words,start=1) if w.strip(\".,\") == word_to_find]\n",
    "\n",
    "if occurences:\n",
    "    print(f\"The word {word_to_find} was found at positions: {occurences}\")\n",
    "    print(f\"Total occurences: {len(occurences)}\")\n",
    "else:\n",
    "    print(f\"The word: {word_to_find} was not found!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d77af6a6",
   "metadata": {},
   "source": [
    "10. Date Extractor: Write a program that extracts dates from a given text. Ask the user to input a text, and then identify and print all the dates present in the text.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "d4c58e15",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Dates found in the text ['6/12/2024']\n"
     ]
    }
   ],
   "source": [
    "import re\n",
    "\n",
    "text = input(\"Enter your text:\")\n",
    "\n",
    "pattern = r'\\b\\d{1,2}[-/]\\d{1,2}[-/]\\d{4}\\b'\n",
    "\n",
    "dates = re.findall(pattern,text)\n",
    "\n",
    "if dates:\n",
    "    print(\"Dates found in the text\", dates)\n",
    "else:\n",
    "    print(\"No dates found!\")"
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
