# Use the official Node.js image.
FROM node:18 AS frontend

# Set the working directory for the frontend.
WORKDIR /app/frontend

# Copy package.json and package-lock.json and install dependencies.
COPY frontend/package.json .
COPY frontend/package-lock.json .
RUN npm install

# Copy the frontend code.
COPY frontend/ .

# Build the SvelteKit application.
RUN npm run build

# Now switch to the backend stage
FROM python:3.12-slim AS backend

# Set the working directory for the backend.
WORKDIR /app/backend

# Copy the requirements file and install dependencies.
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend code.
COPY backend/ .

# Copy the built frontend files to the backend.
COPY --from=frontend /app/frontend/build /app/frontend/build

# Expose the FastAPI port.
EXPOSE 8000

# Install additional dependencies for running both backend and frontend
RUN apt-get update && apt-get install -y curl

# Set environment variables for the frontend
ENV FRONTEND_PORT=5173

# Command to start both the FastAPI and SvelteKit server
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port 8000 --reload & npm --prefix /app/frontend run preview"]
