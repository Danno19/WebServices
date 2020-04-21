import requests

class DeMaService:
    def __init__(self):
        self.url = 'http://localhost:80/'
    
    def get_all_books(self):
        books = []
        try:
            request   = requests.get(self.url + 'books')
            requests.RequestException()
            jsonBooks = request.json()
            library   = jsonBooks
            
            for book in library:
                books.append(book)
            return books
            
        except requests.exceptions.RequestException as exc:
            return 'Book service is down', 503

    def get_book(self, _iban):
        try:
            request   = requests.get(self.url + 'books/' + str(_iban))
            requests.RequestException()
            jsonBooks = request.json()
            book      = jsonBooks

            return book
            
        except requests.exceptions.RequestException as exc:
            return 'Book service is down', 503
