#!/usr/bin/env python3
'''update a document'''


def update_topics(mongo_collection, name, topics):
    '''
        mongo_collection: collection object
        name: the name of the school
        topics: array of topics

        Return: the id of the inserted document 
    '''
    mongo_collection.update_many({'name': name}, 
                                { "$set": {'topics' : topics}})
    

    