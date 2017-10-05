from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True  

@app.route("/validate", methods=['POST'])
def validate():
    username_add = request.form['username']
    password_add = request.form['password']
    verify_add = request.form['verify']
    email_add = request.form['email']

    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

    #test if username is blank
    if username_add == "":
        username_error= "User name cannot be blank." 
        username_add = ""

    #test if username has spaces
    elif " " in username_add:
        username_error = "Username cannot contain spaces."
        username_add = "" 

    #test length of username
    else:
        if len(username_add) < 3 or len(username_add) > 20:
            username_error = "User name must have at least 3 characters and fewer than 20."
            username_add = ""

    #Test if password is blank
    if password_add == "":
        password_error = "Password cannot be blank."
        password_add = ""
    
    #test if password has spaces
    elif " " in password_add:
        password_error = "Password cannot contain spaces."
        password_add = ""

    #test password length
    else:
        if len(password_add) < 3 or len(password_add) >20:
            password_error = "Password must have at least 3 characters and fewer than 20"
            password_add = ""

    #test if passwords match
    if password_add != verify_add:
        verify_error = "Passwords must match."
        password_error = "Passwords must match."

    #test for valid email
    if '@' not in email_add or '.' not in email_add:
        email_error = "Email is not valid. It must contain an '@' and a '.'"
        email_add = ""

    if " " in email_add:
        email_error = "Emain is not valid. It cannot contain spaces."
        email_add = ""

    if len(email_add) < 3 or len(email_add) > 20:
        email_error = "Email is not valid. It must be between 3 and 20 characters long."
        email_add = ""

    if not username_error and not password_error and not verify_error and not email_error:
        return render_template('welcome.html', username=username_add)
    else:
        return render_template('home.html', username=username_add, email=email_add, username_error=username_error, 
            password_error=password_error, verify_error=verify_error, email_error=email_error)
 

@app.route("/")
def index():
    return render_template('home.html')


app.run()