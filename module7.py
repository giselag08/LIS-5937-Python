from datetime import datetime, timedelta
#Orginal datetime
now = datetime.now()
print("now =", now)

#Add 2 years
print(datetime.now() + timedelta(days=730))

#Subtract 60 seconds
print(datetime.now() - timedelta(seconds=60))

from datetime import timedelta
delta1 = timedelta(days = 100, hours = 10, minutes = 13)
print("Object representing 100 days, 10 hours, and 13 minutes:", delta1)

#Two Arguments
#Add 20 days
twentyDays = print(datetime.now() + timedelta(days=20))
#Add 1 hour
oneHour = print(datetime.now() - timedelta(hours=1))
#Add 10 minutes
tenMinutes = print(datetime.now() - timedelta(minutes=10))
print(f"Question #4:\nCurrent datetime: datetime.now()\nAdd 20 days:[twentyDays]\nAdd 1 hour:[oneHour]\nAdd 10 minutes:[tenMinutes]")
