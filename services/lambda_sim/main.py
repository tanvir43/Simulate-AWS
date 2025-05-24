from fastapi import FastAPI, Request
from tasks import simulate_lambda_task

app = FastAPI(title="Lambda Simulator")

@app.post("/trigger")
async def trigger_lambda(request: Request):
    body = await request.json()
    simulate_lambda_task.delay(body)
    return {"status": "task sent", "payload": body.get("payload")}
