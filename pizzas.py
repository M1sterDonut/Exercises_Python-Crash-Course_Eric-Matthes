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

pizzas.append('pizza diavolo')
friend_pizzas.append('pizza tonno')

print ("\nMy favourite pizzas are:")
for pizza in pizzas:
	print(pizza.title())

print ("\nMy friend's favourite pizzas are:")
for friend_pizza in friend_pizzas:
	print (friend_pizza.title())