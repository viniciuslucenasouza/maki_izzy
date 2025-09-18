# Event Processing Engine

This project is a platform that receives events and uses them to send messages, like emails or Slack messages. This `README.md` provides guidance on setting up and running the project, along with best practices for development.

## Project Structure

- `backend/`: Contains the FastAPI application for the event processing engine.
- `frontend/`: (Currently on hold) Intended for the React-based user interface.

## Backend Setup

### Prerequisites

- Python 3.9+
- pip

### Installation

1.  **Navigate to the backend directory:**
    ```bash
    cd backend
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

To run the backend development server, use the following command from the root directory:

```bash
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

The `--reload` flag will automatically restart the server when you make changes to the code.

### API Documentation

Once the server is running, you can access the interactive API documentation (provided by Swagger UI) at:

[http://localhost:8000/docs](http://localhost:8000/docs)

You can also access the ReDoc documentation at:

[http://localhost:8000/redoc](http://localhost:8000/redoc)

## Development Best Practices

### Code Style

- **Python (Backend):**
    - This project should use `black` for code formatting and `flake8` for linting to ensure a consistent code style.
    - **To format your code:** `black backend/`
    - **To check for style issues:** `flake8 backend/`

### Testing

- A comprehensive test suite should be developed to ensure the reliability of the application.
- Tests should be placed in a `backend/tests/` directory.
- `pytest` should be used as the testing framework.
- **To run tests:** `pytest backend/tests/`

### Commits

- Commit messages should follow the [Conventional Commits](https://www.conventionalcommits.org/) specification. This helps in maintaining a clear and understandable commit history.
- Example: `feat: Add user authentication endpoint`
- Example: `fix: Correctly handle Excel parsing errors`
- Example: `docs: Update README with setup instructions`
