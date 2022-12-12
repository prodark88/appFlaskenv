
from flask import Flask, render_template , request
from flask_sqlalchemy import SQLAlchemy

from flask import flask_login   






app = Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


@app.route('/protected')
@flask_login.login_required
def protected():
    return 'Logged in as: ' + flask_login.current_user.id

@app.route('/logout')
def logout():
    flask_login.logout_user()
    return 'Logged out'

#Decoradores
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bienvenido")
def bienvenido(nombre):
    nombre = nombre.upper()
    return render_template('index.html', nombre = nombre)

@app.route("/rutanueva1")
def ruta_nueva():
    return "<h1>Esta es una ruta nueva sin html </h1>"

@app.route("/rutanueva1/rutaHtml")
def ruta_con_html():
    return render_template("nuevo.html")@app.route("/rutanueva1/rutaHtml")

@app.route("/bienvenido/<nombre>")
def bienvenido(nombre):
    nombre = request.args["nombre"]
    nombre = nombre.upper()
    return render_template('index.html', nombre = nombre)

@app.route("/login")
def login():
    form =  loginForm()
    return render_template('login.html', form = form)




#administrador de inicio de sesiones
login_manager = flask_login.LoginManager()
login_manager.init_app(app)


#cargar usuarios
class User(flask_login.UserMixin):
    pass
@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return

    user = User()
    user.id = email
    return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email
    return user

@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'GET':
        return '''
               <form action='login' method='POST'>
                <input type='text' name='email' id='email' placeholder='email'/>
                <input type='password' name='password' id='password' placeholder='password'/>
                <input type='submit' name='submit'/>
               </form>
               '''

    email = flask.request.form['email']
    if email in users and flask.request.form['password'] == users[email]['password']:
        user = User()
        user.id = email
        flask_login.login_user(user)
        return flask.redirect(flask.url_for('protected'))

    return 'Bad login'

@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized', 401



