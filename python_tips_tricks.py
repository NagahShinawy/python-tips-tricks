"""
created by Nagaj at 23/04/2021
"""

# https://holypython.com/100-python-tips-tricks/


import pprint


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

location = {'place_id': 259174015, 'licence': 'Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright',
            'osm_type': 'way', 'osm_id': 12316939,
            'boundingbox': ['42.983431438214', '42.983531438214', '-78.706880444495',
                            '-78.706780444495'], 'lat': '42.983481438214326', 'lon': '-78.70683044449504',
            'display_name': '''230, Fifth Avenue,
        Sheridan Meadows, Amherst Town, Erie County, New York, 14221, United States of America''',
            'class': 'place', 'type': 'house', 'importance': 0.511}

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
