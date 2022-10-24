from flask import Flask, jsonify
from models import Book
from crud import Session

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# GET METHODS
@app.route("/", methods=['GET'])
def get_books():
    s = Session()
    books = s.query(Book).order_by(Book.id).all()
    return jsonify({'books:': list(el.json() for el in books)})


if __name__ == '__main__':
    app.run(debug=True)
