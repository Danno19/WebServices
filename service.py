from flask           import Flask
from flask_restful   import Resource, Api, reqparse

from movie           import Movie
from movie_by_id     import MovieById
from books_by_movie  import BooksByMovie
from books_of_movies import BooksOfMovies

app = Flask(__name__)
api = Api(app)

api.add_resource(Movie,         '/movies')
api.add_resource(MovieById,     '/movies/<int:id>')
api.add_resource(BooksByMovie,  '/movies/<int:id>/books')
api.add_resource(BooksOfMovies, '/movies/books')

if __name__ == '__main__':
    app.run(host = "0.0.0.0", debug = True)