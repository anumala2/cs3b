###############################################
# CS 21B Intermediate Python Programming Lab #5
# Topics: web urllib
# Description: This program finds the html source
#              from nasonline.org and finds the 
#              frequency of certain key terms and  
#              prints that out for the user.
# Input: NA
# Output: date and frequncies
# Version: 3.7.0
# Development Environment:  IDLE
# Developer:  Aadithya Anumala
# Student ID: 20365071
# Date:  05/21/19
###############################################

from urllib import request
from datetime import date

nas = request.Request("http://www.nasonline.org")
resp = request.urlopen(nas)
pars = resp.read()
pars = pars.decode(encoding='UTF-8',errors='strict')

topics = ["research", "climate", "evolution", "cultural",
          "leadership", "nation", "physical", "science",
          "biological", "global"]

print(f"Today's date is {date.today():%Y-%m-%d}\n")

for topic in topics:
    count = str(pars.count(topic))
    print(f"{topic} appears {count} times")

"""   
RESTART: /Users/aadianumala/Documents/CollegeCompSci/CS3B/aadithyaAnumalaLab5.py 
Today's date is 2019-05-21

research appears 8 times
climate appears 3 times
evolution appears 3 times
cultural appears 4 times
leadership appears 2 times
nation appears 17 times
physical appears 1 times
science appears 19 times
biological appears 1 times
global appears 1 times
>>> 
"""
