# MongoDB
from pymongo import MongoClient

client = MongoClient("localhost:27017")
print("Connnection Successful !") if client else print("Connection Failed")