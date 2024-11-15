from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Configurare conexiune la baza de date
db_config = {
    'host': 'localhost',
    'user': 'flask_user',       # Înlocuiește cu utilizatorul tău MySQL
    'password': 'parola_flask', # Înlocuiește cu parola ta MySQL
    'database': 'Biblioteca'
}

# Conexiunea la baza de date
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor(dictionary=True)

# Ruta pentru pagina principală
@app.route('/')
def home():
    return render_template('home.html')

# ------------------- RUTE PENTRU TABEL PRINCIPAL -------------------

# Ruta pentru tabelul Gen
@app.route('/genuri')
def genuri():
    cursor.execute("SELECT * FROM Gen")
    genuri = cursor.fetchall()
    return render_template('genuri.html', genuri=genuri)

# Ruta pentru tabelul Autor
@app.route('/autori')
def autori():
    cursor.execute("SELECT * FROM Autor")
    autori = cursor.fetchall()
    return render_template('autori.html', autori=autori)

# Ruta pentru tabelul Editura
@app.route('/edituri')
def edituri():
    cursor.execute("SELECT * FROM Editura")
    edituri = cursor.fetchall()
    return render_template('edituri.html', edituri=edituri)

# Ruta pentru tabelul Editie (sub numele Cărți)
@app.route('/carti')
def carti():
    cursor.execute("SELECT * FROM Editie")
    carti = cursor.fetchall()
    return render_template('carti.html', carti=carti)

# Ruta pentru tabelul Exemplar
@app.route('/exemplare')
def exemplare():
    cursor.execute("SELECT * FROM Exemplar")
    exemplare = cursor.fetchall()
    return render_template('exemplare.html', exemplare=exemplare)

# Ruta pentru tabelul Imprumut
@app.route('/imprumuturi')
def imprumuturi():
    cursor.execute("SELECT * FROM Imprumut")
    imprumuturi = cursor.fetchall()
    return render_template('imprumuturi.html', imprumuturi=imprumuturi)

# Ruta pentru tabelul Cititor
@app.route('/cititori')
def cititori():
    cursor.execute("SELECT * FROM Cititor")
    cititori = cursor.fetchall()
    return render_template('cititori.html', cititori=cititori)

# Ruta pentru tabelul Sala
@app.route('/sali')
def sali():
    cursor.execute("SELECT * FROM Sala")
    sali = cursor.fetchall()
    return render_template('sali.html', sali=sali)

# ------------------- MAIN -------------------

if __name__ == '__main__':
    app.run(debug=True)
