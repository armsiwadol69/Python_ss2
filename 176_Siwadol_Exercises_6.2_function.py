#E6.2
#Calculate the area of a triangle

print("Calculate the area of a triangle.")
base = int(input("Base Wide : "))
high = int(input("Height : "))

def area(a,b):
    return (1/2)*a*b

print("Area Of Triangle : ",area(base,high))


#Moneyleft
print("Note : Phone is 2369 THB.")
money = int(input("Money you have : "))
def moneyleft(a):
    return a-2369

if moneyleft(money) >= 0:
    print("You can BUY IT!")
    print("Money left : ",moneyleft(money),"THB")
else:
    print("So bad,YOU CAN'T BUY IT. You are so pool.")
    print("Need more",abs(moneyleft(money)),"THB")
