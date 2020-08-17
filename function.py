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


