question_list = [
	"How many continents are there?",  			# pehla question
	"What is the capital of India?",			# doosra question
	"NG mei kaun se course padhaya jaata hai?"	# teesra question
]

options_list = [
	#pehle question ke liye options
	["Four", "Nine", "Seven", "Eight"],
	#second question ke liye options
	["Chandigarh", "Bhopal", "Chennai", "Delhi"],
	#third question ke liye options
	["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]

# har ek question ke liye, uski solution key (yeh index nahi hai)
solution_list = [3, 4, 1]

'''print option_list[0]
print option_list[0][0]
print option_list[1][1]
print option_list[1][2]
print option_list[1][3]'''

count = 0
one_time = 0
while count < len(question_list):
	print question_list[count]
	counter  = 0
	number = 1
	while counter < len(options_list[count]):
		print number, options_list[count][counter]
		counter = counter + 1
		number= number+1
	user = int(raw_input(" Enter a answer or use lifeline 5050:-  "))
	if user == 5050 and one_time == 1:
		print "Aready used lifeline"
		print "~~~~~~~~~~~~~~~~~~~~~~~"
		user = int(raw_input(" Enter a answer or use lifeline 5050:-  "))
	elif user == 5050 and one_time == 0:
		one_time = 1
		print count+1, options_list[count][count]
		print solution_list[count], options_list[count][solution_list[count]-1]
		user = int(raw_input("enter answer"))

		if user == solution_list[count]:
			print "congrats"
			print " "
		else:
			print "You loose"
			print "out of the game"
			break
	if  user == solution_list[count]:
		print "congrats"
		
	else:
		print "You loose"
		print "out of the game"
		break
	count = count +1

