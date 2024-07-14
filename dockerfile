FROM python:3.8

# Set environment variables to avoid SSL verification issues
ENV PIP_TRUSTED_HOST pypi.python.org
ENV PIP_TRUSTED_HOST files.pythonhosted.org
ENV PIP_TRUSTED_HOST pypi.org

# Update pip to the latest version
RUN python -m pip install --upgrade pip

# Install application dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy application code
COPY . /app

WORKDIR /app

# Command to run your application
CMD ["python", "your_application.py"]
