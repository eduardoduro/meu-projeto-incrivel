from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/enviar-redacao', methods=['POST'])
def enviar_redacao():
    data = request.get_json()
    texto_redacao = data.get('conteudo', '')

    # Regra de Negócio: Validação de caracteres
    if len(texto_redacao) < 50:
        return jsonify({
            "erro": "A redação é muito curta.",
            "mensagem": f"A redação possui apenas {len(texto_redacao)} caracteres. O mínimo exigido é 50."
        }), 400

    # Se passar na validação, segue para salvar no PostgreSQL
    # Ex: db.session.add(nova_redacao)...
    return jsonify({"mensagem": "Redação enviada com sucesso!"}), 201