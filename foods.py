#copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print ("My favourite foods are:")
print (my_foods)

print ("\nMy friend's favourite foods are:")
print (friend_foods)

#list with nicer format
print ("\nMy favourite foods are:")
for my_food in my_foods:
	print (my_food.title())

print ("\nMy friend's favourite foods are:")
for friend_food in friend_foods:
	print (friend_food.title())

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print ("\nMy favourite foods are:")
print (my_foods)
print ("\nMy friend's favourite foods are:")
print (friend_foods)

#This doesn't work
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favourite foods are:")
print(my_foods)

print ("\nMy friend's favourite foods are:")
print (friend_foods)

#4-10 slices
print ("\nThe first three items in the list are:")
print (my_foods[0:3])

print ("\nThree items from the middle of the list are:")
print (my_foods[1:4])

print ("\nThe last three items in the list are:")
print (my_foods[-3:])

#4-12 More loops /"nicer print"
print ("\nThe first three items in the list are:")
for food in my_foods [0:3]:
	print (food.title())

print ("\nThree items from the middle of the list are:")
for food in my_foods [1:4]:
	print (food.title())

print ("\nThe last three items in the list are:")
for food in my_foods [-3:]:
	print (food.title())