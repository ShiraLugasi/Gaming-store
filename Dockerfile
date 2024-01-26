# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /shiralu

# Copy the contents of the local directory into the container at /shiralu
COPY . /shiralu

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r versions.txt

# Expose port 8000 to the outside world
EXPOSE 8000

# Run uvicorn when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]


