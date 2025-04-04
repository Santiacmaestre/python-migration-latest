# Frontend Website

## Build and Run the Frontend Container

1. Ensure Docker is installed on your machine.
2. Navigate to the `website/` directory.
3. Run the following command to build and start the frontend container:

```sh
docker build -t frontend-website .
docker run -p 3000:3000 frontend-website
```

## Access the UI

- Open your browser and navigate to: http://localhost:3000

## Verify Frontend-Backend Communication

- The frontend should be able to communicate with the backend. You can verify this by triggering a test call to the backend API (e.g., accessing the `/api/greet/` endpoint).
