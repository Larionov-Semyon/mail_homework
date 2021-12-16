FROM python:3

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /usr/src/new_journal

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

#COPY entrypoint.sh /entrypoint.sh
#RUN chmod +x /entrypoint.sh

#ENTRYPOINT ["/usr/src/new_journal/entrypoint.sh"]

COPY . .