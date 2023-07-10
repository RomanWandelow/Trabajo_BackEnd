from flask import Flask
from flask import render_template
from flask import Request
from flaskext.mysql import MySQL


app = Flask(__name__, template_folder='templates')

mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] ='localhost'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] ='1234'
app.config['MYSQL_DATABASE_DB'] = 'alumnos'
mysql.init_app(app)

sql = 'SELECT * FROM alumnos;'
conex = mysql.connect()
cursor = conex.cursor()
cursor.execute(sql)

alumnos = cursor.fetchall()
cursor.close()


@app.route('/')
def index(): #Funcion
    return render_template ('index.html', alumnos_jinja = alumnos)

@app.route('/create')
def crearAlumno(): #Funcion crear un Alumno
    return render_template ('create.html', alumnos_jinja = alumnos)

@app.route('/guardar', methods=['POST'])
def guadar():
    tipo = Request.form['tipo']
    estado = Request.form['estado']

    print(tipo)
    print(estado)
    
    return "Alumno guardado"

if __name__ == '__main__':
    app.run(debug=True, port=8000)