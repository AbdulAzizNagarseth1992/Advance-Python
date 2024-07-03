import datetime
import calendar

def check_weekday_or_weekend(date):
	try:
		given_date = datetime.datetime.strptime(date, '%d %m %Y')
		day_of_week = (given_date.weekday() + 1) % 7
		
		if day_of_week < 5:
			day_type = 'weekday'
		else:
			day_type = 'weekend'
		
		print(f"The day of the week for {given_date.strftime('%Y-%m-%d')} is {day_of_week} ({day_type})")
		
	except ValueError as e:
		print(f"Error: {e}")

date = '04 07 2024'
check_weekday_or_weekend(date)