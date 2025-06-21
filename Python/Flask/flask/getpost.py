from flask import Flask,render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return "<html><h1>Welcome to the Party. Enjoy...!</h1></html>"

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/form",methods =['GET','POST'])
def form():
    if request.method =='POST':
        name = request.form['name']
        return f"Hello {name}"
    return render_template('form.html')

@app.route('/submit-form', methods=['POST'])
def submit_form():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    print(f"Received form data -> Name: {name}, Email: {email}, Message: {message}")
    return f"<h2>Thanks, {name}! Your message was received.</h2>"

@app.route('/about')
def about():
    return render_template('about.html')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4200,debug=True)