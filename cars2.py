cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
	if car == 'bmw':
		print (car.upper())
	else:
		print (car.title())

car = 'bmw'
print (car == 'bmw')

car = 'Audi'
car.lower() == 'audi'

car = 'subaru'
print ("\nIs car == 'subaru'? I predict True.")
print (car == 'subaru')

print ("\nIs car == 'audi'? I predict False.")
print (car == 'audi')

print ('bmw' in cars)

if 'susuki' not in cars:
	print ("Don't have that one")