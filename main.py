from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True  

@app.route("/validate", methods=['POST'])
def validate():
    username_add = request.form['username']
    password_add = request.form['password']
    verify_add = request.form['verify']

    username_error = ""
    password_error = ""
    verify_error = ""

    if username_add == "":
        username_error= "User name cannot be blank." 
        username_add = ""

    else:
        if len(username_add) < 3 or len(username_add) > 20:
            username_error = "User name must have at least 3 characters and fewer than 20."
            username_add = ""

    if not username_error:
        return redirect("/welcome")
    else:
        return render_template('home.html', username=username_add, username_error=username_error)
 
@app.route("/welcome", methods=['POST'])
def welcome():
    username = request.form['username']
    return render_template('welcome.html', username=username)


@app.route("/")
def index():
    return render_template('home.html')


app.run()