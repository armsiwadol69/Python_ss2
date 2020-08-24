#Example 1
a = 100
def test():
    c = 5
    print("a = %d,c = %d" %(a,c))

print(a)
test()
print(a)

#Example 2
a = 100
def test():
    c = 55
    a = 77
    print(a,c)

print(a)
test()
print(a)

#Example 3 Local
a = 100
def test():
    a = 0
    a = a +100
    print(a)

print(a)
test()
print(a)

#Example 3 Global Var
a = 100
def test():
    global a
    a = a +100
    print(a)

print(a)
test()
print(a)

#Lap 6
#6.1
name = str(input("What Is Your Name? : "))
time = int(input("How many name do you want? : "))
def repeatbday(name):
    print("Happy Birthday To ",name)
for x in range(time):
    repeatbday(name)
num = int(input("Enter the number: "))

print("Multiplication Table of", num)
for i in range(1, 11):
   print(num,"X",i,"=",num * i)

#6.2
number = int(input("What -Multiplication Table- do you want? : "))
def timetable(time):
    for x in range(1,13):
        math = time * x
        print(time,"X",x,"=",math,end=" ")
2
print("Multiplication Table Of", number)
timetable(number)

for loop in range(12,16):
    timetable(loop)
