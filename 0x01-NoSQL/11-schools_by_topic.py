#!/usr/bin/env python3
""" filtter by topic """


def schools_by_topic(mongo_collection, topic):
    '''
        mongo_collection: collection object
        topics: string

        Return: array
    '''
    schools = mongo_collection.find()
    return [school for school in schools if topic in school['topics']]
