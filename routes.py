from bookmanager import app, db, ma

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import jsonify
import json

@app.route('/books', methods=["GET", "POST"])
def home():
    books = None
    if request.form:
        try:
            book = Book(title=request.form.get("title"))
            print(book)
            if (book != None):
                db.session.add(book)
                db.session.commit()
        except Exception as e:
            print("Failed to add book")
            print(e)
    books = Book.query.all()
    return render_template("home.html", books=books)

@app.route("/books/update", methods=["POST"])
def update():
    try:
        newtitle = request.form.get("newtitle")
        _id = request.form.get("id")
        book = Book.query.filter_by(id=_id).first()
        book.title = newtitle
        db.session.commit()
    except Exception as e:
        print("Couldn't update book title")
        print(e)
    return redirect("/")

@app.route("/books/delete", methods=["POST"])
def delete():
    _id = request.form.get("id")
    book = Book.query.filter_by(id=_id).first()
    if (book != None):
        db.session.delete(book)
        db.session.commit()
    return redirect("/")

@app.route("/books/getall", methods=["GET"])
def getall():
    ret = Book.query.all()
    result = books_schema.dump(ret)
    return jsonify(result.data)

@app.route("/books/get/<id>", methods=["GET"])
def books_detail(id):
    books = Book.query.get(id)
    return book_schema.jsonify(books)

