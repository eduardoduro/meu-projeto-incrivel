from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/essays/<int:id>/grade', methods=['PUT'])
def update_grade(id):
    # 1. Buscar a redação pelo ID
    essay = Essay.query.get_or_404(id)
    
    # 2. Obter os dados enviados pelo Postman/Frontend
    data = request.get_json()
    
    # 3. Validar e atualizar os campos
    if 'grade' in data:
        essay.grade = data['grade']
    if 'comment' in data:
        essay.comment = data['comment']
    
    # 4. Salvar no PostgreSQL
    db.session.commit()
    
    return jsonify({
        "message": "Correção enviada com sucesso!",
        "essay_id": essay.id,
        "new_grade": essay.grade
    }), 200