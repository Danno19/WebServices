from flask_restful   import Resource, Api, reqparse

from records         import movie_counter, movies
from dema_service    import DeMaService

class BooksOfMovies(Resource):
    def get(self):
        repertoire    = []
        related_books = []
        bookshelf     = []

        for id in range(0, movie_counter):
            related_books = []
            bookshelf     = movies[id].get('books').split(',')

            for book in bookshelf:
                serviceResponse = DeMaService().get_book(book)

                if serviceResponse != "Book service is down":
                    related_books.append(serviceResponse)
                else:
                    return "Book service is down", 503
        
            new_movie = {
                'id':            id, 
                'title':         movies[id].get('title'), 
                'eidr':          movies[id].get('eidr'), 
                'year':          movies[id].get('year'), 
                'director':      movies[id].get('director'), 
                'related books': related_books 
                }
        
            repertoire.append(new_movie)

        return repertoire, 200