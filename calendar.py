import calendar
year= input("Select the year of the calendar you want to print?:")
months= input("Select the month of the calendar you want to print?:")
year=int(year)
months=int(months)
x=calendar.month(year,months)
print(x)

