from sqlalchemy import create_engine, Column
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from getpass import getpass

Base = declarative_base()
eng = create_engine('sqlite:///:memory:', echo=True)

'''eng = create_engine(f"mssql+pymssql://salas\\tiago.souza:{getpass()}@sql.salas.aulas/fit_alunos")'''

class Author(Base):
    __tablename__ = 'Authors'
    author_id = Column('AuthorId', Integer, autoincrement=True, primary_key=True)
    name = Column('Name', String(30))
    books = relationship("Books", backref='author')

    def __repr__(self):
        return f"<Author: {self.Name}>"


class Books(Base):
    __tablename__ = 'Books'
    book_id = Column('BookId', Integer, primary_key=True, autoincrement=True)
    title = Column('Title', String(30))
    author_id = Column('AuthorId', Integer, ForeignKey('Authors.AuthorId'), nullable=False )

    def __repr__(self):
        return f"<Book: {self.Title}>"

Base.metadata.create_all(bind=eng)

'''
if __name__ == '__main__':
    Session = sessionmaker(eng)
    ses = Session()
    book = ses.query(Books).get(1)

    print(book.author)
'''