# importing packages
import pandas as pd 
import numpy as pd

# creating variables
age = 22
print(age)

name = "Janna Muryawan"
print(name)

grades_list = [88, 92, 95, 98, 100]
print(grades_list)

my_dict = {
    "name": "Janna",
    "ethnicity": "Indonesian",
    "hobbies": ["baking", "hiking", "gaming"],
    "address": {
        "street": "63 Jewel Avenue",
        "city": "Great Neck",
        "zipcode": "54321"
    }
}
print(my_dict)

# creating a function
def calculate_grade(grade1, grade2):
    avg_grade = (grade1 + grade2) / 2
    if avg_grade >= 70:
        return "You have passed your ahi classes for the summer semester, congrats!"
    else:
        return "You did not pass your ahi classes. Try again next summer!"

# two different outputs based on the same function
print(calculate_grade(95,68))
print(calculate_grade(46,71))

## note: chatgpt was helpful in double-checking the structures of my variables and functions quickly when I wasn't sure if I did it correctly 