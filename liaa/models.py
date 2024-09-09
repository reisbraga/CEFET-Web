from database import db

class Departamento(db.Model):
    __tablename__ = "Departamentos"
    id_departamento = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    responsavel = db.Column(db.String(100))
    numero_funcionarios = db.Column(db.Integer)

    def __init__(self, nome, responsavel, numero_funcionarios):
        self.nome = nome
        self.responsavel = responsavel
        self.numero_funcionarios = numero_funcionarios

    def __repr__(self):
        return "<Departamentos {}>".format(self.nome)
