from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello again. Reload test! Successful done"

@app.route("/index")
def index():
    return "This is the index page.Reload succesfully done"

if __name__ == "__main__":
    app.run(debug=True)
