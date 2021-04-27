"""
created by Nagaj at 23/04/2021
"""

# https://holypython.com/100-python-tips-tricks/
import os
import pprint
import time


def make_terminal_clean(symbol="#", times=100, lines_after=2):
    print(symbol * times, end="\n" * lines_after)


# 1) print(\a): (Make print sing)
# import antigravity

# #########################################

# 2) DICTIONARY MERGE: (PYTHON SYNTAX SHOW OFF)

clean_code = {
    "title": "Clean Code For Software Development",
    "author": "Bob",
    "published": "2007",
}

blog = {"title": "Django Framework", "blogger": "James"}

book_and_blog = {**clean_code, **blog}
print(book_and_blog)

# ######################################################

clean_code.update(blog)
print(clean_code)

# ######################################################
clean_code.update(**blog)
print(clean_code)

# ######################################################

clean_code.update(page=400, price="10$")

print(clean_code)

# ######################################################

# 4) BIG NUMBER READABILITY: (MILLIONS AND BILLIONS)

views = 1_000_000
print(f"Channel Views: {views}")
views_by_day = views + 1000
print(f"Views BY Day {views_by_day}")

# #######################################################

# 6) CHAIN OPERATORS: (LARGER THAN AND SMALLER THAN)

your_speed = 160

MIN_SPEED = 50
MAX_SPEED = 120

is_safe = MIN_SPEED < your_speed < MAX_SPEED

print(f"Your Speed Is Safe ?? {is_safe}")

# ########################################################
# 7) PRETTY PRINT: (PPRINT)

pprint.pprint(clean_code, indent=4)

make_terminal_clean(times=100)

location = {
    "place_id": 259174015,
    "licence": "Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright",
    "osm_type": "way",
    "osm_id": 12316939,
    "boundingbox": [
        "42.983431438214",
        "42.983531438214",
        "-78.706880444495",
        "-78.706780444495",
    ],
    "lat": "42.983481438214326",
    "lon": "-78.70683044449504",
    "display_name": """230, Fifth Avenue,
        Sheridan Meadows, Amherst Town, Erie County, New York, 14221, United States of America""",
    "class": "place",
    "type": "house",
    "importance": 0.511,
}

pprint.pprint(location, indent=3)

make_terminal_clean(times=100)
# ##########################################################

# 8) GETTING RID OF UNWANTED CHARACTERS: (LEFT STRIP, RIGHT STRIP AND JUST STRIP)

welcome = "    Hello World    "

print(welcome)
print(welcome.strip())  # remove all white spaces (right & left)
print(welcome.rstrip())  # remove right white spaces
print(welcome.lstrip())  # remove left white spaces

make_terminal_clean(times=100)
# ##########################################################

# 9) MERGING STRINGS: (JOIN METHOD)

servers = ["10.90.80.20", "10.70.21.6", "10.30.40.9"]

db_servers = "||".join(servers)
print(db_servers)

make_terminal_clean(times=100)
# ##########################################################

# 10) VERSATILE ARITHMETIC OPERATORS: (MULTIPLY LISTS & ADD STRINGS) متعدد الجوانب
welcome = "Hello World " * 2
print(welcome)

order = ["Mac Book Pro", "Iphone 12", "Apple Smart Watch"]

FAMILY_MEMBERS = 3

print(order * FAMILY_MEMBERS)

make_terminal_clean(times=100)
# ##########################################################

# 11) FLOOR DIVISION: (KEEP THE CHANGE)

SALARY = 1000
DAYS = 30
salary_per_day = SALARY // DAYS
print(salary_per_day)
salary_per_day = SALARY / DAYS
print(salary_per_day)

# ##########################################################
# 12) Negative Indexing: (Accessing from the end)

lines = ("Alex", "Smart Village", "Zayed", "October", "Valley")

print(lines)

print(lines[0])  # first line
print(lines[-1])  # last line

print(lines[1:3])  # smart-zayed
print(lines[1:4])  # smart-zayed-october

# #############################################

# 13) Break up strings: (Split Method)

text = "Python Is Cool"
print(text)

words = text.split()
print(words)

emails: str = "john@test.com;leon@test.com;james@test.com"

emails: list = emails.split(";")

print(emails)
print(emails[-1])
print(emails[::-1])


# ############################################

# 14) When the code is too fast: (Make Python Sleep)
# count down


def downcount(seconds):
    for i in range(1, seconds + 1):
        print(i)
        time.sleep(1)


# 15) Reverse data: (Slice Notation)

name = "John"
print(name, name[::-1])

# 16) Reverse data: (Reversed Function & Reverse Method)

days = ["Sa", "Sun", "Mon", "Tue", "Wen", "Thur", "Fri"]

print(days)
days.reverse()
print(days)

days.sort(reverse=True)
print(days)

# #######################################################

# using join

blood_types = ("A", "A+", "B", "B+", "AB", "AB+", "O", "O+")

print(blood_types)
print(";".join(blood_types))

# ######################################################


# 17) Multi Assignments: (One-Liner)

subjects = ["Arabic", "English", "Math"]

# ar, en = subjects  # ValueError: too many values to unpack (expected 2)
ar, en = subjects[:2]
print(ar)
print(en)
# print(math)

ar, en, math = subjects
print(ar)
print(en)
print(math)

make_terminal_clean()

# ########################################################################

# 19) Remove Duplicates: (set function)

names = ["John", "Leon", "James", "Smith", "Sara", "John"]
team = ["Lean", "James"]

print(set(names))
unique = []
for name in names:
    if name not in unique:
        unique.append(name)

print(unique)

make_terminal_clean()

# 20) Python Working Directory: (os.getcwd())
print(os.getcwd())
print(os.path.join(os.getcwd(), __file__))

print(os.path.basename(os.path.join(os.getcwd(), __file__)))
print(os.path.dirname(os.path.join(os.getcwd(), __file__)))

make_terminal_clean()
# #########################################################################

# 20) Python Working Directory: (os.chdir())
os.chdir(f"c:\\users\\{os.getlogin()}\\Desktop")


print(os.getcwd())

with open("test.txt", "w") as f:
    f.write("testing")