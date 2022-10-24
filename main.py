from flask import Flask, jsonify, abort, make_response, request
from sqlalchemy import create_engine, and_, or_
from sqlalchemy.orm import sessionmaker, session
from config import DATABASE_URI
from models import Base, Book
from crud import contextmanager, session_scope, engine, Session


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# GET METHODS
@app.route("/", methods=['GET'])
def get_books():
    s = Session()
    # return jsonify([f'{i}' for i in s.query(Book).order_by(Book.id).all()])
    return jsonify((f'Books: {s.query(Book).all()}'))

if __name__ == '__main__':
    app.run(debug=True)
