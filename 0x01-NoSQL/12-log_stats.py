#!/usr/bin/env python3
from pymongo import MongoClient
'''all logs'''


if __name__ == '__main__':
    client = MongoClient('mongodb://localhost:27017')
    logs_collection = client.logs.nginx
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print('{} logs'.format(logs_collection.count_documents({})))
    print('Methods:')
    for method in methods:
        n = logs_collection.count_documents({'method': method})
        print('method {}: {}'.format(method, n))
    status_count = logs_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print('{} status check'.format(status_count))