def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def day_of_year(day, month, year):
    leap_year = is_leap(year)
    
    month_days = [31, 29 if leap_year else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if not is_leap(year) and month == 2 and day == 29:
        print("Invalid")
        exit()
    elif day > month_days[month - 1] or day > month_days[month - 1]:
        print("Invalid")
        exit()

    day_count = sum(month_days[:month - 1]) + day
    return day_count

def date_diff(date1, date2):
    day1, month1, year1 = map(int, str(date1).split('-'))
    day2, month2, year2 = map(int, str(date2).split('-'))
    
    if (month1 < 1 or month1 > 12) or (month2 < 1 or month2 > 12):
        print("Invalid")
        exit()
    elif (day1 < 1 or day1 > 31) or (day2 < 1 or day2 > 31):
        print("Invalid")
        exit()

    #print("date1:", day1, month1, year1)
    #print("date2:", day2, month2, year2)

    day_num1 = day_of_year(day1, month1, year1)
    day_num2 = day_of_year(day2, month2, year2)
    
    total_days1 = day_num1 + sum(366 if is_leap(y) else 365 for y in range(year1))
    total_days2 = day_num2 + sum(366 if is_leap(y) else 365 for y in range(year2))
    
    if total_days2 < total_days1:
        print("Invalid")
        exit()
    return total_days2 - total_days1

raw_input1 = input("Enter Input: ")
valid_input_list = set("0123456789-, ")

if not all(char in valid_input_list for char in raw_input1) or raw_input1.count('-') != 4 or raw_input1.count(',') != 1:
    print("Invalid")
    exit()


date1, date2 = raw_input1.split(", ")
#print("date1:", date1)
#print("date2:", date2)
difference = date_diff(date1, date2)
print(difference+1)