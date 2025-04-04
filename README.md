# python-migration-latest

## Build and Run the Full System

1. Clone the repository:
```sh
$ git clone <repository-url>
$ cd <repository-directory>
```

2. Checkout the branch `python-3.6-to-3.11`:
```sh
$ git checkout python-3.6-to-3.11
```

3. Build and run the system using Docker Compose:
```sh
$ docker-compose up --build
```

4. The following ports are exposed:
- Frontend: 3000
- Backend: 8000

5. Verify communication between frontend and backend:
- Open the frontend at `http://localhost:3000`
- Ensure the frontend can call the backend's `/api/greet/` endpoint
