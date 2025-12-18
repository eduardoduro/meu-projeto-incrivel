from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Configurações de Segurança
app.config["JWT_SECRET_KEY"] = "sua_chave_secreta_super_segura" 
jwt = JWTManager(app)

# Simulando um Banco de Dados de usuários
users_db = {}

# --- ROTA DE REGISTRO ---
@app.route('/auth/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if email in users_db:
        return jsonify({"msg": "Usuário já existe"}), 400

    # Criando o HASH da senha antes de salvar
    hashed_password = generate_password_hash(password)
    users_db[email] = {"password": hashed_password}

    return jsonify({"msg": "Usuário criado com sucesso!"}), 201

# --- ROTA DE LOGIN ---
@app.route('/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = users_db.get(email)
    
    # Verifica se o usuário existe e se a senha (hash) bate
    if user and check_password_hash(user['password'], password):
        # Cria o Token JWT
        access_token = create_access_token(identity=email)
        return jsonify(access_token=access_token), 200
    
    return jsonify({"msg": "E-mail ou senha incorretos"}), 401

if __name__ == '__main__':
    app.run(debug=True)