import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

todos_by_user = {}
print("Initial todos_by_user:", todos_by_user)

# Increment complete TODOs count for each user.
for todo in todos:
    print("\nProcessing todo:", todo)
    if todo["completed"]:
        try:
            # Increment the existing user's count.
            todos_by_user[todo["userId"]] += 1
            print(f"Incremented count for userId {todo['userId']} to {todos_by_user[todo['userId']]}")
        except KeyError:
            # This user has not been seen. Set their count to 1.
            todos_by_user[todo["userId"]] = 1
            print(f"UserId {todo['userId']} not seen before. Initialized count to 1.")

print("\nFinal todos_by_user:", todos_by_user)

# Create a sorted list of (userId, num_complete) pairs.
top_users = sorted(todos_by_user.items(), 
                   key=lambda x: x[1], reverse=True)
print("\nTop users sorted:", top_users)

# Get the maximum number of complete TODOs.
max_complete = top_users[0][1]
print("\nMaximum number of complete TODOs:", max_complete)

# Create a list of all users who have completed
# the maximum number of TODOs.
users = []
for user, num_complete in top_users:
    if num_complete < max_complete:
        break
    users.append(str(user))
    print(f"Added userId {user} to the list of users with maximum complete TODOs")

max_users = " and ".join(users)
print("\nUsers with the most completed TODOs:", max_users)

# Define a function to filter out completed TODOs 
# of users with max completed TODOS.
def keep(todo):
    is_complete = todo["completed"]
    has_max_count = str(todo["userId"]) in users
    return is_complete and has_max_count

# Write filtered TODOs to file.
with open("filtered_data_file.json", "w") as data_file:
    filtered_todos = list(filter(keep, todos))
    json.dump(filtered_todos, data_file, indent=2)

