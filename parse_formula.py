import json
from parse_rest.connection import register
from parse_rest.datatypes import Object
from parse_rest.connection import ParseBatcher


APPLICATION_ID = "pLS8KXt2JBvTEvw2JjiQWuA9uaEd3WD3yMxj6U5h"
REST_API_KEY = "mWg4CfKjn0exkvXPh2QSZQmTPjH264AjD4TfnnFN"
MASTER_KEY = "gSylAEmDW1GRP90nCRVBTCgM3Hm94utcgld6LLSV"

register("pLS8KXt2JBvTEvw2JjiQWuA9uaEd3WD3yMxj6U5h", "mWg4CfKjn0exkvXPh2QSZQmTPjH264AjD4TfnnFN" , master_key=MASTER_KEY)

class Course(Object):
    pass



def formula(course):
	return course["level"] / 100.0 + course["hasLab"]/ 2.0 + course["length"]/ 75.0


# courseList = []
# fp = open('cscourses.json')
# course_data = json.load(fp)

# for x in range(0,len(course_data["courses"])):
# 	test = Course(course_id=course_data["courses"][x]["id"], level= course_data["courses"][x]["level"], title=course_data["courses"][x]["title"], lab=int(course_data["courses"][x]["hasLab"]), length=course_data["courses"][x]["length"])
# 	test.save()
# 	print "Name:",course_data["courses"][x]["id"],course_data["courses"][x]["title"]
# 	print "Score:",formula(course_data["courses"][x])
# 	print "______________"



results = Course.Query.all().order_by("level")
dictionary = {"courses":[]}
for result in results:
	dictionary["courses"].append( {"id": str(result.course_id), "level": result.level, "title": str(result.title), "hasLab": result.lab, "length": result.length})
	print result.title


fp = open("allCourses.json","w+")
fp.write(json.dumps(dictionary,indent=4, separators=(',', ': ')))
fp.close()