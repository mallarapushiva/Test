from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
books = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"}
]

# GET all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# POST a new book
@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify({"message": "Book added!"}), 201

if __name__ == '__main__':
    app.run(debug=True)