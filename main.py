def check_leap_year(year):
	if year % 4 == 0:
		return (str(year) + ' is a leap year')
	else:
		return (str(year) + ' is not a leap year')
		
print(check_leap_year(2012))
print(check_leap_year(2013))
