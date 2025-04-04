# Backend Service

## Build and Run the Backend Container Individually

1. Navigate to the `service` directory:
```sh
$ cd service
```

2. Build the Docker image:
```sh
$ docker build -t backend-service .
```

3. Run the Docker container:
```sh
$ docker run -p 8000:8000 backend-service
```

## Access the `/api/greet/` Endpoint

- Open a browser or API client (e.g., curl, Postman)
- Navigate to `http://localhost:8000/api/greet/`

## Access the Django Admin Panel

- Open a browser and navigate to `http://localhost:8000/admin/`

## Verify Python and Django Versions

- Check the bottom right corner of the Django admin login screen for the Python and Django version information