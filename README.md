# aws-sim-lab

A **FastAPI-based simulation lab** that mimics core AWS services for backend engineers and DevOps learners. This project helps developers understand and experiment with service interactions, scalability, async workflows, and load testing — all while staying within free-tier or local environments.

## 🚀 Why This Project?

Backend systems often rely on AWS services like S3, Lambda, RDS, and SQS — but understanding how they behave in real-world use cases takes practice. This lab simulates that experience with local tools, giving developers hands-on exposure to scalable architecture patterns.

## 🧩 Simulated Services
| Simulated Service | FastAPI Role | AWS Equivalent | Description |
|--------------------|---------------|-----------------|-------------|
| `s3_sim`           | File uploads, versioning | Amazon S3 | Upload and version files with metadata tracking |
| `lambda_sim`       | Async task worker | AWS Lambda | Trigger simulated "Lambda" jobs via Redis queue |
| `sqs_sim`          | Message queue | Amazon SQS | Simulated task queuing using Redis |
| `rds_sim`          | SQL read/write | Amazon RDS | Simulates structured data I/O with PostgreSQL or SQLite |
| `metrics_api`      | Monitoring | CloudWatch + Prometheus | Exposes system metrics for observability |

## 🛠️ Tech Stack
- **FastAPI** for service simulation
- **Redis** for queuing and event simulation
- **Celery** for background task execution
- **Docker + docker-compose** for local orchestration
- **Prometheus + Grafana** for observability
- **Locust** for high-volume simulation and load testing

## 📦 Project Structure
```
aws-sim-lab/
├── services/
│   ├── s3_sim/
│   ├── lambda_sim/
│   ├── sqs_sim/
│   ├── rds_sim/
│   └── metrics_api/
├── locust/
│   └── scenarios/
├── docker-compose.yml
├── prometheus/
├── grafana/
└── README.md
```

## 🎓 What You'll Learn
- How to simulate AWS patterns locally using FastAPI
- How to build async architectures with queues and background workers
- How to monitor system performance using Prometheus and Grafana
- How to write load tests and simulate traffic with Locust
- How to connect backend logic across multiple microservices
- **How to simulate realistic load**, like **1,000 requests in 10 minutes**, using Locust and monitor the system’s behavior under pressure

