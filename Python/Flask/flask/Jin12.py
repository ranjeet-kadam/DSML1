from flask import Flask,render_template,request,redirect,url_for

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

#Variable Rule
@app.route('/success/<int:score>')
def success(score):
    res =""
    if score>=50:
        res="Passed"
    else:
        res="Failed"

    return render_template("success.html",results=res)

@app.route('/success_res/<int:score>')
def successres(score):
    res =""
    if score>=50:
        res="Passed"
    else:
        res="Failed"
    exp = {'score': score,'res':res}
    return render_template("result.html",results=exp)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/fail/<int:score>')
def fail(score):
    return render_template("result.html",results=score)

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score = 0
    if request.method=="POST":
        science =float(request.form['science'])
        maths =float(request.form['maths'])
        c =float(request.form['c'])
        data_science =float(request.form['datascience'])

        total_score = (science + maths + c + data_science)/4
        return redirect(url_for('success_res',score = total_score))
    


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6800,debug=True)