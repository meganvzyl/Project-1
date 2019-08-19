# Introduction to Programming, Task 12: Capstone project 1
# Megan van Zyl, 17/04/2019
# Python code to create and Investment Calculator.

print ("INVESTMENT CALCULATOR")

import math
P = float(input("Enter amount depositing: "))                       #user enters deposit
i = float(input("Enter the interest rate: "))                       #user enters interest rate
t = float(input("Enter the number of years of the investment: "))   #user enters years of the investment
r = i/100                                                           #change the interest to a float
Simple = P*(1+r*t)                                                  #formula for simple interest
Compound = P* math.pow((1+r),t)                                     #formula for compound interest

interest = input("Enter prefered interest: (Simple or Compound)")   #user enters type of interest
if interest == "Simple":  
    print (Simple)
else:
    print (Compound)


