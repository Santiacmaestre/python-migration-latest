# Project Migration to Python 3.11

## Instructions to Build and Run the Full System

### Step 1: Build and Run the System

Run the following command to build and run the entire system using Docker Compose:

```sh
docker-compose up --build
```

### Step 2: Identify Exposed Ports and Services

- Frontend: http://localhost:3000
- Backend: http://localhost:8000

### Step 3: Verify Frontend and Backend Communication

Open your browser and navigate to the frontend URL (http://localhost:3000). The frontend should successfully call the backend’s `/api/greet/` endpoint.
