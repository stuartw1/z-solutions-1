#!/usr/bin/python3
def is_leap_year(year):
    # A leap year is divisible by 4, but years divisible by 100 that are not divisible by 400 are not leap years.
    #Check divisible by 4
    if (year%4 == 0):
        #Check if divisible by 100 but not 400 
        if (year%100 == 0) and (year%400 != 0):
            #Year is divisible by 100 but not 400
            return False
        else:
            #Year is divisible by 4 and is not divisible by 100 but not 400
            return True
    else:
        #Year is not divisible by 4, so cant be a leap year
        return False
    
years = input("input years as 'Y1, Y2' where Y2 > Y1: ")
[year1,year2] = years.rstrip().split(',')
[Y1,Y2] = [int(year1), int(year2)]
assert Y2 > Y1

leap_year_count = 0
for x in range(Y1,Y2+1):
    if is_leap_year(x):
        leap_year_count += 1

print("There are",leap_year_count,"leap year(s) between",Y1,"and",Y2)