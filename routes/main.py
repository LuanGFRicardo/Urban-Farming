from flask import Blueprint, render_template

# Criar um Blueprint
main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

# Função para registrar o Blueprint
def registrar_blueprints(app):
    app.register_blueprint(main)