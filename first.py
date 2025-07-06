from flask import Flask

app = Flask(__name__)

@app.route("/")
def  lwinfo():
	return "i am Linux"

app.run(host="0.0.0.0")