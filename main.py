from fastapi import FastAPI, HTTPException
from models import UserSignup, UserLogin
from redis_client import redis_client

app = FastAPI()

@app.post("/signup")
def signup(user: UserSignup):
    if redis_client.exists(f"user:{user.username}"):
        raise HTTPException(status_code=400, detail="User already exists")
    
    redis_client.set(f"user:{user.username}", user.password)
    return {"message": "Signup successful", "user": user.username}

@app.post("/login")
def login(user: UserLogin):
    stored_password = redis_client.get(f"user:{user.username}")
    
    if stored_password is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    if stored_password != user.password:
        raise HTTPException(status_code=401, detail="Incorrect password")
    
    redis_client.set(f"session:{user.username}", "logged_in", ex=3600)
    return {"message": "Login successful", "user": user.username}

@app.get("/status/{username}")
def status(username: str):
    session_status = redis_client.get(f"session:{username}")
    
    if session_status:
        return {"user": username, "status": session_status}
    
    raise HTTPException(status_code=404, detail="User not logged in")
