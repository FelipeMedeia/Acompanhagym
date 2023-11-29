FROM python:alpine
COPY . /app/
RUN pip install --no-cache-dir "Django>=3.0,<4"
ENV PYTHONUNBUFFERED=1
CMD python /app/manage.py runserver 0.0.0.0:8000