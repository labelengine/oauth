FROM python:3.6-alpine

RUN apk update && apk --no-cache add libffi-dev \
                                     bash \
                                     build-base \
                                     postgresql-dev

WORKDIR root/

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ app/
COPY oauth.py .
COPY docker/entrypoint.sh .

ENV DB_HOST=identities_db
ENV DB_NAME=identities
ENV FLASK_APP=oauth.py

ENTRYPOINT ["/bin/bash", "entrypoint.sh"]
