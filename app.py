# imports
from flask import Flask, request, session, g, redirect, url_for, \
	abort, render_template, flash
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

@app.route('/')
@app.route('/index.html')
def root():
	return render_template('index.html')

@app.route('/contact.html')
def contact():
	return render_template('contact.html')


@app.route('/test', methods=["POST"])
def test():
	return "Nice...\n"

if __name__ == "__main__":
	app.run()