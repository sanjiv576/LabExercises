"""
10. Write a Python program to convert seconds to day, hour, minutes and seconds.
"""
sec = int(input("Enter time in seconds : "))
day = sec/(24*60*60) # 1 day = 24 hours = 24*60 mins = 24*60*60
hour = sec/3600  # 1 hour = 60 mins = 60*60 sec
mins = sec/60  # 1 min = 60 sec
print(f"{sec} seconds = {day} day(s) \n{sec} seconds = {hour} hour(s) \n{sec} seconds = {mins} minutes")