# Frontend Website

## Instructions for Building and Running the Frontend Container Individually

### Step 1: Build the Frontend Container

Run the following command to build the frontend container:

```sh
docker build -t frontend-website .
```

### Step 2: Run the Frontend Container

Run the following command to start the frontend container:

```sh
docker run -p 3000:3000 frontend-website
```

## Accessing the UI

You can access the UI in a browser using the following URL:

```
http://localhost:3000
```

## Verifying Frontend and Backend Communication

To verify that the frontend is communicating correctly with the backend, trigger a test call to the backend API from the frontend. Open the frontend UI and perform an action that calls the backend’s `/api/greet/` endpoint. Ensure that the response is received successfully.