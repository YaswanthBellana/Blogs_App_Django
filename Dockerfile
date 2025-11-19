FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

# Install system dependencies needed by mysqlclient
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        default-libmysqlclient-dev \
        gcc \
        pkg-config \
        libmariadb-dev-compat && \
    rm -rf /var/lib/apt/lists/*

# Install pip dependencies
COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /code/

# Make entrypoint executable
RUN chmod +x /code/docker-entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/code/docker-entrypoint.sh"]
# CMD ["gunicorn", "blog.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
CMD ["gunicorn", "blog.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3", "--timeout", "90"]
