from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import redis

app = FastAPI()

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

class User(BaseModel):
    id: str
    name: str
    age: int

@app.post("/user/")
def create_user(user: User):
    key = f"user:{user.id}"

    # Store in Redis as a hash
    r.hset(key, mapping={
        "name": user.name,
        "age": user.age
    })

    return {"message": "User saved as hash successfully", "key": key}

@app.get("/user/{user_id}")
def get_user(user_id: str):
    key = f"user:{user_id}"

    # Get all fields from the hash
    user_data = r.hgetall(key)

    if not user_data:
        raise HTTPException(status_code=404, detail="User not found")

    # Include the user ID back in the response
    user_data["id"] = user_id
    user_data["age"] = int(user_data["age"])  # Convert age from string to int

    return user_data
