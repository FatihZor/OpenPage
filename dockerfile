FROM python:3-slim

WORKDIR /app/
COPY . .
RUN pip install -r requirements.txt

CMD ["python", "openpage/application.py"]