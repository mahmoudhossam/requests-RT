#!/usr/bin/python

__author__ = 'Mahmoud Hossam'
__version__ = '0.1'

import requests

def make_request(url, params=None):
        req = requests.get(url, params=params)
        return req.content

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
        return make_request(url, params)

    def box_office(self, limit=10, country='us'):
        url = 'http://api.rottentomatoes.com/api/public/v1.0/lists/movies/box_office.json'
        params = {
                'limit': limit,
                'country': country,
                'apikey': self.apikey}
        return make_request(url, params=params)

    def in_theatres(self, page_limit=16, page=1, country='us'):
        url = 'http://api.rottentomatoes.com/api/public/v1.0/lists/movies/in_theaters.json'
        params = {
                'page_limit': page_limit,
                'country': country,
                'page': page,
                'apikey': self.apikey}
        return make_request(url, params=params)

    def opening(self, limit=16, country='us'):
        url = 'http://api.rottentomatoes.com/api/public/v1.0/lists/movies/opening.json'
        params = {
                'limit': limit,
                'country': country,
                'apikey': self.apikey}
        return make_request(url, params=params)

    def upcoming(self, page_limit=16, page=1, country='us'):
        url = 'http://api.rottentomatoes.com/api/public/v1.0/lists/movies/upcoming.json'
        params = {
                'page_limit': page_limit,
                'country': country,
                'page': page,
                'apikey': self.apikey}
        return make_request(url, params=params)
