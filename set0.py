#ex2.2
#ex1
my_tuple = ("Frostleaf","Hibiscus","Leonhardt")
print(my_tuple,type(my_tuple))
#ex2
my_tuple = ("Frostleaf","Hibiscus","Leonhardt")
print(my_tuple[1])
#ex3
my_tuple_ext = ("Frostleaf","Hibiscus","Leonhardt","Lappland")
print(my_tuple_ext[-1])
print(my_tuple_ext[-4])
#ex4
ark_tuple = ("Matoimaru","Mayer","Podenco","Nearl")
x = list(ark_tuple)
x[3] = "Savage"
y = tuple(x)
print(y,type(y))
#ex5
ark_tuple = ("Matoimaru","Mayer","Podenco","Nearl")
print(len(ark_tuple))


