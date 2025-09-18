# Project Roadmap

This document outlines the future development plans for the event processing engine.

## Backend Roadmap

The backend is the core of the application. The following features are planned to enhance its capabilities:

-   **Authentication and Authorization:**
    -   Implement OAuth2 or another authentication mechanism to secure the API endpoints.
    -   Add role-based access control (RBAC) to restrict access to certain features.

-   **Connectors:**
    -   Develop a modular connector system to allow sending messages to various platforms.
    -   **Initial connectors:**
        -   Email (using SMTP)
        -   Slack (using the Slack API)

-   **Database Integration:**
    -   Integrate a relational database (e.g., PostgreSQL) using an ORM like `SQLAlchemy`.
    -   Store event data, message templates, and message logs in the database.

-   **Real-time Event Processing:**
    -   Integrate a message queue (e.g., RabbitMQ or Kafka) to handle events in a real-time, asynchronous manner.
    -   This will improve the scalability and reliability of the platform.

-   **Testing:**
    -   Develop a comprehensive test suite with unit and integration tests using `pytest`.
    -   Aim for high test coverage to ensure the stability of the application.

## Frontend Roadmap

The frontend development is currently on hold due to environmental issues. Once these are resolved, the following features are planned:

-   **Environment Setup:**
    -   Resolve the `npm` issues in the development sandbox to enable frontend development.

-   **User Interface:**
    -   Build a user-friendly interface for managing event sources, message templates, and connectors.
    -   Create a dashboard to view the history of events and the status of sent messages.

-   **Template Builder:**
    -   Implement a visual or text-based editor to make it easy for users to create and preview message templates.

## Code Analysis and Security

To ensure the quality and security of the codebase, the following tools and practices are recommended:

### Backend (Python)

-   **Code Formatting:**
    -   `black`: For consistent and automatic code formatting.

-   **Static Analysis & Linting:**
    -   `flake8`: To check for style guide violations and potential errors.
    -   `mypy`: For static type checking to catch type-related bugs.
    -   `bandit`: To scan for common security vulnerabilities in the code.

-   **Dependency Security:**
    -   `safety` or `pip-audit`: To check for known security vulnerabilities in the project's dependencies.

-   **Security Headers:**
    -   Implement security headers (e.g., `Content-Security-Policy`, `X-Content-Type-Options`) using FastAPI middleware to protect against common web vulnerabilities.

### Frontend (JavaScript/React)

-   **Code Formatting:**
    -   `prettier`: For consistent code formatting.

-   **Static Analysis & Linting:**
    -   `eslint`: To identify and fix problems in the JavaScript code.

-   **Dependency Security:**
    -   `npm audit` or `snyk`: To scan for vulnerabilities in the frontend dependencies.
