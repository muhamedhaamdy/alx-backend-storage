#!/usr/bin/env python3
import pymongo
''''''


def insert_school(mongo_collection, **kwargs):
    mongo_collection.insert_one(kwargs)
