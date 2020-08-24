#6.2
number = int(input("What -Multiplication Table- do you want? : "))
def timetable(time):
    for x in range(1,13):
        math = time * x
        print(time,"X",x,"=",math,end="|")

print("Multiplication Table Of", number)
timetable(number)

for loop in range(12,16):
    timetable(loop)
