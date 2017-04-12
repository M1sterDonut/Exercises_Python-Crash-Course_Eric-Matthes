#3-10
#random cities
cities = ['sydney', 'montreal', 'mexico city', 'cape town', 'moscow', 'london']
print (cities)

#temp. alph. sort
print (sorted(cities))
#temp. alph. rev. sort
print (sorted(cities, reverse=True))
print (cities)

#perm. rev. sort
cities.reverse()
print (cities)

#perm. rev. rev. sort
cities.reverse()
print (cities)

#perm. alph. sort
cities.sort()
print (cities)

#perm. alph. rev. sort
cities.sort(reverse=True)
print (cities)

del cities[1]
print (cities)

cities.insert(1, 'paris')
print (cities)
cities.append('barcelona')
print (cities)
print ("The city I most recently added to my plans is " + cities[-1].title() + ".")
no_go = cities.pop(-2)
print ("I won't make it to " + no_go.title() + " anytime soon :(")
no_go2 = 'sydney'
cities.remove(no_go2)
print ("Also " + no_go2.title() + " is a bit too far...")

print (len (cities))
print ("There are ", len(cities), " cities on my list.")

print (cities)