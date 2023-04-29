from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm-password']
    
    # Vérifier si le nom d'utilisateur et l'adresse email sont disponibles
    # Si oui, enregistrer l'utilisateur dans la base de données
    # Sinon, renvoyer un message d'erreur
    
    return redirect(url_for('login'))

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    
    # Vérifier si l'adresse email et le mot de passe sont corrects
    # Si oui, connecter l'utilisateur et renvoyer la page d'accueil
    # Sinon, renvoyer un message d'erreur
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
