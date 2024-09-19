# pip install flask
# pip install Flask-SQLAlchemy
# pip install Flask-Migrate
# pip install Flask-Script
# pip install pymysql
# flask db init
# flask db migrate -m "Migração Inicial"
# flask db upgrade

# flask run --debug

#delete from 'tabela' where 0;


from flask import Flask, render_template, request, flash, redirect
app = Flask(__name__)
from database import db
from flask_migrate import Migrate
from models import Departamento
#do aquivo database.py importa o db
app.config['SECRET_KEY'] = 'JHG8BJXKSAJK-0j-JKhjn87'

#drive://usuario:senha@servidor/banco_de_dados
conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/flaskg2"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def index():
    u = Departamento.query.all()
    return render_template('departamento_lista.html', dados = u)




@app.route('/departamento')
def departamento():
    u = Departamento.query.all()
    return render_template('departamento_lista.html', dados = u)

@app.route('/departamento/add')
def departamento_add():
    return render_template('departamento_add.html')

@app.route('/departamento/save', methods=['POST'])
def departamento_save():
    nome = request.form.get('nome')
    responsavel = request.form.get('responsavel')
    numero_funcionarios = request.form.get('numero_funcionarios')
    if nome and responsavel and numero_funcionarios:
        departamento = Departamento(nome, responsavel, numero_funcionarios)
        db.session.add(departamento)
        db.session.commit() # salva
        flash('Usuario cadastrado com sucesso')
        return redirect('/departamento')
    else:
        flash('Preencha todos os campos!!!')
        return redirect('/departamento/add')








if __name__ == '__main__':
    app.run()