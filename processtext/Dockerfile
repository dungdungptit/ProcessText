FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
# RUN apt-get update && apt-get install -y gcc python3-dev musl-dev  libffi-dev netcat
RUN pip install --upgrade pip

WORKDIR /

COPY . .

RUN pip install -r requirements.txt

EXPOSE 9000