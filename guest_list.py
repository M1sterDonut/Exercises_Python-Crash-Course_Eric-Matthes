#Try it yourself: lists, popping, deleting, etc.

guest_list = ['the dread pirate roberts', 'ragnar lothbrok', 'heath ledger', 'jimi hendrix']
print (guest_list)
print ("") #How else do you get an empty line in the print?

#3-4
invitation_part1 = "Dear "
invitation_part2 = ",\nYou're kindly invited for dinner.\nI look forward to seeing you,\nM1sterDonut\n"
print (invitation_part1 + guest_list[0].title() + invitation_part2)
print (invitation_part1 + guest_list[1].title() + invitation_part2)
print (invitation_part1 + guest_list[2].title() + invitation_part2)
print (invitation_part1 + guest_list[3].title() + invitation_part2)

guest_list = ['the dread pirate roberts', 'ragnar lothbrok', 'heath ledger', 'jimi hendrix']
print (guest_list)

#name of the guest who can't make it
guest_cant_come = guest_list.pop(2)

sorry_msg1 = "Unfortunately, "
sorry_msg2 = " can't make it to the party."
print (sorry_msg1 + guest_cant_come.title() + sorry_msg2)
print (guest_list)

#replacing name of guest with new person
guest_list.insert(2, 'al pacino')
print (guest_list)

#second set of invitations
print ("")
invitation_part3 = "Dear "
invitation_part4 = ",\nI'm very happy to hear that you've decided to join us.\nSee you at the party tonight.\n- M1sterDonut\n"
print (invitation_part3 + guest_list[0].title() + invitation_part4)
print (invitation_part3 + guest_list[1].title() + invitation_part4)
print (invitation_part3 + guest_list[2].title() + invitation_part4)
print (invitation_part3 + guest_list[3].title() + invitation_part4)

#3-6: 
bigger_table = ", \nI'm happy to announce we've found a larger table.\n-MrD\n"
print (guest_list[0].title() + bigger_table)
print (guest_list[1].title() + bigger_table)
print (guest_list[2].title() + bigger_table)
print (guest_list[3].title() + bigger_table)

guest_list.insert(0, 'rick')
guest_list.insert(2, 'morty')
guest_list.append('enrique iglesias')
invitation_part5 = ", I'm looking forward to see you at our larger and much improved dining experience.\n-MrD\n"
print (guest_list)
print (guest_list[0].title() + invitation_part5)
print (guest_list[1].title() + invitation_part5)
print (guest_list[2].title() + invitation_part5)
print (guest_list[3].title() + invitation_part5)
print (guest_list[4].title() + invitation_part5)
print (guest_list[5].title() + invitation_part5)
print (guest_list[6].title() + invitation_part5)

sorry_msg3 = "Dear guests,\nUnfortunately I will only be able to invite two guests to the party.\n-MrD\n"
print (sorry_msg3)

popped_guest1 = guest_list.pop(1)
sorry_msg4 = "I'm sorry "
sorry_msg5 = ", \nI can't invite you this time.\nI hope we'll get a chance to make up for this missed occasion soon.\n-MrD\n"
print (sorry_msg4 + popped_guest1.title() + sorry_msg5)

popped_guest2 = guest_list.pop(2)
sorry_msg4 = "I'm sorry "
sorry_msg5 = ", \nI can't invite you this time.\nI hope we'll get a chance to make up for this missed occasion soon.\n-MrD\n"
print (sorry_msg4 + popped_guest2.title() + sorry_msg5)

popped_guest3 = guest_list.pop(2)
sorry_msg4 = "I'm sorry "
sorry_msg5 = ", \nI can't invite you this time.\nI hope we'll get a chance to make up for this missed occasion soon.\n-MrD\n"
print (sorry_msg4 + popped_guest3.title() + sorry_msg5)

popped_guest4 = guest_list.pop(2)
sorry_msg4 = "I'm sorry "
sorry_msg5 = ", \nI can't invite you this time.\nI hope we'll get a chance to make up for this missed occasion soon.\n-MrD\n"
print (sorry_msg4 + popped_guest4.title() + sorry_msg5)

popped_guest5 = guest_list.pop(2)
sorry_msg4 = "I'm sorry "
sorry_msg5 = ", \nI can't invite you this time.\nI hope we'll get a chance to make up for this missed occasion soon.\n-MrD\n"
print (sorry_msg4 + popped_guest5.title() + sorry_msg5)

still_invited1 = "Dear "
still_invited2 = ",\nJust to let you know: You're still invited.\nI look forward to meeting you.\n-MrD\n"
print (still_invited1 + guest_list[0].title() + still_invited2)
print (still_invited1 + guest_list[1].title() + still_invited2)

del guest_list[0]
del guest_list[0]
print (guest_list)

print (len(guest_list))
guest_list = ['the dread pirate roberts', 'ragnar lothbrok', 'heath ledger', 'jimi hendrix']
guest_list.append('rick')
guest_list.append('morty')
guest_list.append('enrique iglesias')
print (guest_list)
print (len(guest_list))

#3-9 print message with len number
list_message = "\nTonight I'm inviting "
list_message2 = " guests to dinner."
print (list_message, len(guest_list), list_message2)