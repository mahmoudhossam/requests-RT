#!/usr/bin/python

__author__ = 'Mahmoud Hossam'
__version__ = '0.1'

import requests
try:
    import simplejson as json
except ImportError:
    import json

def get_response(url, params=None):
        req = requests.get(url, params=params)
        return req.text

class RT:
    def __init__(self, apikey):
        self.apikey = apikey
    
    def search(self, query, page_limit=30, page=1):
        url = 'http://api.rottentomatoes.com/api/public/v1.0/movies.json'
        params = {
                'q': query,
                'page_limit': page_limit,
                'page': page,
                'apikey': self.apikey}
        response = get_response(url, params)
        if response:
            movies = json.loads(response)['movies']
            if len(movies) > 1:
                return [Movie(m) for m in movies]
            else:
                return Movie(movies[0])

    def box_office(self, limit=10, country='us'):
        url = 'http://api.rottentomatoes.com/api/public/v1.0/lists/movies/box_office.json'
        params = {
                'limit': limit,
                'country': country,
                'apikey': self.apikey}
        return get_response(url, params=params)

    def in_theatres(self, page_limit=16, page=1, country='us'):
        url = 'http://api.rottentomatoes.com/api/public/v1.0/lists/movies/in_theaters.json'
        params = {
                'page_limit': page_limit,
                'country': country,
                'page': page,
                'apikey': self.apikey}
        return get_response(url, params=params)

    def opening(self, limit=16, country='us'):
        url = 'http://api.rottentomatoes.com/api/public/v1.0/lists/movies/opening.json'
        params = {
                'limit': limit,
                'country': country,
                'apikey': self.apikey}
        return get_response(url, params=params)

    def upcoming(self, page_limit=16, page=1, country='us'):
        url = 'http://api.rottentomatoes.com/api/public/v1.0/lists/movies/upcoming.json'
        params = {
                'page_limit': page_limit,
                'country': country,
                'page': page,
                'apikey': self.apikey}
        return get_response(url, params=params)


class Movie:
    def __init__(self, movie_info):
        self.movie_id = movie_info.get('id')
        self.cast = movie_info.get('abridged_cast')
        self.posters = movie_info.get('posters')
        self.rating = movie_info.get('ratings')
        self.duration = movie_info.get('runtime')
        self.name = movie_info.get('title')
        self.year = movie_info.get('year')
        self.synopsis = movie_info.get('synopsis')
        self.ratings = movie_info.get('ratings')
        self.critics_score = self.ratings.get('critics_score')
        self.critics_rating = self.ratings.get('critics_rating')
        self.audience_score = self.ratings.get('audience_score')
        self.audience_rating = self.ratings.get('audience_rating')
        self.genres = movie_info.get('genres')
        self.studio = movie_info.get('studio')
        self.links = movie_info.get('links')

