# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Print Python version
RUN python -m pip install --upgrade pip

# Install libpq-dev for pg_config
RUN apt-get update \
    && apt-get install -y libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory to /app
WORKDIR /app

# Copy the application files into the container
COPY . /app

# Uninstall psycopg2 and install psycopg2-binary
RUN python -m pip uninstall -y psycopg2 \
    && python -m pip install --no-cache-dir -r requirements.txt

# # Add NLTK data download commands
# RUN python -m nltk.downloader punkt stopwords wordnet

# Expose port 8517 for the application
EXPOSE 8560

# Start the application
CMD ["python3", "runserver.py", "--host", "0.0.0.0", "--port", "8560"]
