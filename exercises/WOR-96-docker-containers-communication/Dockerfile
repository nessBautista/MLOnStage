# Use the official Python 3.8 slim image as the base
FROM python:3.8-slim

# Set the working directory inside the container to /app
WORKDIR /app 

# Copy the requirements.txt file from the host to the container's /app directory
COPY app/requirements.txt ./
# Install the Python dependencies listed in requirements.txt
# --no-cache-dir reduces the image size by not caching the downloaded packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files from the current directory on the host to the container's /app directory
COPY . .

# Specify the command to run when the container starts
# This will execute "python app.py"
CMD ["python", "app/app.py"]