# Use an official lightweight Python base image
FROM python:3.9-slim

# Set the working directory in the Docker container
WORKDIR /app

# Copy the current directory contents (chatbot script) into the container at /app
COPY . /app

# Run the chatbot script when the container launches
CMD ["python", "./chatbot.py"]
