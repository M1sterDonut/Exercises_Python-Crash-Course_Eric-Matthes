buffet_foods = ('rice with basil pork', 'stamppot', 'hamburger', 'apple pie', 
'coffee')

print (buffet_foods)

#use for loop to print items
for buffet_food in buffet_foods:
	print (buffet_food.title())


#try modify
#buffet_foods[1] = 'burrito'
#can only write as comment or pragramme crash


buffet_foods = ['rice with basil pork', 'burrito', 'cheeseburger', 'apple pie', 
'coffee']

print ('\nNew and improved menu:')
for buffet_food in buffet_foods:
	print (buffet_food.title())