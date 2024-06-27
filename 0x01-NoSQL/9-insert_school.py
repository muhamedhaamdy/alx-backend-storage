#!/usr/bin/env python3
import pymongo
'''pymongo app'''


def insert_school(mongo_collection, **kwargs):
    '''insert into a collection'''
    mongo_collection.insert_one(kwargs)
