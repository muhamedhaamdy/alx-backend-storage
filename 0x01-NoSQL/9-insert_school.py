#!/usr/bin/env python3
"""Insert a document"""


def insert_school(mongo_collection, **kwargs):
    """
    mongo_collection: collection object
    **kwargs: dictionary

    Return: the id of the inserted document 
    """
    return mongo_collection.insert_one(kwargs).inserted_id
