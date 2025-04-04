# Backend Service

## Instructions for Building and Running the Backend Container Individually

### Step 1: Build the Backend Container

Run the following command to build the backend container:

```sh
docker build -t backend-service .
```

### Step 2: Run the Backend Container

Run the following command to start the backend container:

```sh
docker run -p 8000:8000 backend-service
```

## Accessing the /api/greet/ Endpoint

You can access the `/api/greet/` endpoint from a browser or API client (e.g., curl, Postman) using the following URL:

```
http://localhost:8000/api/greet/
```

## Accessing the Django Admin Panel

You can access the Django admin panel at the following URL:

```
http://localhost:8000/admin/
```

## Verifying Python and Django Versions

The Python and Django versions are displayed on the Django admin login screen (bottom right corner). Open the Django admin panel and check the versions displayed there.