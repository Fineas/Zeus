from pymongo import MongoClient
from bson import ObjectId

client = MongoClient('localhost', 27017)

db = client.dictionary_database

collection = db.dictionary_database

#dictionary = \
#{
#    "how"  : ["well", "good", "bad"],
#    "when" : ["today", "tomorrow", "later"],
#    "why"  : ["bla bla", "just so"]
#}

message = raw_input()

print(db.posts)

d = con[db][col].find_one()

print(d)

db.dictionary_database.posts.remove({ "_id" : ObjectId("58c045c2a7643f7fd10e9e01")})
db.dictionary_database.posts.remove({ "_id" : ObjectId("58c0454ca7643f7fb0d8cabb")})
db.dictionary_database.posts.remove({ "_id" : ObjectId("58c0453aa7643f7fa63abd98")})


print(message)
#posts   = db.posts
#post_id = posts.insert_one(dictionary).inserted_id
#print post_id