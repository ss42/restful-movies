import webapp2

import json

from google.appengine.ext import ndb


class Book(ndb.Model):
    """A main model for representing an individual Book."""
    publication_year = ndb.IntegerProperty(indexed=False)
    author = ndb.StringProperty(indexed=True)
    title = ndb.StringProperty(indexed=True)
# # [END Book]


class HomeHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')


class BookListHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('We should display a list.')


class BookByISBNHandler(webapp2.RequestHandler):
    def get(self, isbn):
        book = Book.get_by_id(isbn)
        book_dict = book.to_dict()
        book_dict["isbn_number"] = isbn
        response_body = json.dumps(book_dict)
        self.response.write(response_body)

    def put(self, isbn):
        book = Book.get_by_id(isbn)
        json_string = self.request.body
        json_dict = json.loads(json_string)
        for key, value in json_dict.iteritems():
            setattr(book, key, value)
            print("Setting key " + key + " to value " + value)
        book.put()
        book_dict = book.to_dict()
        book_dict["isbn_number"] = isbn
        response_body = json.dumps(book_dict)
        self.response.write(response_body)

    def post(self, isbn):

        json_string = self.request.body
        json_object = json.loads(json_string)

        publication_year = json_object["publication_year"]
        author = json_object["author"]
        title = json_object["title"]

        new_book = Book(id=isbn,
                        title=title,
                        author=author,
                        publication_year=publication_year)

        new_book.put()
        json_response_dict = new_book.to_dict()
        json_response_dict["isbn"] = isbn
        json_response_string = json.dumps(json_response_dict)
        self.response.headers["Content-Type"] = "application/json"
        self.response.write(json_response_string)

    def delete(self, isbn):
        book_key = ndb.Key('Book', isbn)
        book_key.delete()
        self.response.write('Deleted book with isbn ' + isbn)


app = webapp2.WSGIApplication([
    webapp2.Route(r'/', handler=HomeHandler, name='home'),
    webapp2.Route(r'/books', handler=BookListHandler, name='book-list'),
    webapp2.Route(r'/book/<isbn>', handler=BookByISBNHandler, name='book-by-isbn'),
])

# this is the json object in the request body for our new book
# {
# "title": "Our Awesome Book",
# "author": "Kim, Jung",
# "publication_year": 2015
# }
