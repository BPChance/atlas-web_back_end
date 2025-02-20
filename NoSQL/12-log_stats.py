#!/usr/bin/env python3
""" Python script that provides stats about Nginx logs stored in MongoDB """


from pymongo import MongoClient


def log_stats():
    """ provides some stats about Nginx logs stored in MongoDB """
    client = MongoClient('mongodb://127.0.0.1:27017')
    # access logs db and nginx collection
    db = client.logs
    collection = db.nginx

    total = collection.count_documents({})
    print(f"{total} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    # loop through each method and count occurences in the logs
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    # count GET requests specifically to "/status" path
    status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status_check")

if __name__ == "__main__":
    log_stats()
