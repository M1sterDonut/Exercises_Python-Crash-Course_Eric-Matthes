#permanently sorting alphabetically

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print (cars)

# ... & reverse alphabetical order
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print (cars)

#temporary sorting
cars = ['bmw', 'audi', 'toyota', 'subaru']
print ("\nHere is the original list:")
print (cars)

print ("\nHere is the sorted list:")
print (sorted(cars))
print ("\nHere is the reverse alphabetically sorted list:")
print (sorted(cars, reverse=True))
print ("\nHere is the original list again:")
print (cars)