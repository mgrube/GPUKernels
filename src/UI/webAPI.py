from flask import Flask
app = Flask(__name__)

@app.route("/")
def default():
	return 'Placeholder.'

if __name__ == "__main__":
	app.run()
