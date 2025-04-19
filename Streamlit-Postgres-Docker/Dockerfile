FROM python:3.9

# Set working directory
WORKDIR /app

# Install necessary Python packages
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the app files into the container
COPY . .

# Run Streamlit app
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
