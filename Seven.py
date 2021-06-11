"""
You live 4 miles from university.
The bus drives at 25mph but spends 2 minutes at each of the 10 stops on the way.
How long will the bus journey take? Alternatively, you could run to university.
You jog the first mile at 7mph; then run the next two at 15mph; before jogging the last at 7mph again.
Will this be quicker or slower than the bus?
"""

distance = 40 # 25 miles

# For bus
busSpeed = 25  # 25 mph
stopsNo = 10
stoppingTime = 2 /60  # 2 mins in each stop , so in hour : 2/60
totalStoppingTime = stoppingTime * stopsNo

busTime = distance/busSpeed # formula : s = d/t

totalTimeBus = totalStoppingTime + busTime  # calculated time will be 1.9333 hours
print(f"The bus journey takes  {totalTimeBus} hours ")

# For jogging student

studentSpeedAt1 = 7  # 7 mph in first mile

studentSpeedAt23 = 15  # 15 mph in next two miles i.e 2 and 3

studentSpeedAt4 = 7  # 7 mph in last mile

averageStudentSpeed = (studentSpeedAt1 + studentSpeedAt23 + studentSpeedAt4)/3

totalTimeStudent = distance/averageStudentSpeed  # formula , calculated time will be 4.1379 hours

print(f"The jogging student takes {totalTimeStudent} hours")

if totalTimeStudent < totalTimeBus:
    print(f"By jogging , the student becomes slower")
else:
    print(f"By bus, the student is quicker")