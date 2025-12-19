from database import db

class Aluno(db.Model):
    __tablename__ = 'alunos'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    objetivo = db.Column(db.String(255), nullable=False)  # O foco da sua atividade

    def to_dict(self):
        return {"id": self.id, "nome": self.nome, "objetivo": self.objetivo}