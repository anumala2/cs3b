###############################################
# CS 21B Intermediate Python Programming Lab #4
# Topics: input, lists, formatting
# Description: This program uses user input of a
#              date in mm/dd/yyyy and converts it
#              into a more readable format, by 
#              taking advantage of lists and 
#              string formatting. Furthermore, the
#              program ensures that the date
#              actually exists (e.g. Feb 29th on
#              non-leap years).
# Input: mm/dd/yyyy date
# Output: Month dd, yyyy format
# Version: 3.7.0
# Development Environment:  IDLE
# Developer:  Aadithya Anumala
# Student ID: 20365071
# Date:  05/07/19
###############################################

#some constants
MIN_YEAR = 1000
MAX_YEAR = 2999
LEAP_DAY = 29
LEAP_MONTH = 2
ONE_DIGIT = 9
MO_INDEX = 2
DAY_IND_ONE = 3
DAY_IND_TWO = 5
YEAR_IND = 6

#getting user input
ori = input("Enter a date (mm/dd/yyyy): ")

#trying to convert to ints - if impossible, invalid input
try:
    moNo = ori[:MO_INDEX]
    daNo = ori[DAY_IND_ONE:DAY_IND_TWO]
    yeNo = ori[YEAR_IND:]
    
    moNo = int(moNo)
    daNo = int(daNo)
    yeNo = int(yeNo)
except:
    print("Invalid Input.")
    raise SystemExit

#list of months
months = ["January", "February", "March", "April", "May",\
          "June", "July", "August", "September", "October",
          "November", "December"]
month = months[moNo-1]

#list of number of days in each month
days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#conditions for date actually existing
if yeNo > MAX_YEAR or yeNo < MIN_YEAR:
    print("Not in year range.")
    raise SystemExit
if daNo > days[moNo-1]:
    print("That day doesn't exist.")
    raise SystemExit
if moNo == LEAP_MONTH and yeNo%4 != 0 and daNo == LEAP_DAY:
    print("This isn't a leap year.")
    raise SystemExit

#format printing
if daNo > ONE_DIGIT:
    print("The converted date is:", month, str(daNo) + ", " + str(yeNo))
else:
    print("The converted date is:", month + " 0" + str(daNo) + ", " \
          + str(yeNo))

"""
RESTART: /Users/aadianumala/Documents/CollegeCompSci/CS3B/aadithyaAnumalaLab4.py 
Enter a date (mm/dd/yyyy): 05/07/2019
The converted date is: May 07, 2019
>>> 
RESTART: /Users/aadianumala/Documents/CollegeCompSci/CS3B/aadithyaAnumalaLab4.py 
Enter a date (mm/dd/yyyy): 01/01/1000
The converted date is: January 01, 1000
>>> 
RESTART: /Users/aadianumala/Documents/CollegeCompSci/CS3B/aadithyaAnumalaLab4.py 
Enter a date (mm/dd/yyyy): 06/19/2050
The converted date is: June 19, 2050
>>> 
RESTART: /Users/aadianumala/Documents/CollegeCompSci/CS3B/aadithyaAnumalaLab4.py 
Enter a date (mm/dd/yyyy): 02/29/2016
The converted date is: February 29, 2016
>>> 
RESTART: /Users/aadianumala/Documents/CollegeCompSci/CS3B/aadithyaAnumalaLab4.py 
Enter a date (mm/dd/yyyy): 02/29/2015
This isn't a leap year.
>>> 
RESTART: /Users/aadianumala/Documents/CollegeCompSci/CS3B/aadithyaAnumalaLab4.py 
Enter a date (mm/dd/yyyy): hi, ms. lamble!
Invalid Input.
>>> 
"""
