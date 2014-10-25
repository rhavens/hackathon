import os
import pprint
from extra import *



# Loop to start interface
while True:
	os.system('clear') #clear's the screen
	print color.BLUE + color.UNDERLINE + "What Would You Like to Do?" + color.END
	print color.PURPLE + "   [0] = exit"	
	print "   [1] = add class"
	print "   [2] = remove class"
	print "   [3] = view classes"
	print "   [4] = get score"
	print "   [5] = see course lists"
	print color.END


	n = input()
	if n == 1: #Add Class
		os.system('clear')
		classAdder()
		print "Class added successfully!"
		print
		print 
		print
		print "Press return to return"
		hi = raw_input()
	if n == 2:
		os.system('clear')
		print
		print
		removeClass()
		print
		print "Press return to return"
		hi = raw_input()
	if n == 3:
		os.system('clear')
		print "Printing classes! Hellz yea!"
		printUserClasses(userList)
		print
		print 
		print
		print "Press return to return"
		hi = raw_input()
	if n == 4: 
		os.system('clear')
		print "Getting your score..."
		print "Your Score is:", formulaScore(userList)
		print
		shittyScoreRater(formulaScore(userList))
		print
		print "Press return to return"
		hi = raw_input()
	if n == 5:
		os.system('clear')
		print
		print
		print "[1] = Art History Classes"
		print "[2] = Computer Science Courses"
		print
		print
		stuff = input("Choice: ")
		print
		if stuff == 1:
			printClassShit(courseListFAH) 
		if stuff == 2:
			printClassShit(courseListCOMP)
		print
		print "Press return to return"
		hi = raw_input()
	if n == 0:
		break

print "thanks for using me! ;)"
print "see ya!"






