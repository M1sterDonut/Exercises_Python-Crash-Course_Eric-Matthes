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
guest_list.append('enrique iglesias')
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