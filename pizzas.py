pizzas = ['pizza funghi', 'pizza hawaii', 'pizza parma']
for pizza in pizzas:
	print (pizza + "\n")
for pizza in pizzas:
	print ("I really like " + pizza.title() + "!\n")
print ("Pizza = <3\n")

pizzas.append('pizza tonno')
pizzas.append('pizza diavolo')
print (pizzas)

print ("\nThe first three pizzas on the list are:")
for pizza in pizzas [:3]:
	print (pizza.title())

print ("\nThree pizzas from the middle of the list are:")
for pizza in pizzas [1:4]:
	print (pizza.title())

print ("\nThe last three pizzas in the list are:")
for pizza in pizzas [-3:]:
	print (pizza.title())

#"pizza slices"

pizzas = ['pizza funghi', 'pizza hawaii', 'pizza parma']
friend_pizzas = pizzas [:]
