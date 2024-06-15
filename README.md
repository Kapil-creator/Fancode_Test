# FanCode City ToDo Automation

This project automates the validation that users in the FanCode city have completed more than 50% of their todos tasks. The automation is implemented in Python using the requests library and pytest framework.

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/kapil-sdet/fancode-city-todo-automation.git
    cd fancode-city-todo-automation
    ```

2. Optionally, set up a virtual environment:

    ```bash
    python -m venv venv
    # On Windows: venv\Scripts\activate
    # On macOS/Linux: source venv/bin/activate
    pip install -r requirements.txt
    ```

3. Run the tests:

    ```bash
    pytest
    ```

## Project Structure

- `test_fancode_city.py`: Contains test cases to validate the completion percentage for users in the FanCode city.
- `api_automation.py`: Provides functions to interact with the FanCode city APIs.

## API Resources

- `/todos`
- `/posts`
- `/comments`
- `/albums`
- `/photos`
- `/users`

## Contributing

Contributions are welcome! Feel free to open issues or pull requests.


