#1.6 boolean
#ex1
a = True
b = False
print(a,type(a))
print(b,type(b))
#ex2
c = 8 > 4
c2 = 8 < 4
print(c,type(c))
print(c2,type(c2))
#ex3
d = bool("lost one")
print("line 14",d,type(d))
#ex4
e = bool(False)
e2 = bool(None)
e3 = bool(0)
e4 = bool("")
print(e)
print(e2)
print(e3)
print(e4)
#ex5
f = 10 > 5
if f == True:
    print("YES MAMA")
else:
    print("NO WAY!")



