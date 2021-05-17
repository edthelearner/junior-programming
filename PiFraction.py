import math

searchSpace = int(input("What number would you like to search up to? > "))

bestGuessPair = [0,0]
bestGuessDiff = 1

for i in range(1,searchSpace):
    for j in range(1,searchSpace):
        if abs(float(i/j - math.pi)) < bestGuessDiff:
            bestGuessPair[0], bestGuessPair[1] = i, j
            bestGuessDiff = abs(float(i / j - math.pi))

print("Best guess difference:",bestGuessDiff)
print("Best guess pair:",bestGuessPair)