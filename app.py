# imports
from flask import Flask, request, session, g, redirect, url_for, \
	abort, render_template, flash
from flask_wtf import Form
from wtforms import StringField, IntegerField, SelectField, TextAreaField
from wtforms.validators import DataRequired
from indicoio import sentiment

WTF_CSRF_ENABLED = False

import json
from parse_rest.connection import register
from parse_rest.datatypes import Object
from parse_rest.connection import ParseBatcher

APPLICATION_ID = "pLS8KXt2JBvTEvw2JjiQWuA9uaEd3WD3yMxj6U5h"
REST_API_KEY = "mWg4CfKjn0exkvXPh2QSZQmTPjH264AjD4TfnnFN"
MASTER_KEY = "gSylAEmDW1GRP90nCRVBTCgM3Hm94utcgld6LLSV"

register(APPLICATION_ID, REST_API_KEY, master_key=MASTER_KEY)

class Course(Object):
    pass

app = Flask(__name__, static_url_path='/home/ryan/Documents/PROJECTS/hackathon2/hackathon/static/')
app.config.from_object(__name__)
app.secret_key = 'chiave'

course_ids = []
difficulties = [(1,"Very easy"),(2,"Easy"),(3,"Medium"),(4,"Hard"),(5,"Very hard")]
for course in Course.Query.all().order_by("-course_id"):
	course_ids.append((course.course_id, course.course_id+" "+course.title))

def update_course(id, diff):
	courseS = Course.Query.get(course_id = id)
	courseS.difficulty = float("{0:.2f}".format((courseS.difficulty * courseS.num_reviews + diff) / (courseS.num_reviews + 1)))
	courseS.num_reviews = courseS.num_reviews + 1
	courseS.save()

class MyForm(Form):
	def __init__(self, *args, **kwargs):
		kwargs['csrf_enabled'] = False
		super(MyForm, self).__init__(*args, **kwargs)
	course_id = SelectField('course_id', choices=course_ids)
	difficulty = SelectField('difficulty', choices=difficulties)
	text = TextAreaField('text')

@app.route('/')
@app.route('/index.html')
def root():
	return render_template('index.html', Course=Course)

@app.route('/contact.html')
def contact():
	return render_template('contact.html')

@app.route('/about.html')
def about():
	return render_template('about.html')

msg = ""
@app.route('/rate.html', methods=['GET','POST'])
def rate():
	msg = ""
	form = MyForm(csrf_enabled=False)
	print(form)
	if request.method == "POST":
		if len(request.form['text']) > 20:
			if sentiment(request.form['text']) == "positive":
				update_course(request.form['course_id'], int(request.form['difficulty']) - (0 + int(request.form['difficulty'])) / 5.0)
			else:
				update_course(request.form['course_id'], int(request.form['difficulty']) + (5 - int(request.form['difficulty'])) / 5.0)
		update_course(request.form['course_id'], int(request.form['difficulty']))
		msg = "Thank you for your submission!"
	else:
		msg = "Enter your submission:"
	return render_template('rate.html', form=form, Course=Course, msg=msg)

@app.route('/test', methods=["POST"])
def test():
	return "Nice...\n"

if __name__ == "__main__":
	app.debug = True
	app.run()