def spam():
    global eggs
    eggs = 97

def bacon( arg ):
    arg = 100

eggs = 55

spam()
print(eggs)

bacon( eggs )
print(eggs)
