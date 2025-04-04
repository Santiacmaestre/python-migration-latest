# Backend Service

## Build and Run the Backend Container

1. Ensure Docker is installed on your machine.
2. Navigate to the `service/` directory.
3. Run the following command to build and start the backend container:

```sh
docker build -t backend-service .
docker run -p 8000:8000 backend-service
```

## Access the API Endpoint

- Open your browser or API client (e.g., curl, Postman) and navigate to: http://localhost:8000/api/greet/

## Access the Django Admin Panel

- Open your browser and navigate to: http://localhost:8000/admin/

## Verify Python and Django Versions

- The Python and Django versions are displayed on the bottom right corner of the Django admin login screen.
