print("\n\nBook your Tickets\n")
restart = ('Y')

while restart != ('N','NO','n','no'):
	print("1.Check PNR status")
	print("2.Reserve Tickets")
	choice = int(input("\nEnter your option : "))

	if choice == 1:
		print("Your PNR status is t3")
		exit(0)

	elif choice == 2:
		no_of_tickets = int(input("\nEnter no. of Ticket you want : "))
		name_list = []
		age_list = []
		sex_list = []
		for p in range(no_of_tickets):
			name1 = str(input("\nPassenger's Name : "))
			name_list.append(name1)
			sex1  = str(input("\nGender - Male or Female : "))
			sex_list.append(sex1)
			age1 = int(input("\nPassenger's Age  : "))
			age_list.append(age1)

		restart = str(input("\nWant to add someone? y/n: "))
		if restart in ('y','YES','yes','Yes'):
			restart = ('Y')
		else :
			x = 0
			print("\nTotal Tickets : ",no_of_tickets)
			for p in range(1,no_of_tickets+1):
				print("Passenger's Ticket : ",p)
				print("Passenger's Name : ", name_list[x])
				print("Passenger's Age  : ", age_list[x])
				print("Passenger's Sex : ",sex_list[x])
				x += 1



	
