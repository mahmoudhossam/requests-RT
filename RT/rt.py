#!/usr/bin/python

__author__ = 'Mahmoud Hossam'
__version__ = '0.1'

import requests

def _get_response(url, params=None):
    req = requests.get(url, params=params)
    return req.json()

def _get_movies(url, params=None):
    response = _get_response(url, params)
    movies = response['movies']
    if len(movies) > 1:
        return [Movie(m) for m in movies]
    else:
        return Movie(movies[0])

def _get_reviews(url, params=None):
    response = _get_response(url, params)
    reviews = response['reviews']
    if len(reviews) > 1:
        return [Review(r) for r in reviews]
    else:
        return Review(reviews[0])

def _get_cast(url, params=None):
    response = _get_response(url, params)
    cast = response['cast']
    return [Actor(a) for a in cast]

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
        return _get_movies(url, params)
                           
    def box_office(self, limit=10, country='us'):
        url = 'http://api.rottentomatoes.com/api/public/v1.0/lists/movies/box_office.json'
        params = {
                'limit': limit,
                'country': country,
                'apikey': self.apikey}
        return _get_movies(url, params)

    def in_theatres(self, page_limit=16, page=1, country='us'):
        url = 'http://api.rottentomatoes.com/api/public/v1.0/lists/movies/in_theaters.json'
        params = {
                'page_limit': page_limit,
                'country': country,
                'page': page,
                'apikey': self.apikey}
        return _get_movies(url, params)

    def opening(self, limit=16, country='us'):
        url = 'http://api.rottentomatoes.com/api/public/v1.0/lists/movies/opening.json'
        params = {
                'limit': limit,
                'country': country,
                'apikey': self.apikey}
        return _get_movies(url, params)

    def upcoming(self, page_limit=16, page=1, country='us'):
        url = 'http://api.rottentomatoes.com/api/public/v1.0/lists/movies/upcoming.json'
        params = {
                'page_limit': page_limit,
                'country': country,
                'page': page,
                'apikey': self.apikey}
        return _get_movies(url, params)

    def review(self, movie_id, review_type='top_critic', page_limit=20, page=1, country='us'):
        url = 'http://api.rottentomatoes.com/api/public/v1.0/movies/%s/reviews.json' % movie_id
        params = {
                'country': country,
                'page': page,
                'page_limit': page_limit,
                'review_type': review_type,
                'apikey': self.apikey}
        return _get_reviews(url, params)

    def cast(self, movie_id):
        url = 'http://api.rottentomatoes.com/api/public/v1.0/movies/%s/cast.json' % movie_id
        params = {'apikey': self.apikey}
        return _get_cast(url, params)


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

class Review:

    def __init__(self, review_info):
        self.critic = review_info.get('critic')
        self.date = review_info.get('date')
        self.quote = review_info.get('quote')
        self.publication = review_info.get('publication')
        self.freshness = review_info.get('freshness')
        self.original_score = review_info.get('original_score')
        self.link = review_info.get('links').get('review')

class Actor:

    def __init__(self, actor_info):
        self.actor_id = actor_info.get('id')
        self.name = actor_info.get('name')
        self.characters = actor_info.get('characters')

