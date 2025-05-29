import redis
import json


import redis
import json

r = redis.Redis(host="redis", port=6379, db=0)
QUEUE_NAME = "sqs_sim_queue"

def enqueue_message(data): # message enqueue
    r.rpush(QUEUE_NAME, json.dumps(data))

def dequeue_message(): # message dequeue 
    item = r.lpop(QUEUE_NAME)
    if item:
        return json.loads(item)
    return None