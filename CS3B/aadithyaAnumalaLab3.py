###############################################
# CS 21B Intermediate Python Programming Lab #3
# Topics: Class Design, Methods
# Description: This program uses a bank account
#              and methods of depositing, with-
#              drawing, adding interest, and
#              printing out the balance in order
#              to work more closely with method
#              and class interaction in python.
# Output: Account values as we alter the balance
# Version: 3.7.0
# Development Environment:  IDLE
# Developer:  Aadithya Anumala
# Student ID: 20365071
# Date:  04/30/19
###############################################

#import class
from aadithyaAnumalaBank import BankAccount

#Instantiate a bank account with an original balance of $1000.00
account = BankAccount(1000)
account.get_balance()

#Deposit $500.00
account.deposit(500)
account.get_balance()

#Withdraws $2000.00
account.withdraw(2000)
account.get_balance()

#Adds 1% interest 
account.add_interest(1)
account.get_balance()

#Adds  2% interest
account.add_interest(2)
account.get_balance()

#Deposit $125,000.99
account.deposit(125000.99)
account.get_balance()

#Withdraws $0.99
account.withdraw(0.99)
account.get_balance()

#Withdraws $126,500.00
account.withdraw(126500.00)
account.get_balance()

#Withdraws $10.00
account.withdraw(10.00)
account.get_balance()

#Adds 1% interest
account.add_interest(1)
account.get_balance()

#test run
"""
RESTART: /Users/aadianumala/Documents/CollegeCompSci/CS3B/aadithyaAnumalaLab3.py 
$1000.00
$1500.00
$1490.00
$1504.90
$1504.90
$126505.89
$126504.90
$4.90
-$5.10
-$5.10
>>> 
"""
