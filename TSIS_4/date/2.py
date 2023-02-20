import datetime
print("Today: ", datetime.date.today())
print("Yesterday: ", datetime.date.today()-datetime.timedelta(days=1))
print("Next day: ", datetime.date.today()+datetime.timedelta(days=1))
