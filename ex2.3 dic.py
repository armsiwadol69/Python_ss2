#2.3 Dictionary
#Ex1
dic1 = {
    "Name" : "Plume",
    "Class" : "Vanguard",
    "Rarity" : 3
}
print(dic1,type(dic1))
#ex2
dic1 = {
    "Name" : "Plume",
    "Class" : "Vanguard",
    "Rarity" : 3
}
print(dic1["Name"],"Is",dic1["Class"])
#ex3
dic1 = {
    "Name" : "Plume",
    "Class" : "Vanguard",
    "Rarity" : 3
}
dic1["Name"] = "Elysium"
dic1["Rarity"] = 5
print(dic1)
#ex4
dic2 = {
    "Name" : "Manticore",
    "Class" : "Specialist",
    "Rarity" : 5
}
dic2["Faction"] = "R.I."
print(dic2)
#ex5
dic3 ={
    "Name" : "Haze",
    "Class" : "Caster",
    "Rarity" : 4
}
dic3.pop("Class")
print(dic3)

