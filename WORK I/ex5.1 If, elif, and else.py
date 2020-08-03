#ex5.1
#ex1
ex1 = 15
ex1_1 = 15
ex1_2 = 10
if ex1 == ex1_1 and ex1+ex1_1 >= ex1_2:
    print("TRUE")
else:
    print("FALSE")
#ex2
b1 = "Ansel"
if b1.isdecimal() is True :
    print("b1 is number")
elif b1.isupper() is True :
    print("B1 is all upper case")
elif b1.isalpha() is True :
    print("b1 is TEXT")
#ex3
ex3 = 9902
if ex3 < 9000 :
    print("ex3 below 9000")
elif ex3 > 10000 :
    print("ex over 9000")
else:
    print("maybe ex3 around 9001-9999")
#ex4
ex4 = "SliverAsh"
if ex4.isalpha() and ex4 == "SliverAsh": print("SILVERASH BLOODLINE MUST CONTINUE")
print(ex4.isalpha() and ex4 == "SliverAsh")
#ex5
ex5 = 6000
if ex5 == 1699 or ex5 < 600 or ex3.bit_length() == 14 :
    print("WOW NICE!",ex3.bit_length())




