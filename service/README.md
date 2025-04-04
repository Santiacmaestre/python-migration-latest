# Backend Service

## Build and Run the Backend Container

To build and run the backend container individually using Docker, follow these steps:

1. Ensure you have Docker installed on your machine.
2. Navigate to the `service` directory of the repository.
3. Run the following command to build the container:

```sh
docker build -t backend-service .
```

4. Once the build is complete, run the container using the following command:

```sh
docker run -p 8000:8000 backend-service
```

## Access the `/api/greet/` Endpoint

You can access the `/api/greet/` endpoint from a browser or API client (e.g., curl, Postman) using the following URL:

```
http://localhost:8000/api/greet/
```

## Access the Django Admin Panel

To access the Django admin panel, follow these steps:

1. Open your browser and navigate to the following URL:

```
http://localhost:8000/admin/
```

2. Log in using your admin credentials.

## Verify Python and Django Versions

To verify the Python and Django versions displayed on the Django admin login screen, look at the bottom right corner of the login page. The versions should be displayed there.