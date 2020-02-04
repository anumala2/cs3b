###############################################
# CS 21B Intermediate Python Programming Lab #1
# Topics: Arithmetic, Data Types, User Input,
#         Formatting Output, Importing Modules
# Description: This program uses user input of
#              last name and student number to
#              calculate some interesting
#              expressions and print them out,
#              allowing us to see the properties
#              of ints in python (for instance,
#              as a boolean, or for rounding or
#              absolute value).
# User Input: name and student ID
# Output: expression results as per lab spec.
# Version: 3.7.0
# Development Environment:  IDLE
# Developer:  Aadithya Anumala
# Student ID: 20365071
# Date:  04/16/19
###############################################

# importing date from datetime package to print at end
from datetime import date
print("\n\n")

# receiving family name from user
fname = 0
while type(fname) != str or len(fname) < 2 or len(fname) > 15:
    fname = input("Enter your family name: ")
fname = str(fname)

# receiving student id from user
stud = '#'
while (not stud.isdigit()) or len(stud) != 8:
    stud = input("Enter your student ID: ")
stud = int(stud)

# finding my_id and n_let from fname and stud
my_id = 0
while stud:
    my_id, stud = my_id + stud % 10, stud // 10
my_id = int(my_id)
n_let = int(len(fname))

# calculating the third expression value
three = 0
i = 2
while i <= n_let:
    three = three+i
    i = i+1

# printing of my_id and n_let
print("my_id is: " + str(my_id))
print("n_let is: " + str(n_let))

# printing of given expressions
print("expression 1: " + str(my_id / 2))
print("expression 2: " + str(my_id % 2))
print("expression 3: " + str(three))
print("expression 4: " + str(my_id + n_let))
print("expression 5: " + str(abs(n_let - my_id)))           
print("expression 6: " + str((my_id) / (n_let + 1100)))
print("expression 7: " + str((n_let % n_let) and (my_id * my_id)))
print("expression 8: " + str(1 or (my_id / 0)))
print("expression 9: " + str(round(3.15, 1)))
print("\n")
print("Today's date is " + str(date.today()))
print("\n")

# test run
"""
 RESTART: /Users/aadianumala/Documents/CollegeCompSci/CS3B/aadithyaAnumalaLab1.py 



Enter your family name: Student
Enter your student ID: 12345678
my_id is: 36
n_let is: 7
expression 1: 18.0
expression 2: 0
expression 3: 27
expression 4: 43
expression 5: 29
expression 6: 0.032520325203252036
expression 7: 0
expression 8: 1
expression 9: 3.1


Today's date is 2019-04-16


>>> 
"""
