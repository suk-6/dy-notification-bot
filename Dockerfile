FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY app.py .
COPY api.py .
COPY models.py .
COPY frontend/public ./frontend/public

CMD ["python", "/app/app.py"]