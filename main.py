
from pymongo import MongoClient

client = MongoClient("mongodb+srv://slooviTestdb:DZzJvtn6RzUuiOiI@sloovitest.dhkofzo.mongodb.net/?retryWrites=true&w=majority")

db = client['SLOOVITEST']

collection = db["jbichene@gmail.com"]


collection.insert_one(
    {"user_info":{
        "password":"A1234b","first_name":"john","last_name":"bichene","Email":"jbichene@gmail.com","Templates":{
            "Template_id":{
                "template_name": "ggg" ,
                "subject": "mmm",
                "body": "hhh"
            }
            }
            }
             
            }
    
) 
# doc_count = collection.count_documents({})
# # db.collection.find()_one("jbichene@gmail.com")
# print(db["jbichene@gmail.com"].user_info())#.collection.find())#_one("jbichene@gmail.com"))
# collections = collection.list_collection_names()
# for collection in collections:
#    print(collection)