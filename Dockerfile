FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["uvicorn", "app.api.endpoints.documentation:router", "--host", "0.0.0.0", "--port", "8080"]