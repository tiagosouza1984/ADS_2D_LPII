# Linguagem de Programação II
# AC08 ADS2D - LMS
# alunos: tiago.souza@aluno.faculdadeimpacta.com.br
#         diego.farina@aluno.faculdadeimpacta.com.br

from sqlalchemy import (create_engine, MetaData, Column, Integer, String,
                        ForeignKey, Date, SmallInteger)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

# Setup do ambiente - Não é preciso alterar
load_dotenv()

# modifique o arquivo .env com os seus dados para realizar a conexão
user = os.environ.get("DB_USER")
pwd = os.environ.get("DB_PASS")
server = os.environ.get("DB_HOST")

engine = create_engine(f"mssql+pymssql://{user}:{pwd}@{server}/LMS_Database")
# engine = create_engine(f"mssql+pymssql://
# sa:Tiago@Souza1984@localhost/LMS_Database")
Base = declarative_base(bind=engine, metadata=MetaData(schema="lms"))

# Classes a serem criadas
# Crie todos os atributos (colunas) para as classes abaixo, e
# também  implemente o método __repr__


class Usuario(Base):
    '''
    Classe Usuario: mapeia a tabela usuário do Banco de dados
    '''
    __tablename__ = 'Usuario'
    id_usuario = Column(
        'idUsuario', SmallInteger, autoincrement=True, primary_key=True
    )
    id_login = Column('idLogin', String(30), nullable=False)
    senha = Column('Senha', String(30))
    dt_expiracao = Column('DtExpiracao', Date)
    aluno = relationship('Aluno', backref='usuario')
    coordenador = relationship('Coordenador', backref='usuario')
    professor = relationship('Professor', backref='usuario')

    def __repr__(self):
        '''
        Método de representação do objeto
        '''
        return f"<Usuario({self.id_usuario}): {self.id_login}>"


class Aluno(Base):
    '''
    Classe Aluno: mapeia a tabela Aluno do Banco de Dados
    possui um realacionamento com Usuario de nome usuario, e cria
    a backref perfil_aluno.
    '''
    __tablename__ = 'Aluno'
    id_aluno = Column(
        'idAluno', SmallInteger, autoincrement=True, nullable=False,
        primary_key=True
    )
    id_usuario = Column(
        'idUsuario', SmallInteger, ForeignKey('Usuario.idUsuario'),
        nullable=False
    )
    nome = Column('Nome', String(100), nullable=False)
    email = Column('Email', String(50), nullable=False, unique=True)
    celular = Column('Celular', String(14), nullable=False, unique=True)
    ra = Column('RA', SmallInteger,  nullable=False)

    def __repr__(self):
        '''
        Método de representação do objeto
        '''
        return f"<Aluno: {self.nome}"


class Professor(Base):
    '''
    Classe Professor: mapeia a tabela Profesor do Banco de Dados
    possui um realacionamento com Usuario de nome usuario, e cria
    a backref perfil_professor.
    '''
    __tablename__ = 'Professor'
    id_professor = Column(
        'idAluno', SmallInteger, autoincrement=True,
        nullable=False, primary_key=True
    )
    id_usuario = Column(
        'idUsuario', SmallInteger, ForeignKey('Usuario.idUsuario'),
        nullable=False
    )
    email = Column('Email', String(50), nullable=False, unique=True)
    celular = Column('Celular', String(14), nullable=False, unique=True)
    apelido = Column('Apelido', String(15), nullable=False)

    def __repr__(self):
        '''
        Método de representação do objeto
        '''
        return f"<Aluno: {self.nome}"


class Coordenador(Base):
    '''
    Classe Coordenador: mapeia a tabela Profesor do Banco de Dados
    Possui um realacionamento com Usuario, de nome usuario, e cria
    a backref perfil_coordenador.
    Possui um relaciomento com Disciplina de nome disciplinas e cria
    a backref coordenador.
    '''
    __tablename__ = 'Coordenador'
    id_coordenador = Column(
        'idCoordenador', SmallInteger, nullable=False,
        autoincrement=True, primary_key=True
    )
    id_usuario = Column(
        'idUsuario', SmallInteger, ForeignKey('Usuario.idUsuario'),
        nullable=False
    )
    nome = Column('Nome', String(30), nullable=False)
    email = Column('Email', String(50), nullable=False, unique=True)
    celular = Column('Celular', String(14), nullable=False, unique=True)
    disciplina = relationship('Disciplina', backref='coordenador')

    def __repr__(self):
        '''
        Método de representação do objeto
        '''
        return f"<Coordenador: {self.nome}"


class Disciplina(Base):
    '''
    Classe Disciplina: mapeia a tabela Disciplina do Banco de Dados.
    Não é necessário colocar as restições das colunas: PercentualPrático,
    PercentualTeórico, CargaHoraria e StatusDisciplina
    '''
    __tablename__ = "Disciplina"
    id_disciplina = Column(
        'idDisciplina', SmallInteger, nullable=False,
        autoincrement=True, primary_key=True
    )
    nome = Column('Nome', String(50), nullable=False)
    data_disciplina = Column('DataDisciplina', Date)
    status_disciplina = Column('StatusDisciplina', String(8))
    plano_de_ensino = Column('PlanoDeEnsino', String(100))
    carga_horaria = Column('CargaHoraria', Integer, nullable=False)
    competencias = Column('Competencias', String(500))
    habilidades = Column('Habilidades', String(500))
    ementa = Column('Ementa', String(500))
    id_coordenador = Column(
        'idCoordenador', SmallInteger, ForeignKey('Coordenador.idCoordenador'),
        nullable=False
    )
    conteudo_programatico = Column('ConteudoProgramatico', String(500))
    bibliografia_basica = Column('BibliografiaBasica', String(500))
    bibliografia_complementar = Column('BibliografiaComplementar', String(500))
    percentual_pratico = Column('PercentualPratico', Integer, nullable=False)
    percentual_teorico = Column('PercentualTeorico', Integer, nullable=False)

    def __repr__(self):
        '''
        Método de representação do objeto
        '''
        return f"<Disciplina: {self.nome}>"


class Curso(Base):
    '''
    Classe Curso: mapeia a tabela Curso do Banco de Dados.
    '''
    __tablename__ = "Curso"
    id_curso = Column(
        'idCurso', SmallInteger, nullable=False, autoincrement=True,
        primary_key=True
    )
    nome = Column('nome', String(50), nullable=False)

    def __repr__(self):
        '''
        Método de representação do objeto
        '''
        return f"<Curso: {self.nome}>"
