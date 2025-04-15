#!/usr/bin/python3
import datetime

date_entry = input("Enter date (dd/mm/yyyy): ")
[day,month,year] = date_entry.rstrip().split('/')
base_date=datetime.date(1990,1,1)
target_date=datetime.date(int(year),int(month),int(day))
date_delta=target_date-base_date
print('Entered date is',date_delta.days,'days different from 1st January 1990')