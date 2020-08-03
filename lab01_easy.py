#8/3/2020 Lab1PythonEZ
#Example1
m = 1
if m == 10 :
    print('Print Value Of m = %d' %m)
else:
    print('Value Of m = %d' %m)

#Example2
a = 10
b = 2
if a > b :
    print('a is greater than b')

#Example3
x = 5
y = 1
if 10 > x > y :
    print(x)

#Example4
mark = int(input("Enter You Score : "))
if 100 >= mark > 80 :
    print('Grade A')
else:
    print("You got Grade B~F")

#Example5
data = int(input('Enter the desired numeric value : '))
digit = 20
if data == digit :
    print('Equal')
elif data > digit :
    print('over')
else:
    print('Wrong')

#Example6
zipcode = input('Enter zip code : ')

if len(zipcode) <= 0 :
    print("Please Enter ZipCode!")
elif len(zipcode) > 5 :
      print("The ZipCode is not valid. Please check try again.")
else: print("ZipCode is valid, ready to deliver."," ","Your ZipCode : ",zipcode)
