FROM python:3.9-slim

WORKDIR /app

COPY monitor.py .
 
RUN pip install psutil

CMD ["python", "monitor.py"]
