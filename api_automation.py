import requests

API_BASE_URL = "https://jsonplaceholder.typicode.com"

def get_users_in_fancode_city():         #get_users_in_fancode_city function fetches all users and filters those belonging to the specified FanCode city based on latitude and longitude.
    users_in_fancode_city = []
    users_response = requests.get(f"{API_BASE_URL}/users")
    users = users_response.json()
    
    for user in users:
        lat, lng = float(user['address']['geo']['lat']), float(user['address']['geo']['lng'])
        if -40 <= lat <= 5 and 5 <= lng <= 100:
            users_in_fancode_city.append(user)
    
    return users_in_fancode_city

def get_user_todos(user_id):          #get_user_todos function fetches the todos for a specific user.
    todos_response = requests.get(f"{API_BASE_URL}/todos?userId={user_id}")
    return todos_response.json()

def calculate_completed_task_percentage(user_todos):         #calculate_completed_task_percentage function calculates the percentage of completed tasks for a user.
    total_tasks = len(user_todos)
    completed_tasks = sum(1 for todo in user_todos if todo['completed'])
    return (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0


#These functions can be used in test script (test_fancode_city.py) to interact with the FanCode city APIs and perform the necessary validations.




