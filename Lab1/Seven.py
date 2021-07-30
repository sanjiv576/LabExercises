"""
You live 4 miles from university.
The bus drives at 25mph but spends 2 minutes at each of the 10 stops on the way.
How long will the bus journey take? Alternatively, you could run to university.
You jog the first mile at 7mph; then run the next two at 15mph; before jogging the last at 7mph again.
Will this be quicker or slower than the bus?
"""
distance = 4
busSpeed = 25
busTime = (busSpeed/distance)+(20/60)
joggingStudentSpeedAt1 = 7
joggingStudentSpeedAt23 = 15
joggingStudentSpeedAt4 = 7
joggingStudentTime = (distance) / ((2/7)+(2/15))
if busTime < joggingStudentTime:
    print("By jogging student reaches University slower than bus")
else:
    print("By bus, students reach University faster")



"""
distance = 4  # 4 miles

# For bus
busSpeed = 25  # 25 mph
stopsNo = 10
stoppingTime = 2 / 60  # 2 mins in each stop , so in hour : 2/60
totalStoppingTime = stoppingTime * stopsNo

busTime = distance/busSpeed  # formula : s = d/t

totalTimeBus = totalStoppingTime + busTime 
print(f"The bus journey takes  {totalTimeBus} hours ")

# For jogging student

studentSpeedAt1 = 7  # 7 mph in first mile
studentCoveredDistance1 = 1
studentTime1 = studentCoveredDistance1/studentSpeedAt1
studentSpeedAt23 = 15  # 15 mph in next two miles i.e 2 and 3
studentCoveredDistance23 = 2
studentTime23 = studentCoveredDistance23/studentSpeedAt23
studentSpeedAt4 = 7  # 7 mph in last mile
studentCoveredDistance4 = 1
studentTime4 = studentCoveredDistance4/studentSpeedAt4
realStudentTime = studentTime1+studentTime23+studentTime4

print()
if realStudentTime < totalTimeBus:
    print(f"By jogging , the student becomes slower")
else:
    print(f"By bus, the student is quicker")
"""