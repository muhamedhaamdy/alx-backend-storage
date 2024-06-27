#!/usr/bin/env python3
import pymongo
'''pymongo app'''


def insert_school(mongo_collection, **kwargs):
    """
    mongo_collection: pymongo collection object
    **kwargs: key-value pairs to be inserted in the document

    Return: new _id
    """
    mongo_collection.insert_one(kwargs)
