import pytest
from api_automation import get_users_in_fancode_city, get_user_todos, calculate_completed_task_percentage

@pytest.fixture
def user_in_fancode_city():
    # Fixture to get a user in the FanCode city for testing
    users_in_fancode_city = get_users_in_fancode_city()
    if not users_in_fancode_city:
        pytest.skip("No users found in FanCode city for testing.")
    return users_in_fancode_city[0]

def test_completed_task_percentage_greater_than_50(user_in_fancode_city):
    # Test that completed task percentage is greater than 50% for a user in the FanCode city
    user_todos = get_user_todos(user_in_fancode_city['id'])
    percentage_completed = calculate_completed_task_percentage(user_todos)
    assert percentage_completed > 50, f"User {user_in_fancode_city['name']} has less than 50% completed tasks."

def test_no_users_in_fancode_city():
    # Test scenario when there are no users in the FanCode city
    # This test is expected to be skipped
    with pytest.raises(pytest.skip.Exception):
        get_users_in_fancode_city()

if __name__ == "__main__":
    pytest.main([__file__])
