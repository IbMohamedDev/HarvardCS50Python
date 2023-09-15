# following along to Harvard CS50 Intro to Python

name = input("what is your name " )  # name = Cena
print("Hello", name, end="\n")

name = name.strip()   #removes whitespace from str
name = name.title() #capitalize user's name
# chaining methods
# name = name.strip().title()
print(f"Hey, {name}")  # returns "Hey, Cena" 

#split str on space
first, last = name.split(" ")
print(first, last)
# ONE LINE COMMENT
''' MULTI LINEb
COMMENTS
 '''

#strings 


def hello(name="Cena"):  #default name value
    print(name)


hello()
hello("John")  # can still add new parameter