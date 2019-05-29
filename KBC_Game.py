from random import randint
questions = [
    "1.How many continents are there?",              # pehla question
    "2.What is the capital of India?",            # doosra question
    "3.NG mei kaun se course padhaya jaata hai?"    # teesra question
]

options= [
    #pehle question ke liye options
    ["1. Four", "2. Nine", "3. Seven", "4. Eight"],
    #second question ke liye options
    ["1. Chandigarh", "2. Bhopal", "3. Chennai", "4. Delhi"],
    #third question ke liye options
    ["1. Software Engineering", "2. Counseling", "3. Tourism", "Agriculture"]
]

life_line=["1. Seven",
"1. Delhi",
"1. Software Engineering"]

options2= [
    #pehle question ke liye options
    [ "2. Nine", "3. four", "4. Eight"],
    #second question ke liye options
    ["1. Chandigarh", "2. Bhopal", "3. Chennai"],
    #third question ke liye options
    [ "2. Counseling", "3. Tourism", "Agriculture"]
]



solutions = [3, 4, 1]

Question=0
while Question<len(options):
    print questions[Question]
    
    Option=0
    while Option<=len(options):
        print "\t",options[Question][Option]
        Option=Option+1
        
    userAnswer=input("enter your ans option\t")

    if userAnswer == solutions[Question]:
        print "Congrats! Aapka answer sahi hai"
    elif userAnswer == 5050:
	print randint(0,3)
	print life_line[Question]
        
    else:
        print "Sadly aapka javab galat hai."
    print ' '
    Question=Question+1
