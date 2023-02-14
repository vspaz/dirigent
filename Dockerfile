FROM python:3.10-bullseye

WORKDIR /ork8r

COPY . /ork8r

RUN apt-get update && apt-get upgrade -y \
    && apt-get install -y \
        python-dev  \
        procps \
        vim \
        less \
        telnet \
        curl \
        net-tools \
        build-essential \
        python3-mysqldb \
        default-libmysqlclient-dev \
        mariadb-client

RUN pip install -r requirements/prod.txt

EXPOSE 8000

CMD ["python3", "src/manage.py", "runserver", "0.0.0.0:8000"]