#!/usr/bin/env python3
'''pymongo app'''


def list_all(mongo_collection):
    '''list all documents in this collection'''
    return mongo_collection.find()
