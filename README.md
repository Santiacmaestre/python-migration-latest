# python-migration-latest
This repository contains tests and experiments for migrating code from Python 3.7 to the latest stable Python version. It aims to identify compatibility issues, modernize syntax, and validate dependencies across environments.

## Instructions to build and run the full system

1. **Build and run the system**:
    ```sh
    docker-compose up --build
    ```

2. **Exposed Ports and Services**:
    - Frontend: 3000
    - Backend: 8000

3. **Verify communication between frontend and backend**:
    - Ensure the frontend can call the backend's `/api/greet/` endpoint successfully.
