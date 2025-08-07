import redis

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

def create_user(user_id, name, destination, age):
    r.hset(user_id, mapping={"name": name, "destination": destination, "age": age})
    print(f" Created user '{user_id}' with data.")

def read_user(user_id):
    data = r.hgetall(user_id)
    if data:
        print(f"📖 Read user '{user_id}':")
        for field, value in data.items():
            print(f"  {field}: {value}")
    else:
        print("User not found")

def update_user(user_id, field, new_value):
    if r.exists(user_id):
        r.hset(user_id, field, new_value)
        print(f"Updated {field} for user '{user_id}' to '{new_value}'")
    else:
        print("User not found for update")

def delete_user(user_id):
    if r.exists(user_id):
        r.delete(user_id)
        print(f"🗑️ Deleted user '{user_id}'")
    else:
        print("User not found for deletion")

# --- Interactive CRUD ---
while True:
    print("\nOptions: create | read | update | delete | exit")
    action = input("Enter operation: ").lower()

    if action == 'exit':
        break
    elif action in ['create', 'read', 'update', 'delete']:
        user_id = input("Enter user ID: ")

        if action == 'create':
            name = input("Enter name: ")
            destination = input("Enter destination: ")
            age = input("Enter age: ")
            create_user(user_id, name, destination, age)

        elif action == 'read':
            read_user(user_id)

        elif action == 'update':
            field = input("Enter field to update (name/destination/age): ")
            new_value = input("Enter new value: ")
            update_user(user_id, field, new_value)

        elif action == 'delete':
            delete_user(user_id)

    else:
        print("Invalid operation.")
