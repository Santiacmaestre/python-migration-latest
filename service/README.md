# Backend Setup

## Build and Run

To build and run the backend container individually using Docker, follow these steps:

1. Navigate to the `service/` directory.
2. Run the following command to build and start the container:

```sh
docker build -t backend-service .
docker run -p 8000:8000 backend-service
```

## Accessing the API

To access the `/api/greet/` endpoint from a browser or API client (e.g. curl, Postman), use the following URL:

```
http://localhost:8000/api/greet/
```

## Accessing the Django Admin Panel

To access the Django admin panel, use the following URL:

```
http://localhost:8000/admin/
```

## Verify Python and Django Version

To verify the Python and Django version displayed on the Django admin login screen, navigate to the admin panel URL and check the bottom right corner of the login screen.