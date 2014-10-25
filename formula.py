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


courseList = []
size = 0
courseList.append(Course("FAH 2",2, "Art History From 1700 to the Present", 0, 220))
courseList.append(Course("FAH 15", 15, "Japanese Architecture", 0, 150))
courseList.append(Course("FAH 19",19,"Classic Architecture",0,150))
courseList.append(Course("FAH 21",21,"Early Islamic Art",0,150))
courseList.append(Course("FAH 41",41,"The Age of Rembrandt and Bernini",0,150))
courseList.append(Course("FAH 92",92,"Vikings!",0,150))
courseList.append(Course("FAH 98",98,"Senior Integrative Project Seminar",0,150))
courseList.append(Course("FAH 104",104,"Greek Art and Archaeology",0,150))
courseList.append(Course("FAH 120",120,"Armenian Art and Shit",0,150))
courseList.append(Course("FAH 122",122,"Iconoclosm and Shit",0,150))
courseList.append(Course("FAH 193",193,"Histories of Modern Architecture",0,150))
courseList.append(Course("FAH 200",200,"Narrative: Japanese Heroes",0,150))
courseList.append(Course("FAH 280",280,"Photography in Mexico",0,150))
courseList.append(Course("FAH 288",288,"Art!!!",0,150))
size = 14

for x in range(0,size):
	print "Name:",courseList[x].ID,courseList[x].title, "Score:",formula(courseList[x])
	print
	print "		Time (minutes):", courseList[x].length
	print "______________"