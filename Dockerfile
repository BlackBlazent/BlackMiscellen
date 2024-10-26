# Use the official Python image from Docker Hub
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements.txt file first to leverage Docker cache
COPY requirements.txt .

# Install any required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application into the container
COPY . .

# Make the "App/data/forbidden/backup/crossx/" directory invisible (Linux)
RUN chmod -R 700 App/data/forbidden/backup/crossx/

# Expose the application port
EXPOSE 5000

# Detect the operating system and set appropriate environment variables
ARG OS_TYPE
ENV OS_TYPE=${OS_TYPE:-linux}

# Set the default command to run your app based on OS
CMD ["sh", "-c", "if [ \"$OS_TYPE\" = \"windows\" ]; then python BlackDownloader.py; else python BlackDownloader.py; fi"]
