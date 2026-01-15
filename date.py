def is_leap(year):
    try:
        year = int(year)
    except:
        return False
    else:
        if year < 1:
            return False
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def day_of_year(day, month, year):
    try:
        day = int(day)
        month = int(month)
        year = int(year)
    except:
        return 'Invalid'
    else:
        if day < 1 or month < 1 or year < 1:
            return 'Invalid'
    
    if month < 1 or month > 12:
        return 'Invalid'

    leap_year = is_leap(year)
    
    month_days = [31, 29 if leap_year else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if not is_leap(year) and month == 2 and day == 29:
        return 'Invalid'
    elif day > month_days[month - 1] or day > month_days[month - 1]:
        return 'Invalid'
    day_count = sum(month_days[:month - 1]) + day
    return day_count

date_str = input("Enter a date : ")
valid_input_list = set("0123456789-")
try:
    day, month, year = date_str.split('-')
except:
    day = -1
    month = -1
    year = -1
day_number = day_of_year(day, month, year)
print("day of year:",day_number,",is_leap:",is_leap(year))