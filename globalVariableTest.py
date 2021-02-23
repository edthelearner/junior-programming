def fooBar():
    global pName
    pName = input("What's your name? > ")
    
pName = None
fooBar()
print(pName)
