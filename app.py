from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# In-memory database of books
books = [
    {'id': 1, 'title': '1984', 'author': 'George Orwell'},
    {'id': 2, 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald'},
    {'id': 3, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'}
]

# Route for the root URL
@app.route('/')
def index():
    return 'Welcome to the Book API'

# Route to get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({'books': books})

# Route to get a single book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book is not None:
        return jsonify(book)
    else:
        return jsonify({'message': 'book not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)