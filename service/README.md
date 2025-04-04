# Backend Service Instructions

## Building and Running the Backend Container Individually

To build and run the backend container using Docker, follow these steps:

1. Ensure you have Docker installed on your machine.
2. Navigate to the `service` directory of the project.
3. Run the following command to build and start the container:

```sh
docker build -t backend-service .
docker run -p 8000:8000 backend-service
```

## Accessing the `/api/greet/` Endpoint

You can access the `/api/greet/` endpoint from a browser or API client (e.g., curl, Postman) using the following URL:

```
http://localhost:8000/api/greet/
```

## Accessing the Django Admin Panel

To access the Django admin panel, navigate to the following URL in your browser:

```
http://localhost:8000/admin/
```

## Verifying Python and Django Version

You can verify the Python and Django version displayed on the Django admin login screen at the bottom right corner.