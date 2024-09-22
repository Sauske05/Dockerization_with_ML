# Use the official Python image from the Docker Hub
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Expose the port Django will run on
EXPOSE 8000

# Define the command to run Django's development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
