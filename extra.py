import os
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
def formula(course):
	return course.level / 100.0 + course.haslab / 2.0 + course.length / 75.0

class Course(object):
	def __init__(self, ID, level, title, haslab, length):
		self.ID = ID
		self.level = level
		self.title = title
		self.haslab = haslab
		self.length = length
	def thing(self):
		print(ID,level,title,haslab,length)

courseListFAH = []
courseListCOMP = []
userList = []

courseListFAH.append(Course("FAH 2",2, "Art History From 1700 to the Present", 0, 220))
courseListFAH.append(Course("FAH 15", 15, "Japanese Architecture", 0, 150))
courseListFAH.append(Course("FAH 19",19,"Classic Architecture",0,150))
courseListFAH.append(Course("FAH 21",21,"Early Islamic Art",0,150))
courseListFAH.append(Course("FAH 41",41,"The Age of Rembrandt and Bernini",0,150))
courseListFAH.append(Course("FAH 92",92,"Vikings!",0,150))
courseListFAH.append(Course("FAH 98",98,"Senior Integrative Project Seminar",0,150))
courseListFAH.append(Course("FAH 104",104,"Greek Art and Archaeology",0,150))
courseListFAH.append(Course("FAH 120",120,"Armenian Art and Shit",0,150))
courseListFAH.append(Course("FAH 122",122,"Iconoclosm and Shit",0,150))
courseListFAH.append(Course("FAH 193",193,"Histories of Modern Architecture",0,150))
courseListFAH.append(Course("FAH 200",200,"Narrative: Japanese Heroes",0,150))
courseListFAH.append(Course("FAH 280",280,"Photography in Mexico",0,150))
courseListFAH.append(Course("FAH 288",288,"Art!!!",0,150))
courseListCOMP.append(Course("COMP 11",11,"Intro to Computer Programming",0,150))
courseListCOMP.append(Course("COMP 15",15,"Data Structures",0,150))
courseListCOMP.append(Course("COMP 20",20,"Web Programming",0,150))
courseListCOMP.append(Course("COMP 40",40,"You know...",0,150))
courseListCOMP.append(Course("COMP 61",61,"Discrete Mathematics",0,150))
courseListCOMP.append(Course("COMP 97",97,"Senior Capstone Project",0,150))
courseListCOMP.append(Course("COMP 105",105,"Programming Languagues",0,150))
courseListCOMP.append(Course("COMP 111",111,"Operating Systems",0,150))
courseListCOMP.append(Course("COMP 116",116,"Intro to Computer Security",0,150))
courseListCOMP.append(Course("COMP 135",135,"Intro to Machine Learnign",0,150))
courseListCOMP.append(Course("COMP 136",136,"Statistical Program Recognition",0,150))
courseListCOMP.append(Course("COMP 160",160,"Algorithms",0,150))
courseListCOMP.append(Course("COMP 163",163,"Computational Geometry",0,150))
courseListCOMP.append(Course("COMP 193",193,"Algorithmic Lower Bounds",0,150))


def shittyScoreRater(score):
	print "TCOC rating: "
	if score < 5:
		print color.RED,"Your Schedule is so Easy it would get laid at a Hackathon",color.END
		return
	if score < 10:
		print color.BLUE,"Congrats, your score could not be mediocre. Don't worry, you're still special, just like your mom said you were",color.END
		return
	if score < 15:
		print color.GREEN,"Your schedule is decent...if you're a wimp",color.END
		return
	if score < 20: 
		print color.RED,color.BOLD,"WHY YOU HAVE TO DO THIS TO YO SELF? WHY!?",color.END
		return

def printClassShit(temp):
	for x in range(0,len(temp)):
		print color.GREEN,x+1,"-","Name:",temp[x].ID,temp[x].title," || ","Score:",formula(temp[x]),color.END



def printClass(temp):
		print "__________________________________"
		print "Name:",temp.ID,temp.title
		print "Difficulty:",formula(temp)
		print "__________________________________"

def printer():
	for x in range(0,len(courseList)):
		print "Name:",courseList[x].ID,courseList[x].title
		print "Score:",formula(courseList[x])
		print
		print "		Time (minutes):", courseList[x].length
		print "__________________________________"

def printRank():
	for x in range(0,len(courseList)):
		print color.GREEN,"Name:",courseList[x].ID,courseList[x].title, "Score:",formula(courseList[x])
	print color.END



def printUserClasses(tempArray):
	for x in range(0,len(tempArray)):
		printClass(tempArray[x])

def formulaScore(tempArray):
	sum = 0
	for x in range(0,len(tempArray)):
		sum = sum + formula(tempArray[x])
	return sum

def removeClass():
	os.system('clear')
	print color.BOLD,color.RED,"Here are your classes:",color.END
	printUserClasses(userList)
	print
	removed = input("Which class would you like to remove? ")-1
	classToRemove = userList[removed]
	userList.remove(classToRemove)
	print classToRemove.ID,classToRemove.title,"was removed"



def classAdder():
	print color.BOLD,color.BLUE,"Would you like a Fine Arts Class or a Computer Science Class?",color.END
	print color.RED,"[1] = Fine Arts"
	print " [2] = Computer Science",color.END
	choice = input("Choice:")
	if choice == 1:
		print "You chose Fine Arts...Why?"
		print "List of Fine Arts Classes offered:"
		print
		printClassShit(courseListFAH)
	if choice == 2:
		print "You chose Computer Science. You have seen the light."
		print "List of Computer Science classes offered:"
		print
		printClassShit(courseListCOMP)
	print 
	print "Pick a class!"
	temp = 0
	temp = input("")
	print
	print "You Picked:"
	if choice == 2:
		print '\033[1m' + courseListCOMP[temp-1].ID,courseListCOMP[temp-1].title
		print 'Difficulty:',formula(courseListCOMP[temp-1])
		print '\033[0m'	
	if choice == 1:
		print '\033[1m' + courseListFAH[temp-1].ID,courseListFAH[temp-1].title
		print 'Difficulty:',formula(courseListFAH[temp-1])
		print '\033[0m'	
	print "Adding class..."
	if choice == 1:
		userList.append(courseListFAH[temp-1])
	if choice == 2:
		userList.append(courseListCOMP[temp-1])


