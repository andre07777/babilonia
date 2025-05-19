from peewee import *

db = SqliteDatabase('biblioteca.db')


class Autor(Model):
    nome = CharField()

    class Meta:
        database = db


class Categoria(Model):
    nome = CharField()

    class Meta:
        database = db


class Livro(Model):
    titulo = CharField()
    autor = ForeignKeyField(Autor, backref='livros')
    categoria = ForeignKeyField(Categoria, backref='livros')
    ano_publicacao = IntegerField()

    class Meta:
        database = db