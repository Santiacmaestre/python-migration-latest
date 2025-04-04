# Frontend Setup

## Build and Run

To build and run the frontend container independently using Docker, follow these steps:

1. Navigate to the `website/` directory.
2. Run the following command to build and start the container:

```sh
docker build -t frontend-website .
docker run -p 3000:3000 frontend-website
```

## Accessing the UI

To access the UI in a browser, use the following URL:

```
http://localhost:3000
```

## Verify Communication with Backend

To verify that the frontend is communicating correctly with the backend, trigger a test call to the backend API by accessing the following endpoint from the frontend application:

```
http://localhost:8000/api/greet/
```

You should see a response from the backend indicating successful communication.