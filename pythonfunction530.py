#1
def hello(name):
    print('Hello %s'% name)
def count_vowel(str):
    vowel=0
    for c in str:
        if c in ('A','E','I','O','U','a','e','i','o','u'):
            vowel=vowel+1
    return vowel
def area(width, height):
    c=widthheight
    return c
#calling functions
hello('Danny')
hello('Mateo')
print('Vowel in string= %d'% count_vowel('marcuscode.com'))
print('Vowel in string= %d'% count_vowel('Python'))
print('Area = %d'% area(8,4))


#2
def show_info(name,salary=75000, lang="Python"):
    print('Name: %s'% name)
    print('Salary: %d'% salary)
    print('Language: %s'% lang)
#calling function
show_info('Nam')
show_info('Nam', 100000)
show_info('Champ', 900000,'Java')



#3
def create_button(id, color='#ffffff', text='Button',size=16):
    print('Button ID: %d'% id)
    print('Attributes:')
    print('Color: %s'% color)
    print('Text %s'% text)
    print('Size: %d px'% size)
    print()
#calling function
create_button(1)
create_button(2,color='#4286f4',text='Sign up')
create_button(id=3,color='#323f54', size=24)
create_button(color='#1cb22b',text='Login',size=32,id=4)


#4
f=lambda x: x+1
print(f(2))
print(f(8))

g=lambda a, b: (a+b) /2
print(g(3,5))
print(g(10,33))

def make_incrementor(n):
    return lambda x: x + n

f =make_incrementor(13)
print(f(0))
print(f(1))
print(f(5))


#5
numbers=[2,15,5,7,10,3,28,30]
print(list(filter(lambda x: x%5==0, numbers)))
print(list(map(lambda x: x*2, numbers)))
