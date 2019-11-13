# Linguagem de Programação II
# AC08 ADS2D - LMS
# alunos: tiago.souza@aluno.faculdadeimpacta.com.br
#         diego.farina@aluno.faculdadeimpacta.com.br

from lms import (engine, Usuario, Aluno, Professor,
                 Coordenador, Disciplina, Curso)
from sqlalchemy.orm import sessionmaker
from typing import List, Dict

# Setup: não alterar
Session = sessionmaker(engine)
ses = Session()

# Funções de Query para implementar


def lista_logins() -> List[str]:
    '''
    retorna uma lista com todos os logins de Usuarios presentes no banco.
    '''
    Session = sessionmaker(engine)
    ses = Session()
    logins = ses.query(Usuario).all()
    lista_logins = []
    for i in logins:
        lista_logins.append(i.id_login)
    return lista_logins


def lista_alunos() -> List[str]:
    '''
    retorna uma lista com os nomes de todos os Alunos do banco.
    '''
    Session = sessionmaker(engine)
    ses = Session()
    alunos = ses.query(Aluno).all()
    lista_alunos = []
    for i in alunos:
        lista_alunos.append(i.nome)
    return lista_alunos


def lista_cursos() -> List[str]:
    '''
    retorna uma lista com os nomes de todos os Cursos do banco.
    '''
    Session = sessionmaker(engine)
    ses = Session()
    cursos = ses.query(Curso).all()
    lista_cursos = []
    for i in cursos:
        lista_cursos.append(i.nome)
    return lista_cursos


def lista_professores() -> List[str]:
    '''
    retorna uma lista com os apelidos de todos os professores do banco.
    '''
    Session = sessionmaker(engine)
    ses = Session()
    professores = ses.query(Professor).all()
    lista_professores = []
    for i in professores:
        lista_professores.append(i.apelido)
    return lista_professores


def lista_coordenadores() -> List[str]:
    '''
    retorna uma lista com os nomes de todos os coordenadores do banco.
    '''
    Session = sessionmaker(engine)
    ses = Session()
    coordenadores = ses.query(Coordenador).all()
    lista_coordenadores = []
    for i in coordenadores:
        lista_coordenadores.append(i.nome)
    return lista_coordenadores


def lista_disciplinas() -> List[str]:
    '''
    retorna uma lista com o nome de todas as Discplinas do banco.
    '''
    Session = sessionmaker(engine)
    ses = Session()
    disciplinas = ses.query(Disciplina).all()
    lista_disciplinas = []
    for i in disciplinas:
        lista_disciplinas.append(i.nome)
    return lista_disciplinas


def carga_horaria_total() -> int:
    '''
    retorna a soma da carga horária de todas as diciplinas do banco
    '''
    Session = sessionmaker(engine)
    ses = Session()
    disciplinas = ses.query(Disciplina).all()
    total_ch = 0
    for i in disciplinas:
        total_ch += i.carga_horaria
    return total_ch


def monta_coordenadores() -> Dict[str, List[str]]:
    '''
    Retorna um dicionario cujo as chaves são os nome dos
    coordenadores, e o valor é uma lista com os nomes das
    disciplinas que ele coordena. Caso um professor não coordene
    nenhuma diciplina o valor é uma lista vazia.
    '''
    Session = sessionmaker(engine)
    ses = Session()
    coordenadores = ses.query(Coordenador).all()
    disciplinas = ses.query(Disciplina).all()
    ret = {}
    for i in coordenadores:
        lista_discp = []
        for x in disciplinas:
            if i.id_coordenador == x.id_coordenador:
                lista_discp.append(x.nome)
        ret[i.nome] = lista_discp
    return ret


if __name__ == '__main__':
    # Use esta área para testar sua funções, compare o resultado
    # obtido aqui com o feito direto com SELECT no SQL SERVER
    print(lista_logins())
    print(lista_alunos())
    print(lista_cursos())
    print(lista_professores())
    print(lista_coordenadores())
    print(lista_disciplinas())
    print(carga_horaria_total())
    print(monta_coordenadores())
