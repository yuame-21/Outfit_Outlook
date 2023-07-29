# Dockerfile

# Working from Python version 3.9
FROM python:3.9-alpine

# Set the working directory to /weather_APP
WORKDIR /weather_app

# Copy requirements to the container
COPY requirements.txt requirements.txt

RUN pip install -r requirements.tt

# Copy all files into container within directory
COPY . .

# What command to run when image is executed inside container
CMD ["python", "app.py"]