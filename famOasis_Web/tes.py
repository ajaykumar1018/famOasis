from flask import Flask, render_template, request, session, redirect, url_for, flash, session

from flask_sqlalchemy import SQLAlchemy
#from dh import calll
import datetime

# app = Flask(__name__, static_url_path='/static')
app = Flask(__name__)

app.config['SECRET_KEY'] = 'qwertyasdf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///answers.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class answers (db.Model):
    id = db.Column("id", db.Integer, primary_key = True)
    date = db.Column("date",db.String(100))
    username = db.Column("username",db.String(100))
    threeGoodThings = db.Column("threeGoodThings",db.Text)
    sleepHours = db.Column("sleepHours",db.Integer)
    howFeel = db.Column("howFeel", db.Text)
    pleasureThings = db.Column("pleasureThings",db.Integer)
    appetite = db.Column("appetite",db.Integer)
    feelBad = db.Column("feelBad",db.Integer)
    mood = db.Column("mood",db.Integer)


    def __init__(self,date,username,threeGoodThings,sleepHours,howFeel,pleasureThings,appetite,feelBad,mood):
        self.date = date
        self.username = username
        self.threeGoodThings = threeGoodThings
        self.sleepHours = sleepHours
        self.howFeel = howFeel
        self.pleasureThings = pleasureThings
        self.appetite = appetite
        self.feelBad = feelBad
        self.mood = mood


class User (db.Model):
    id = db.Column("id", db.Integer, primary_key = True)
    name = db.Column("name",db.String(1000))
    age = db.Column("age",db.Integer)
    username = db.Column("username",db.String(100))
    password = db.Column("password",db.String(100))
    email = db.Column("email",db.String(100))

    def __init__(self,name,age,username,password,email):
        self.name = name
        self.age = age
        self.username = username
        self.password = password
        self.email = email


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/login", methods=["POST","GET"])
def loginp():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        uname = User.query.filter_by(username=username).first()
        passw = User.query.filter_by(password=password).first()
        if uname is None or passw is None:
            flash("Incorrect Username or password")
            return redirect(url_for("login"))
        elif uname.username == username and passw.password == password:
            session["username"] = username
            return redirect(url_for("mhealth"))
    return redirect(url_for("login"))

@app.route("/mhealth")
def mhealth():
    return render_template("mhealth.html")

@app.route("/mhealth", methods=["POST","GET"])
def mhealthp():
    if request.method == "POST":
        x = str(datetime.datetime.now())
        date = x[0:19]
        uname = session["username"]
        tgt = request.form["threeGoodThings"]
        sho = request.form["sleepHours"]
        hfe = request.form["howFeel"] 
        plet = request.form["pleasureThings"]
        apeti = request.form["appetite"]
        feb = request.form["feelBad"]
        moo = request.form["mood"]
        adat = answers(date,uname,tgt,sho,hfe,plet,apeti,feb,moo)
        db.session.add(adat)
        db.session.commit()    
        #calll(tgt)
    return redirect(url_for("profile"))

@app.route("/view")
def view():
    return render_template("view.html", values= answers.query.all())

@app.route("/signup")
def signup():
    return render_template("signup.html")
@app.route("/signup", methods=["POST","GET"])
def signupp():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]
        adat = User(name,age,username,password,email)
        db.session.add(adat)
        db.session.commit()
        flash('Account Created, Please Login!!')
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    return render_template("index.html")

@app.route("/profile")
def profile():
    #User.query.filter_by(username=session['username']).first().name
    values=[User.query.filter_by(username=session['username']).first(), answers.query.filter_by(username=session['username']).all() ]
    user = User.query.filter_by(username=session['username']).first()
    ans = answers.query.filter_by(username=session['username']).all()
    return render_template("profile.html", user=user,ans=ans )

if __name__ == "__main__":
    db.create_all()
    #app.run(host='0.0.0.0')
    app.run(debug=True)