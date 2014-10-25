def formula(course):
	return course.level / 100.0 + course.lab / 2.0 + course.length / 75.0


class Course(object):
	def __init__(self, level, lab, length):
		self.level = level
		self.lab = lab
		self.length = length


c = Course(20, True, 150)

print(formula(c))