from django.db import models

# Create your models here.

from pymongo import MongoClient

mongo_client = None
redis_client = None


def makeMongoConnection():
    mongo_client = MongoClient('mongodb+srv://ankur:ankur321@cluster0.0trdv.mongodb.net/studentDB?retryWrites=true&w=majority')

    # Access the database
    db = mongo_client['studentDB']
    # Check if the database exists
    print(mongo_client.list_database_names())  # This will list all databases
    return db

def makeMongoCollection(db, collection):
    return db.create_collection(name=collection)

# Create a connection to Redis
import redis

def makeRedisConnection():
    redis_client = redis.Redis(
        host='redis-17832.c305.ap-south-1-1.ec2.redns.redis-cloud.com',
        port=17832,
        password='UvlAIeLkP28TzdLUGaRkA1MdLJXsYu1M')
    # redis_client = redis.Redis(
    #     host='rediss://red-csbv24jv2p9s73dlvhug:qr9yK3V582nV4ytfwjSCFxbkwFu5Hz1E@oregon-redis.render.com:6379')

    # # Set a value
    # redis_client.set('my_key', 'my_value')
    #
    # # Get a value
    # value = redis_client.get('my_key')
    # print(value)  # Output: my_value
    return redis_client


