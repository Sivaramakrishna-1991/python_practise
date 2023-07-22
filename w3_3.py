# printing date and time
import datetime
now = datetime.datetime.now()
print("Current time is: ", now)
print(now.strftime('%Y-%m-%d %H-%M-%S'))
