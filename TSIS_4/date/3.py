import datetime as datetime
dt_with_microseconds = datetime.datetime.now() 
dt_without_microseconds = dt_with_microseconds.replace(microsecond=0) 
print("Дата-время с микросекундами:", dt_with_microseconds)
print("Дата-время без микросекунд:", dt_without_microseconds) 