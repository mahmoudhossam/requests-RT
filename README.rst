###########
requests-RT
###########

A python interface for the Rotten Tomatoes API.

Uses requests under the hood.

Usage
---------
::  

    from rt import RT

    #set your api key here
    api = RT('API_KEY')

    #do your thing
    result = api.search('inception')

    #if this works, this should print 'inception'
    print(result.name)

License
----------

BSD