from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client.new_db
collection = db.new_collection
collection1=db.new_collection1

collection.insert_many([
    {
        "name": "venkatesu",
        "class": "cse"
    },
    {
        "name": "sri",
        "class": "cse-c"
    },
    {
        "name": "sri",
        "class": "cse-c"
    }
])
collection1.insert_many([
    {
        "name": "venkatesu",
        "class": "cse"
    },
    {
        "name": "sri",
        "class": "cse-c"
    },
    {
        "name": "sri",
        "class": "cse-c"
    }
])
