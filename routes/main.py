from flask import Blueprint, render_template

# Criar um Blueprint com o nome 'main'
bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return render_template('home.html')