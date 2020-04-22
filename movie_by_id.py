from flask_restful   import Resource, Api, reqparse

from records         import id_register, movie_counter, movies
from dema_service    import DeMaService

class MovieById(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title',    type = str, required = True, location = 'json', help = "Title must be specified")
        self.reqparse.add_argument('eidr',     type = str, required = True, location = 'json', help = "EIDR must be specified")
        self.reqparse.add_argument('year',     type = str, required = True, location = 'json', help = "Year must be specified")
        self.reqparse.add_argument('director', type = str, required = True, location = 'json', help = "Director must be specified")
        self.reqparse.add_argument('books',    type = str, required = True, location = 'json', help = "At least one book must be specified")

    def get(self, id):
        if id not in movies:
            return 'There is no movie with the given ID', 404
        else:
            return movies[id], 200

    def post(self, id):
        return "Posting is not allowed on this page", 400

    def put(self, id):
        if id not in movies:
            return 'There is no movie with the given ID', 404
        else:
            args = self.reqparse.parse_args()
            temp_eidr = movies[id].get('eidr')
            if temp_eidr in id_register:
                id_register.remove(temp_eidr)
            
            changed_movie = {
                'id': id, 
                'title': args['title'], 
                'eidr': args['eidr'], 
                'year': args['year'], 
                'director': args['director'],
                'books': args['books']
            }
            
            if args['eidr'] in id_register:
                return 'Every movie has its unique EIDR', 403
            elif args['books'] == '':
                return 'Every movie has at least one book', 403
            else:
                library = args['books'].split(',')
                books   = DeMaService().get_all_books()

                if books == 'Book service is down':
                    return 'Book service is down', 503

                duplicates = []
                for isbn in library:
                    try:
                        books[int(isbn)-9786090138823].get('isbn')

                        for duplicate in duplicates:
                            if duplicate == (int('isbn')-9786090138823):
                                return "Book duplicates found in json", 400

                        duplicates.append(int(isbn)-9786090138823)

                    except IndexError as exc:
                        id_register.append(id_register)
                        return "At least one book isbn is invalid or the json format is unrecognized", 400

                movies[id] = changed_movie
                id_register.append(changed_movie['eidr'])
                return 'Movie "'+changed_movie['title']+'" succesfully changed with ID '+str(id), 200
    
    def delete(self, id):
        if id not in movies:
            return 'There is no movie with the given ID', 404
        else:
            movies.pop(id)
            return 'Movie with ID '+str(id)+' succesfully deleted', 200
