import os
from datetime import datetime
from flask import Flask, session, url_for, redirect, render_template, request, abort, flash
from database import db_connect, user_registration, view_posts, analysis, add_post
from database import admin_login, user_login, search_friend, friend_request, get_users_data
from database import accept, reject, view_requests, bot_check, view_predict

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/")
@app.route("/index")
def index_route():
    return render_template("index.html")

@app.route("/user")
def user_route():
       return render_template("user.html")

@app.route("/register")
def register_route():
    return render_template("form.html")

@app.route("/home") 
def home_route():
    return render_template("home.html")

@app.route("/post")
def post_route():
    return render_template("post.html")

@app.route("/posts")
def posts_route():
    username = session['username']
    posts = view_posts(username)
    return render_template("posts.html", posts=posts)

@app.route("/request")
def request_route():
    username = session['username']
    status = friend_request(username, request.args.get('fname'))
    return render_template("home.html")

@app.route("/requests") 
def requests_route():
    username = session['username']
    data = view_requests(username)
    return render_template("requests.html", requests=data)

# --------------- USER END ----------------

@app.route("/admin")
def admin_route():
    return render_template("admin.html")

@app.route("/adminhome") 
def admin_home_route():
    return render_template("admin_home.html")

@app.route("/users") 
def users_route():
    data = get_users_data()
    return render_template("users.html", users=data)

@app.route("/predict") 
def predict_route():
    username = session['username']
    data = view_predict(username)
    return render_template("predict.html", predict=data)

@app.route("/analysis")
def analysis_route():
    username = session['username']
    data = analysis(username)
    return render_template("analysis.html", analysis=data)

# -------------- ADMIN END -------------------

# -------------------------------Registration-----------------------------------------------------------------    
@app.route("/submit", methods=['GET','POST'])
def submit_details_route():
    if request.method == 'POST':
        username = request.form['uname']
        mail = request.form['mail']
        password = request.form['password']
        gender = request.form['gender']
        dob = request.form['dob']
        mobile = request.form['mobile']
        address = request.form['address']
        status = user_registration(username, mail, password, gender, dob, mobile, address)
        if status:
            return render_template("user.html", msg="Success")
        return render_template("form.html", msg="Failed")

@app.route("/add", methods=['GET','POST'])
def add_post_route():
    if request.method == 'POST':
        try:
            username = session['username']
            post = request.form['post']
            status = add_post(username, post)
            result = bot_check(username, post)
            return render_template("post.html")
        except Exception as e:
            return render_template("home.html")

# # -------------------------------Login-----------------------------------------------------------------
@app.route("/adminlogin", methods=['GET', 'POST'])       
def admin_login_route():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        status = admin_login(username, password)
        if status:
            session['username'] = username
            return render_template("admin_home.html", msg="Login Success")
        return render_template("admin.html", msg="Login Failed")

@app.route("/login", methods=['GET', 'POST'])   
def login_route():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        status = user_login(username, password)
        if status:
            session['username'] = username
            return render_template("home.html", msg="Login Success")
        return render_template("user.html", msg="Login Failed")
# # -------------------------------Login-End-----------------------------------------------------------------

@app.route("/search", methods = ['GET','POST']) 
def search_route():
   if request.method == 'POST':      
      data = search_friend(request.form['friend'])
      return render_template("home.html", friends=data)
     
@app.route("/accept")
def accept_route():
    uname = session['username']
    status = accept(uname, request.args.get('fname'))
    if status:
       return render_template("home.html", msg="Success")
    return render_template("requests.html", msg="Failed")

@app.route("/reject")
def reject_route():
    uname = session['username']
    status = reject(uname, request.args.get('fname'))
    if status:
       return render_template("home.html", msg="Success")
    return render_template("requests.html", msg="Failed")

if __name__ == "__main__":
    app.run(debug=True)
