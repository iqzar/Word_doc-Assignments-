#Python program to convert seconds to day, hour, minutes and seconds:
time_sec=int(input("Enter time in seconds :"))
time_days=round(time_sec/86400)
time_hours=round(time_sec/3600)
time_min=round(time_sec/60)
print("Time in days :" ,time_days)
print("Time in hours:", time_hours)
print("Time in minutes:",time_min)
