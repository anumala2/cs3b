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

from decimal import *
from datetime import date

#global variables
balance = Decimal(1000)
last_interest_date = date.min
OVERCHARGE_FEE = Decimal(10)

class BankAccount:

    #constructor
    def __init__(self, initial_balance):
        global balance
        balance = Decimal(initial_balance)

    #deposit money
    def deposit(self, amount):
        global balance
        balance = balance + Decimal(amount)

    #withdraw money
    def withdraw(self, amount):
        global balance
        if balance < Decimal(amount):
            balance = balance - Decimal(OVERCHARGE_FEE)
            return
        balance = balance - Decimal(amount)

    #adding interest to the balance - only once a month
    def add_interest(self, rate):
        global balance
        global last_interest_date
        if last_interest_date.month != date.today().month:
            balance = balance * (Decimal(rate)/Decimal(100) + Decimal(1))
            last_interest_date = date.today()

    #prints out balance aesthetically
    def get_balance(self):
        if balance > 0:
            print("$" + str(round(balance,2)))
        if balance < 0:
            print("-$" + str(abs(round(balance,2))))
