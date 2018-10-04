from flask import Flask, request, redirect, render_template
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/welcome", methods=['POST'])
def welcome():
    return render_template('welcome.html')


@app.route("/signup",  methods=['POST'])
def signup():
    user = request.form['user']
    user_error = ''
    
    if ' ' in user:
        user_error = 'No spaces allowed in username'
        
    if len(user) < 3 or len(user)> 20:
       user_error = 'Username must be at least three characters and no more than twenty characters'
       
       
    pass_var = request.form['pass_var']  
    pass_var_error = ''  
    if pass_var.isspace():
       pass_var_error = 'No spaces allowed in password'
    
    if len(pass_var) < 3 or len(pass_var)> 20:
        pass_var_error = 'Password must be at least three characters and no more than twenty characters'   
         

    verify_password = request.form['verify']
    verify_password_error = ''

    if len(verify_password) == 0:
        verify_password_error = 'Verify password field can not be empty'
    if verify_password != pass_var:
        verify_password_error = 'Password does not match'
        

    mail = request.form['mail']  
    mail_error = '' 
    
    if mail.isspace():
        mail_error = 'No spaces allowed in email'

    #check to see if email contains @ . 
    if '@' not in mail or '.' not in mail:
        mail_error = 'Invalid email address expecting @/.'
    else:
        if len(mail) < 3 or len(mail) > 20:
            mail_error = 'Email must be at least three characters and no more than twenty characters'   


    #Check If Any Failures        
    if len(user_error) > 0 or len(pass_var_error) > 0 or len(verify_password_error) > 0 or len(mail_error) > 0: 
        #Passing variables to signup_form html page
        return  render_template('signup_form.html', 
            user_html = user, 
            user_error_html = user_error, 
            
            pass_var_error_html = pass_var_error, 
            
            verify_error_html = verify_password_error,
            mail_html = mail,
            mail_error_html = mail_error)
     
    else:
        return render_template('welcome.html', name = user)    


@app.route("/")
def index():
    return render_template('signup_form.html') #html.format("")

app.run()

