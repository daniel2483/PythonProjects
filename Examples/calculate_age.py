import sys
from datetime import datetime

year = input("Year of birth: ")
month = input("Month of birth: ")
day = input("Day of birth: ")
errors = 0

try:
    year = int(year)
    if year < 1:
        print("Year Value should be a positive integer")
        errors=errors+1
except ValueError:
    print("Year was not provided with good format, should be YYYY. Example: 2014")
    errors=errors+1

try:
    month = int(month)
    if month > 12 or month < 1:
        print("Month Value should be in the range 1-12")
        errors=errors+1

except ValueError:
    print("Month was not provided with good format, should be YYYY. Example: 2014")
    errors=errors+1

try:
    day = int(day)
    if day > 31 or day < 1:
        print("Day Value should be in the range 1-31")
        errors=errors+1
except ValueError:
    print("Day was not provided with good format, should be YYYY. Example: 2014")
    errors=errors+1

if errors > 0:
    print("Date has errors...")
    sys.exit()

print("\n\nThis is a test...")
today = datetime.today()
now = today.strftime("%Y-%m-%d")
print("Today is ", now)

#if(month < 10):
#    month = "0"+str(month)

#if(day < 10):
#    day = "0"+str(day)

#date_time_str = str(year)+str(month)+str(day)

#date_time_obj = datetime.strptime(date_time_str, '%Y%m%d')

#print("YearMonthDay: ",date_time_str)

birthday = datetime(year, month, day, 0, 0, 0)
days = today - birthday

days_delta = days.days

#print("The type of days: ",type(days_delta))
years_number = days_delta//365
month_n = days_delta%365
month_number = month_n//30
days_number = month_n%30
print("The number of days: ",days_delta)
print("Number of Years: ",str(years_number)," and month(s) ",str(month_number)," and days ",str(days_number))


#print ("\n\nThe type of the date is now",  type(date_time_obj))
#print ("The date is", date_time_obj)
