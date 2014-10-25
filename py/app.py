from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	return url_for('static', filename='../html/index.html')

@app.route('/test', methods=["POST"])
def test():
	return "Nice...\n"

if __name__ == "__main__":
	app.run()