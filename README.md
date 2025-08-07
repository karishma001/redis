# redis
1. FastAPI + Redis (Login & Signup API)
Features:
User signup stores data in Redis.
Login checks credentials from Redis.

Validation: Incorrect login throws an error.
Uses pydantic for data validation and uvicorn as ASGI server.

Key Files:
main.py: FastAPI app with endpoints for /signup and /login.
redis_client.py: Redis connection logic.
models.py: User data schema using Pydantic.

work flow:
redis-login-demo/
│
├── main.py              # FastAPI app
├── models.py            # Pydantic models
├── redis_client.py      # Redis client connection
├── requirements.txt

How to Run:
uvicorn main:app --reload

2. CLI-based Redis CRUD App
---------------------------------------------------------------------------------------------------------------------------
Features:
Interactive CLI tool to create, read, update, and delete records in Redis.
Menu-driven approach using terminal.

Key File:
cli_crud.py: Command-line interface that performs CRUD on Redis.

How to Run:
python cli_crud.py

<img width="1470" height="956" alt="Screenshot 2025-08-07 at 5 49 43 PM" src="https://github.com/user-attachments/assets/c488eecb-b4f5-4db2-94cc-7c477d5a0718" />
<img width="2940" height="1912" alt="image" src="https://github.com/user-attachments/assets/611d30f7-25fb-4926-ac8f-4e41635f11a1" />
<img width="2940" height="1912" alt="image" src="https://github.com/user-attachments/assets/1c72737c-9d36-41e6-a99a-ee907d13d715" />

