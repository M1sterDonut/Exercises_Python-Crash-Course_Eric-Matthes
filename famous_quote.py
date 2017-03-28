# Printing a quote using \n and \t as well as quotation marks in printed text
print ('Winston Churchill once said, \n\t"What is the purpose of living \n\tif it be not to strive for noble causes \n\tand to make this muddled world a better place \n\tfor those who live in it after we are gone."')

famous_person = "Winston Churchill"
message = ( ' once said, \n\t"What is the purpose of living \n\tif it be not to strive for noble causes \n\tand to make this muddled world a better place \n\tfor those who live in it after we are gone."')
print (famous_person + message)

# Using a different name in the same message
famous_person_2 = "\nJustin Bieber has NOT"
print (famous_person_2 + message)

# Practicing the stripping functions
article = "\nHe, "
famous_person_2 = "    Justin Bieber has NOT   "
print (article + famous_person_2 + message)
print (article + famous_person_2.strip().title() + message)
print (article + famous_person_2.lstrip().upper() + message)
print (article + famous_person_2.rstrip().lower() + message)