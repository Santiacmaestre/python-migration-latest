# Project Setup and Instructions

## Building and Running the Full System

To build and run the full system using Docker Compose, follow these steps:

1. Ensure you have Docker and Docker Compose installed on your machine.
2. Navigate to the root directory of the project.
3. Run the following command to build and start the containers:

```sh
docker-compose up --build
```

## Exposed Ports and Services

- Frontend: http://localhost:3000
- Backend: http://localhost:8000

## Verifying Communication Between Frontend and Backend

1. Open your browser and navigate to the frontend URL: http://localhost:3000
2. The frontend should be able to communicate with the backend. You can verify this by triggering a test call to the backend API (e.g., accessing the `/api/greet/` endpoint).
