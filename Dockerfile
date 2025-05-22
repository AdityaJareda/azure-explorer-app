FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV APP_IMAGE_URL="https://via.placeholder.com/300x200.png?text=App+Image+Not+Set"

CMD ["python", "app.py"]
