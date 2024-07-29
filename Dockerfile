# NOTE: Docker engine must be running

# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /code

# Copy the current directory contents into the container at /app
COPY ./requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run app.py when the container launches (effectively runs the following command: "uvicorn src.main:app --host=0.0.0.0 --port=8000 --reload")
#src.main:app is the path to the main.py file /src/main.py(app)
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"] 
