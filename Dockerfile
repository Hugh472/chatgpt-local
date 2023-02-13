# Use an official Python runtime as the base image
FROM python:3.8-slim-buster

# Set the working directory
WORKDIR /app

# Copy the required files to the container
COPY . .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Set the environment variable for the OpenAI API key
ENV API_KEY YOUR_OPENAI_API_KEY

# Expose the default Flask port
EXPOSE 5000

# Set the entrypoint command to run the Flask app
ENTRYPOINT ["python", "app.py"]
