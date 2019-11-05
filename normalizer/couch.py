import couchdb
from couchdb import ResourceNotFound

from config import COUCHDB


class CouchDB:
    database_name = "cinema-scrapper"

    def __init__(self):
        self.couch = couchdb.Server(f'{COUCHDB["HOST"]}:{COUCHDB["PORT"]}')
        try:
            self.log_db = self.couch['cinema-scrapper-logs']
        except ResourceNotFound:
            self.log_db = self.couch.create('cinema-scrapper-logs')

    def new_session(self, session: dict):
        self.log_db.save(session)

    # def new_movie(self, movie: dict):
    #     doc = {
    #         "raw_movie_data": movie,
    #         "is_processed": False,
    #         "normalized_movie_title": None
    #     }
    #
    #     self.movie_db.save(doc)
