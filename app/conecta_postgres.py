import psycopg2
import time
from flask import Flask
from flask_restx import Api, Resource


app =Flask(__name__)
api =Api(app, version='1.0', title='Aluno API',
         description='API para conectar e consultar dados no PostgreSQL',
         doc='/swagger')

ns = api.namespace('alunos', description='Operações de conexão com PostgeSQL')

def get_connection():
    conn = psycopg2.connect(
        host="db",
        dbname="postgres"
        user="postgres",
        password="senha123"
    )
    return conn
@ns.route('/')
class AlunosList(Resource):
    def get(self):
        time.sleep(5)
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
                CREATE TABLE IF NOT EXISTS alunos(
                    id SERIAL PRIMARY KEY,
                    nome VARCHAR(50)
                    );
                    """)
        conn.commit()
        cur.execute("INSERT INTO alunos (nome) VALUES ('João'), ('Maria'), ('José');")
        conn.commit()

        cur.execute("SELECT * FROM alunos;")
        alunos = cur.fetchall()
        cur.close()
        conn.close()
        return {'alunos': [{'id':alunos[0],'nome':alunos[1]} for aluno in alunos]}