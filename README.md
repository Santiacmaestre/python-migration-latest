# Project Setup

## Build and Run the Full System

1. Ensure Docker and Docker Compose are installed on your machine.
2. Navigate to the root directory of the project.
3. Run the following command to build and start the containers:

```sh
docker-compose up --build
```

## Exposed Ports

- Frontend: http://localhost:3000
- Backend: http://localhost:8000

## Verify Communication

1. Open your browser and navigate to the frontend URL: http://localhost:3000
2. The frontend should be able to communicate with the backend. You can verify this by triggering a test call to the backend API (e.g., accessing the `/api/greet/` endpoint).
