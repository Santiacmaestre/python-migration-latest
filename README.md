# python-migration-latest
This repository contains tests and experiments for migrating code from Python 3.7 to the latest stable Python version. It aims to identify compatibility issues, modernize syntax, and validate dependencies across environments.

## Build and Run the Full System

To build and run the full system using Docker Compose, follow these steps:

1. Ensure you have Docker and Docker Compose installed on your machine.
2. Navigate to the root directory of the repository.
3. Run the following command to build and start the containers:

```sh
docker-compose up --build
```

## Exposed Ports

- Frontend: http://localhost:3000
- Backend: http://localhost:8000

## Verify Communication

To verify that the frontend and backend can communicate successfully, follow these steps:

1. Open your browser and navigate to the frontend URL: http://localhost:3000
2. The frontend should make a call to the backend's `/api/greet/` endpoint and display the response.
