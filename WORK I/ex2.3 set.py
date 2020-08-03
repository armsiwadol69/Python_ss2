#ex2.3
#ex1
set_1 = {"Vigna","Reed","Zima"}
print(set_1,type(set_1))
#ex2
set_1 = {"Vigna","Reed","Zima"}
for x in set_1 :
    print(x)
print("Reed" in set_1)
#ex3
set_1 = {"Vigna","Reed","Zima"}
set_1.add("Yato")
print(set_1,"ADD")
set_1.update(["Warfarin","Skadi"])
print(set_1,"UPDATE")
#ex4
set_2 ={"Warfarin","Skadi","Silence","Specter","Platinum"}
print(len(set_2))
#ex5
set_1 = {"Vigna","Reed","Zima"}
set_2 = {"Warfarin","Skadi","Silence","Specter","Platinum"}
set_3 = set_1.union(set_2)
print(set_3)

