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

#printing reverse order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print (cars)

cars.reverse()
print (cars)

cars.reverse()
print (cars)

#length of a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print (len(cars))

#3-8

visit_here = ['costa rica', 'australia', 'canada', 'sweden', 'lebanon']
print ("\nList in orginial order:")
print (visit_here)

print ("\nalphabetical without change:")
print (sorted(visit_here))
print (visit_here)

print ("\nreverse alphabetical without change:")
print (sorted(visit_here, reverse=True))
print (visit_here)

print ("\nreverse order of list:")
visit_here.reverse()
print (visit_here)

visit_here.reverse()
print (visit_here)

print ("\nstored alphabetically:")
visit_here.sort()
print (visit_here)

visit_here.sort(reverse=True)
print (visit_here)

