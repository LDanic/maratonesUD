from flask import Flask, render_template, send_file
from gestionEstudiantes import estudiantes_bp
from gestionEquipos import equipos_bp
from gestionCompetencias import competencias_bp

app = Flask(__name__)

# Puedes definir rutas y configuraciones adicionales en app.py

# Monta el blueprint de estudiantes bajo la ruta /api
app.register_blueprint(estudiantes_bp, url_prefix='/api')
app.register_blueprint(equipos_bp, url_prefix='/api')
app.register_blueprint(competencias_bp, url_prefix='/api')

@app.get('/')
def home():
    return render_template("index.html")

@app.get('/Principal.html')
def principal():
    return render_template("Principal.html")

@app.get('/Competencias.html')
def competencias():
    return render_template("Competencias.html")

@app.get('/Equipos.html')
def equipos():
    return render_template("Equipos.html")

@app.get('/Estudiantes.html')
def estudiantes():
    return render_template("Estudiantes.html")

if __name__ == '__main__':
    app.run(debug=True)
