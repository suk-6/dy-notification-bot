FROM python:3.9 as base

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY app.py .
COPY api.py .
COPY models.py .

FROM node:18-alpine as frontend

WORKDIR /app

COPY frontend/package.json .
COPY frontend/yarn.lock .

RUN yarn install

COPY frontend .

RUN yarn build

FROM base as final

COPY --from=frontend /app/public ./frontend/public

CMD ["python", "/app/app.py"]