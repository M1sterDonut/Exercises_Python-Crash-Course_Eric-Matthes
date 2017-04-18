squares = []
for value in range (1,11):
	square = value**2
	squares.append(square)
print (squares)

squares = []
for value in range (1,11):
	squares.append(value**2)
print (squares)

digits = [1,2,3,4,5,6,7,8,9,0]
print (min(digits))
print (max(digits))
print (sum(digits))

squares = [value**2 for value in range (1,11)]
print(squares)

#4-3 counting to twenty
for value in range (1,21):
	print (value)

#4-4 one million - shortened to 1000 to fasten exec
for value in range (1,1001):
	print (value)

#4-5 summing a million
millions = [million for million in range (1,1000001)]
print (min(millions))
print (max(millions))
print (sum(millions))

#4-6 odd numbers
odds = list (range (1,21,2))
print (odds)

for odds in range (1,21,2):
	print (odds)

#4-7 threes
threes = []
for value in range (1,11):
	threes.append(value*3)
print (threes)

threes = [3*value for value in range (1,11)]
print (threes) #f-yeah! B)

#4-8 cubes
cubes = []
for cube in range (1,11):
	cubes.append(cube**3)
print (cubes)

#4-9 list comprehension
cubes = [value**3 for value in range (1,11)]
print (cubes)