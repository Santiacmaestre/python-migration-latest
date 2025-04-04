# Frontend Website

## Build and Run the Frontend Container Individually

1. Navigate to the `website` directory:
```sh
$ cd website
```

2. Build the Docker image:
```sh
$ docker build -t frontend-website .
```

3. Run the Docker container:
```sh
$ docker run -p 3000:3000 frontend-website
```

## Access the UI

- Open a browser and navigate to `http://localhost:3000`

## Verify Frontend-Backend Communication

- Trigger a test call to the backend API from the frontend UI