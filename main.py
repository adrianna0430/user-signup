from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True



@app.route('/')
def index():
    return render_template('home-page.html')

@app.route('/')
def request_signup_info():
    return render_template('home-page.html', username='', username_error='', password='', password_error='', verify_password='', verify_pass_error='', email='', email_error='')

@app.route('/', methods=['POST'])
def validate_signup():
    username= request.form['username']
    password= request.form['password']
    verify_password=request.form['verify_password']
    email= request.form['email']

    username_error=''
    password_error=''
    verify_pass_error=''
    email_error=''
    #value=undefined in username, password, and verify password
    if len(username)==0:
        username_error="Username must not be blank."
    if (len(username)>0 and len(username)<3) or len(username)>20:
        username_error= "Username must be between 3 and 20 characters."
    for i in range(len(username)):
        if username[i] == ' ':
            username_error= "Username cannot contain spaces."
            break
    
    if len(password)==0:
        password_error="Password cannot be blank."
        password=''
    if  (len(password)>0 and len(password)<3) or len(password)>20:
        password_error= "Passwords must be between 3 and 20 characters."
        password=''
    for i in range(len(password)):
        if password[i] == ' ':
            password_error= "Passwords cannot contain spaces."
            password=''
            break
    if password != verify_password: 
        verify_pass_error= "Passwords don't match."
        password=''
        verify_password=''
    
    if (len(email)>0 and len(email)<3) or len(email)>20:
        email_error= "Email addresses must contain between 3 and 20 characters."
    elif (len(email)>0) and (email.count('@')!=1 or email.count('.')!=1):
        email_error= "Email addresses must include 1 @ symbol and 1 period."
    for i in range(len(email)):
        if (len(email)>0) and email[i] == ' ':
            email_error= "Emails cannot contain spaces."
            break

    if not username_error and not password_error and not verify_pass_error and not email_error:
        #redirect to welcome pages
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('home-page.html', username=username, username_error=username_error, password=password, password_error=password_error, verify_password=verify_password, verify_pass_error=verify_pass_error, email=email, email_error=email_error)

@app.route('/welcome')
def welcome_page():
    username=request.args.get('username')
    return render_template('welcome-page.html', username=username)


app.run()