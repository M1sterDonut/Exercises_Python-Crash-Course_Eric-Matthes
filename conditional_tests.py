weather = 'sunny'
print ("Is the weather sunny today? I predict True.")
print (weather == 'sunny')

print ("\nIs the weather rainy today? I predict False.")
print (weather == 'rainy')

food = 'gross'
print ("\nIs the food gross today? I predict True.")
print (food == 'gross')

print ("\nIs the food tasty today? I predict False.")
print (food == 'tasty')

# using !=
shop = 'empty'
print ("\nIs the shop busy today? I predict True.")
print (shop == 'busy')

if shop != 'busy': 
	print ("Oh no, I was wrong!")
else: 
	print ("Look at all these people!")

shop = 'busy'
print ("\nIs the shop busy today? I predict True.")
print (shop == 'busy')

if shop != 'busy': 
	print ("Oh no, I was wrong!")
else: 
	print ("Look at all these people!")

#5-2 more conditional tests

couch = 'large and comfortable'
print ("\nIs the couch large and comfortable?")
print (couch == 'large and comfortable')

print ("\nIs the couch small and comfortable?")
print (couch == 'small and comfortable')

name = 'James'
print ("\nIs his name James?")
print (name.lower() == 'james')

print ("\nIs his name Brian?")
print (name.lower() == 'brian')

friends_at_party = 13
print ("\nAre there 13 friends?")
print (friends_at_party == 13)
print ("\nAre there 15 guests or less?")
print (friends_at_party <= 15)
print ("\nAre there more than 13 guests?")
print (friends_at_party > 13)

shopping_list = ['tuna', 'bread', 'yoghurt']
print ("\nHave you remembered the bread?")
if 'bread' in shopping_list:
	print ("Yeah, got it.")
else:
	print ("Oh shoot, let me add that.")

print ("\nHave you remembered the tuna?")
if 'tuna' in shopping_list:
	print ("Yeah, got it.")
else:
	print ("Oh shoot, let me add that.")

print ("\nHave you remembered the peas?")
if 'peas' in shopping_list:
	print ("Yeah, got it.")
else:
	print ("Oh shoot, let me add that.")




