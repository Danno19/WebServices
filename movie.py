from flask_restful   import Resource, Api, reqparse

from records         import id_register, movie_counter, movies
from dema_service    import DeMaService

class Movie(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title',    type = str, required = True, location = 'json', help = "Title must be specified")
        self.reqparse.add_argument('eidr',     type = str, required = True, location = 'json', help = "EIDR must be specified")
        self.reqparse.add_argument('year',     type = str, required = True, location = 'json', help = "Year must be specified")
        self.reqparse.add_argument('director', type = str, required = True, location = 'json', help = "Director must be specified")
        self.reqparse.add_argument('books',    type = str, required = True, location = 'json', help = "At least one book must be specified")

    def get(self):
        repertoire = []
        for movie in movies.values():
            repertoire.append(movie)
        if len(repertoire) is 0:
            return 'Nothing to watch', 404
        else:
            return repertoire, 200

    def post(self):
        args = self.reqparse.parse_args()
        
        global movie_counter
        movie_counter += 1
        
        new_movie = {'id': movie_counter, 'title': args['title'], 'eidr': args['eidr'], 'year': args['year'], 'director': args['director'], 'books': args['books'] }
        
        if args['eidr'] in id_register:
            movie_counter -= 1
            return 'Every movie has its unique EIDR', 403
        else:
            library = args['books'].split(',')
            books   = DeMaService().get_all_books()

            if books == 'Book service is down':
                return 'Book service is down', 503

            duplicates = []
            for isbn in library:
                try:
                    books[int(isbn)].get('isbn')

                    for duplicate in duplicates:
                        if duplicate == int('isbn'):
                            movie_counter -= 1
                            return "Book duplicates found in json", 400

                    duplicates.append(int(isbn))

                except IndexError as exc:
                    movie_counter -= 1
                    return "At least one book isbn is invalid or the json format is unrecognized", 400

            movies[new_movie['id']] = new_movie
            id_register.append(new_movie['eidr'])
            return 'Movie "'+new_movie['title']+'" succesfully added with ID '+str(movie_counter), 201