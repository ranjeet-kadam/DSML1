from flask import Flask

app1 = Flask(__name__)

@app1.route("/")
def welcome():
    return "Happy Ending...!It's good to see you."

if __name__ =="__main__":
    app1.run(host='0.0.0.0', port=8000,debug=True)
