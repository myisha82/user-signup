from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

html = """
<!doctype html>

<html>
<head>
    <style>
        .error {{
            color: red;
        }}
    </style>
</head>

<body>

    </h1>Signup</h1>
    <form action='signup'  method= 'POST'>
        <label>Username</label>
        <input type = "text" name= "user" value = '{4}'/>
        <span class='error'> {0}</span>
        <br />
        <label>Password</label>
        <input type = "password" name = "pass_var" />
        <span class = 'error'>{1} </span>
        <br />
    
        <label> Verify Password </label>
        <input type = "password" name = "verify"/>
        <span class = 'error'>{2}</span>
        <br />

        <label> Email (optional) </label>
        <input type = "text" name = "mail" value = '{5}'/>
        <span class = 'error'>{3}</span>
        <br />

        <input type = "submit" value = "Submit"/>
        
        
    </body>        
</html>
"""




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
            

    return  html.format(user_error, pass_var_error,verify_password_error,mail_error,user,mail)


@app.route("/")
def index():
    return html.format("")

app.run()

