FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Create directories including Data so we can seed initial documents if present
COPY . .

# Expose port and run server
EXPOSE 5000
CMD ["python", "server.py"]
