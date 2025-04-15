#!/usr/bin/python3
import calendar

month_to_int = {"January":1,"February":2,"March":3,"April":4,"May":5,"June":6,"July":7,"August":8,"September":9,"October":10,"November":11,"December":12}
int_to_month = {v: k for k, v in month_to_int.items()}

def read_data(filename):
    f = open(filename, "r")
    line1 = f.readline().rstrip()
    [month_name,year] = line1.split(" ")
    month = month_to_int[month_name]
    start_day = f.readline().rstrip()
    end_day = f.readline().rstrip()
    f.close()
    return [month, int(year), int(start_day), int(end_day)]

def save_data(filename, lines):
    f = open(filename, "w")
    for line_iter in range(0,len(lines)):
        f.writelines(lines[line_iter])
        if line_iter < len(lines)-1:
            f.writelines('\n')
    f.close()
    return 0

def produce_calendar(month, year, start_day, end_day):
    calendar_lines = [(int_to_month[month]+' '+str(year)),'S    M    T    W    T    F    S ']
    calendar_object = calendar.Calendar(firstweekday=start_day)
    calendar_numeric = calendar_object.monthdayscalendar(year, month)
    end = False
    for cal_week in calendar_numeric:
        text_list = []
        for cal_day in cal_week:
            if cal_day == 0:
                text_list.append("     ")
            else:
                text_list.append(str(cal_day).ljust(5,' '))
            if cal_day == end_day:
                end = True
                break
        calendar_lines.append(''.join(text_list))
        if end:
            break


    return calendar_lines


[month, year, start_day, end_day] = read_data("BAI2.INP")
calendar_lines = produce_calendar(month, year, start_day, end_day)
save_data("BAI2.OUT", calendar_lines)