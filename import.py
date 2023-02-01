# 2) Create a Module in VS Code and Import It into jupyter notebook
# Module should have the following capabilities:

# 1) Has a function to calculate the square footage of a house
# Reminder of Formula: Length X Width == Area

# 2) Has a function to calculate the circumference of a circle
# Program in Jupyter Notebook should take in user input and use imported functions to calculate a circle's circumference or a houses square footage


def find_area ():
    length = int(input('What is the length  of the house?'))
    width = int(input('What is the width of the house?'))
    area = length * width 
    return area    
print(find_area()) 


def find_circumference ():
    pie = 3.14
    radius = int(input('What is the radius of the circle?'))
    circ = 2 * pie * radius
    return circ
print(find_circumference())    