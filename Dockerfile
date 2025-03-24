# Use Python as base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy requirements.txt separately for caching
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy everything from registerform (including app.py)
COPY registerform/ /app/

# Expose port 5000
EXPOSE 5000

# Run the Flask app
CMD ["python", "/app/app.py"]
