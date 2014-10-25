# imports
from flask import Flask, request, session, g, redirect, url_for, \
	abort, render_template, flash

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