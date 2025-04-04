# Frontend Website

## Build and Run the Frontend Container

To build and run the frontend container independently using Docker, follow these steps:

1. Ensure you have Docker installed on your machine.
2. Navigate to the `website` directory of the repository.
3. Run the following command to build the container:

```sh
docker build -t frontend-website .
```

4. Once the build is complete, run the container using the following command:

```sh
docker run -p 3000:3000 frontend-website
```

## Access the UI

You can access the UI in a browser using the following URL:

```
http://localhost:3000
```

## Verify Frontend-Backend Communication

To verify that the frontend is communicating correctly with the backend, follow these steps:

1. Open your browser and navigate to the frontend URL: http://localhost:3000
2. The frontend should make a call to the backend's `/api/greet/` endpoint and display the response.