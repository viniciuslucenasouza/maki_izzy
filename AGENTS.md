# AI Assistant Guide for the Event Processing Engine

This document provides guidance for AI assistants working on this project.

## Project Overview

The goal of this project is to create a platform that receives events from various sources, processes them, and sends out messages (like emails or Slack notifications) based on customizable templates. The project is divided into a backend (the processing engine) and a frontend (the user interface).

## Technology Stack

- **Backend:** Python with [FastAPI](https://fastapi.tiangolo.com/)
- **Frontend:** JavaScript with [React](https://reactjs.org/) (Note: The frontend is currently on hold due to environmental issues in the development sandbox).
- **Data Handling:** [Pydantic](https://pydantic-docs.helpmanual.io/) for data validation and `pandas` for Excel file processing.

## Project Structure

- `backend/`: This directory contains all the Python code for the FastAPI application.
  - `main.py`: The main entry point of the application, containing the API endpoints.
  - `models.py`: The Pydantic models for data validation and structure.
  - `requirements.txt`: The list of Python dependencies.
- `README.md`: Contains setup and development instructions for human developers.
- `ROADMAP.md`: Outlines the future development plans for the project.

## Development Workflow

1.  **Understand the Goal:** Before making any changes, carefully read the user's request and the project's overall goals described in this document and the `README.md`.
2.  **Plan Your Changes:** Use the `set_plan` tool to create a clear, step-by-step plan. If you need to modify an existing plan, get user approval for significant changes.
3.  **Focus on the Backend:** For now, all development should be focused on the backend. Do not attempt to work on the frontend unless the user explicitly asks for it and the environmental issues are resolved.
4.  **Stay Consistent:** Follow the existing code style and structure. Use Pydantic for data models and create new endpoints in `main.py` as needed.
5.  **Verify Your Work:** After making changes, run the backend server and use `curl` or another tool to test the endpoints. Ensure that your changes work as expected and have not introduced any regressions.
6.  **Keep it Clean:** Do not commit temporary files, logs, or build artifacts like `__pycache__`.
7.  **Document Your Work:** For new features, consider if the `README.md` or other documentation needs to be updated.

## How to Run the Backend

To run the development server, use the following command from the project's root directory:

```bash
uvicorn backend.main:app --reload
```

This will start the server on `http://localhost:8000`. You can access the API documentation at `http://localhost:8000/docs`.
