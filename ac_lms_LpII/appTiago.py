from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


Base = declarative_base()


class User(Base):
    __tablename__ = "person"
    id = Column('IdPerson', Integer, primary_key=True)
    username = Column('username', String(50), unique=True)


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

engine = create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(bind=engine)