from celery import Celery
import time

# Connect to Redis running in Docker
app = Celery("tasks", broker="redis://redis:6379/0")

@app.task
def simulate_lambda_task(payload):
    print("[Lambda Simulation] Start task with payload:", payload)
    time.sleep(2)  # Simulate processing delay
    print("[Lambda Simulation] Task complete for payload:", payload)
