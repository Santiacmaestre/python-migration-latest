# Backend Service

## Instructions for building and running the backend container individually using Docker

1. **Build and run the backend container**:
    ```sh
    docker build -t backend-service .
    docker run -p 8000:8000 backend-service
    ```

2. **Access the `/api/greet/` endpoint**:
    - From a browser: `http://localhost:8000/api/greet/`
    - Using curl: `curl http://localhost:8000/api/greet/`
    - Using Postman: Create a new GET request to `http://localhost:8000/api/greet/`

3. **Access the Django admin panel**:
    - URL: `http://localhost:8000/admin/`

4. **Verify Python and Django version**:
    - Check the bottom right corner of the Django admin login screen to see the Python and Django version displayed.