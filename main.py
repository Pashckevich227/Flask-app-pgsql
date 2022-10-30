from flask import Flask, jsonify, abort, make_response, request
from models import Book
from crud import Session

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# GET ALL METHODS
@app.route("/", methods=['GET'])
def get_books():
    s = Session()
    books = s.query(Book).order_by(Book.id).all()
    return jsonify({'books:': list(el.json() for el in books)})


# GET ONE POSITION
@app.route("/<int:book_id>", methods=['GET'])
def get_book(book_id):
    s = Session()
    book = list(el.json() for el in s.query(Book).all())
    book = list(filter(lambda x: x['id'] == book_id, book))
    if len(book) == 0:
        abort(404)
    return jsonify({'books:': book[0]})


# ERROR METHODS
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)  # 404 - Not found


# POST METHODS
@app.route('/', methods=['POST'])
def add_book():
    s = Session()
    books = list(el.json() for el in s.query(Book).all())

    if not request.json or not 'title' in request.json:
        abort(404)
    book = Book(id=books[-1]['id'] + 1,
                title=request.json['title'],
                author=request.json['author'],
                pages=request.json['pages'],
                published=request.json['published'],
                price=request.json['price'])
    s.add(book)
    s.commit()
    return {'book': book.json()}, 201  # 201 - CREATED


# PUT METHODS
# @app.route('/<int:book_id>', methods=['PUT'])
# def update_task(book_id):
#     s = Session()
#     book = list(el.json() for el in s.query(Book).all())
#     book = list(filter(lambda x: x['id'] == book_id, book))
#
#     if not request.json and len(book) == 0:
#         abort(400)
#
#     book[0]['title'] = request.json.get('title', book[0]['title'])
#     book[0]['price'] = request.json.get('price', book[0]['price'])
#     book[0]['kill_reward'] = request.json.get('kill_reward', book[0]['kill_reward'])
#     return jsonify({'task': book[0]})


@app.route('/<int:book_id>', methods=['DELETE'])
def delete_task(book_id):
    s = Session()
    data = s.query(Book).all()
    book = s.query(Book).filter(Book.id == book_id).first()
    if book not in data:
        abort(404)
    s.delete(book)
    s.commit()
    return ({'result': True})


if __name__ == '__main__':
    app.run(debug=True)
