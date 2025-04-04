# Full System Setup

## Build and Run

To build and run the full system using Docker Compose, follow these steps:

1. Navigate to the root directory of the repository.
2. Run the following command to build and start the containers:

```sh
docker-compose up --build
```

## Exposed Ports

- Frontend: http://localhost:3000
- Backend: http://localhost:8000

## Verify Communication

To verify that the frontend and backend can communicate successfully:

1. Open your browser and navigate to the frontend URL: http://localhost:3000
2. Trigger a test call to the backend API by accessing the following endpoint:

```
http://localhost:8000/api/greet/
```

You should see a response from the backend indicating successful communication.
