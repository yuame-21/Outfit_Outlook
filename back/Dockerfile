# Dockerfile

# Working from Python version 3.9
FROM python:3.9-alpine

# Set the working directory to /app
WORKDIR /app

# Copy requirements to the container
COPY back/requirements.txt requirements.txt

RUN pip install -r requirements.txt

# expose port 4000 from the container
EXPOSE 4000

# What command to run when image is executed inside container
CMD ["python", "app.py"]