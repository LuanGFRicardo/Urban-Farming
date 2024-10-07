# app.py
from flask import Flask
from routes.auth import bp as auth_bp
from routes.main import bp as main_bp

def registrar_blueprints(app):
    """Função para registrar todos os blueprints na aplicação."""
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

def criar_app():
    """Função para criar a instância da aplicação Flask."""
    app = Flask(__name__)

    # Configurações do Flask (exemplo)
    app.config['SECRET_KEY'] = 'sua_chave_secreta'

    # Registrar as blueprints
    registrar_blueprints(app)

    return app

if __name__ == '__main__':
    app = criar_app()
    app.run(debug=True)  # Executar a aplicação com modo de depuração