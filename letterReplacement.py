aString = "Charizard"
listString = list( aString )

print("Before operation:", listString)

for i in range(len(listString)):
    if listString[i] == 'a':
        listString[i] = '*'

print("After operation:", ''.join(listString))