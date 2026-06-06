FROM python:3.10-slim
RUN pip install psutil
COPY app1.py /app/app.py
CMD ["python", "/app/app.py"]
