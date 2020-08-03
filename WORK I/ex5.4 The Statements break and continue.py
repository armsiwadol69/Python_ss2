#ex5.4
#ex1
ex1 = ["Angelina","Croissant","Astesia","Durin","Exusiai"]
for x in ex1 :
    print(x,end=" ")
    if x == "Durin":
        break
print("")
#ex2
ex2 = ["Angelina","Croissant","Astesia","012","Exusiai"]
for y in ex2 :
    if y.isalpha() is True :
        print(y)
        while y.isalpha() is False :
            continue

#ex3
ex3 = 80
while ex3 < 100 :
    print(ex3,end=" ")
    ex3 += 2
    if ex3 > 92 :
        break
print(" ")
#ex4
ex4 = 0
while ex4 < 20 :
    print(ex4,end=" ")
    ex4 += 2
    if ex4 in range(10,15) :
        break
print(" ")
#ex5
ex5 = 60
while ex5 < 80:
    ex5 += 5
    if ex5 in [70,75] :
        continue
    print(ex5)
    






