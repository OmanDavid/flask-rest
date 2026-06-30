from flask import Blueprint,jsonify,request
from flask_restful import Api,Resource


library_bp = Blueprint('library_bp',__name__)
library_api = Api(library_bp)


class Book:
    def __init__(self,id,title,year,author):
        self.id = id
        self.title = title
        self.year = year
        self.author = author
        pass

    def to_dict(self):
        return{'id':self.id,'title':self.title,'author':self.author.__dict__}

class Author:
    def __init__(self,id,name):
        self.name = name
        self.id = id
        pass

authors = [
    Author(1,'Ken Walibora'),Author(2,'James Clear')
]

books = [
    Book(1,"Test Book",2020,authors[0]),
    Book(2,"Test Book2",2021,authors[1]),
    Book(3,"Testi Buku",2022,authors[0])
]
@library_bp.route('/')
def home():
    return jsonify({'message':'Loaded succesfully'})

    pass
@library_bp.route('/get_books')
def get_books():
    booklist = [book.to_dict() for book in books]
    return jsonify(booklist)

@library_bp.route('/get_book/<int:id>')
def get_book(id):
    for book in books:
        if book.id == id:
            
            return (jsonify(book.to_dict()))
    else:
        return ( jsonify({'error':'Book Not Found'}), 404)

@library_bp.route('/create_book',methods=['POST'])
def create_book():
    book_info = request.json
    new_book = Book(title=book_info.get('title'),year = book_info.get('year'),id = len(books)+1, author=authors[0])
    books.append(new_book)
    return jsonify(new_book.to_dict()),201

@library_bp.route('/search_books')
def search_books():
    query = request.args.get('q', '').lower()
    results = [b.to_dict() for b in books if query in b.title.lower()]
    return jsonify(results)


class AuthorResource(Resource):
    def get(self):
        author_list = [author.__dict__ for author in authors]
        return author_list
    
    def post(self):
        author_data = request.json
        new_author = Author(id=len(authors)+1, name=author_data['name'])
        authors.append(new_author)
        return new_author.__dict__, 201

    pass

library_api.add_resource(AuthorResource,'/authors')
