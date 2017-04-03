motorcycles = ['honda', 'yamaha', 'suzuki']
print (motorcycles)

#replacing the first element
motorcycles[0] = 'ducati'
print (motorcycles)

#adding elements - appending
motorcycles.append('ducati')
print (motorcycles)

#adding to empty list
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

#inserting new element
motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(0, 'ducati')
print (motorcycles)

#deleting list elements
motorcycles = ['honda', 'yamaha', 'suzuki']
print (motorcycles)

del motorcycles[0]
print (motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print (motorcycles)

del motorcycles[1]
print (motorcycles)
print (motorcycles[1])

#"popping" a motorcycle a.k.a. list item
motorcycles = ['honda', 'yamaha', 'suzuki']
print (motorcycles)

popped_motorcycle = motorcycles.pop()
print (motorcycles)
print (popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print ('The last motorcycle I owned was a ' + last_owned.title() + '.')

#Popping Items from any Position in a List
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title()+ '.')

#Removing an Item by Value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print (motorcycles)

motorcycles.remove('ducati')
print (motorcycles)

#use remove() method to work with a value removed from list
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print (motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")





