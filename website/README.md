# Frontend Website

## Instructions for building and running the frontend container independently using Docker

1. **Build and run the frontend container**:
    ```sh
    docker build -t frontend-website .
    docker run -p 3000:3000 frontend-website
    ```

2. **Access the UI in a browser**:
    - URL: `http://localhost:3000`

3. **Verify frontend-backend communication**:
    - Trigger a test call to the backend API from the frontend and ensure it responds correctly.