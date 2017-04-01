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