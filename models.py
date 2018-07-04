from bookmanager import app, db, ma

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    book = db.relationship('Book', backref='Author', lazy=True, uselist=True)

class AuthorSchema(ma.Schema):
    class Meta:
        fields = ('id','name', 'book')

class Book(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)

    def __repr__(self):
        return "\"Title\": {}".format(self.title)

class BookSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'title', 'author_id')

book_schema = BookSchema()
books_schema = BookSchema(many=True)
author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)