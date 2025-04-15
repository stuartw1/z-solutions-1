#!/usr/bin/python3
import datetime

number = input("enter spreadsheet date number: ")
date = datetime.datetime(1990,1,1)+datetime.timedelta(days=int(number))
print(date.strftime("Day: %d, month: %m, year: %Y"))