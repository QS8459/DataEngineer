FROM python:3.10-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the contents of the src directory on your machine to /app in the container
COPY /code /app

# Expose port 8000 for the application
EXPOSE 8000

# Run the application
CMD ["python3", "server.py"]

