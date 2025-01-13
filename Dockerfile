FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# CMD ["python3", "velho-oeste/database.py"]
CMD ["tail", "-f", "/dev/null"]