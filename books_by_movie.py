from flask_restful   import Resource, Api, reqparse

from records         import movie_counter, movies
from dema_service    import DeMaService

class BooksByMovie(Resource):
    def get(self, id):
        if id not in movies:
            return 'There is no movie with the given ID', 404

        related_books = []
        bookshelf     = movies[id].get('books').split(',')

        for book in bookshelf:
            serviceResponse = DeMaService().get_book(book)
            if serviceResponse is not 'Book service is down':
                related_books.append(serviceResponse)
            else:
                return 'Book service is down', 503
        
        new_movie = {
            'id':            id, 
            'title':         movies[id].get('title'), 
            'eidr':          movies[id].get('eidr'), 
            'year':          movies[id].get('year'), 
            'director':      movies[id].get('director'), 
            'related books': related_books 
            }
        
        return new_movie, 200