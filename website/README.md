# Frontend Website Instructions

## Building and Running the Frontend Container Independently

To build and run the frontend container using Docker, follow these steps:

1. Ensure you have Docker installed on your machine.
2. Navigate to the `website` directory of the project.
3. Run the following command to build and start the container:

```sh
docker build -t frontend-website .
docker run -p 3000:3000 frontend-website
```

## Accessing the UI

You can access the UI in your browser using the following URL:

```
http://localhost:3000
```

## Verifying Frontend Communication with Backend

To verify that the frontend is communicating correctly with the backend, you can trigger a test call to the backend API (e.g., accessing the `/api/greet/` endpoint from the frontend).