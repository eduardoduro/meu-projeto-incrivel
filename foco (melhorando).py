from flask import Flask, request, jsonify
from models import db, Progresso

app = Flask(__name__)

# Configuração da URL do PostgreSQL (No Render, você usará a variável de ambiente)
app.config['SQLALCHEMY_DATABASE_DATABASE_URI'] = 'postgresql://usuario:senha@localhost:5432/nome_do_banco'
db.init_app(app)

@app.route('/progresso', methods=['POST'])
def adicionar_progresso():
    dados = request.json
    novo_registro = Progresso(
        aluno_nome=dados['nome'],
        nota_anterior=dados['nota_anterior'],
        nota_atual=dados['nota_atual']
    )
    db.session.add(novo_registro)
    db.session.commit()
    
    return jsonify({
        "mensagem": "Dados registrados!",
        "analise": novo_registro.status_melhora()
    })

if __name__ == '__main__':
    with app.app_context():
        db.create_all() # Cria as tabelas automaticamente
    app.run(debug=True)