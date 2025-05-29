from fastapi import FastAPI, Request
from queue import enqueue_message

app = FastAPI(title='SQS Simulator')

@app.post('/enqueue')
async def enqueue(request: Request):
    body = await request.json()
    enqueue_message(body)
    return {"status": "message enqueued", "body": body}