FROM python:3.7-alpine

RUN apk update && apk --no-cache add libffi-dev \
                                     build-base \
                                     postgresql-dev \
                                     python3-dev

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ app/
COPY oauth.py .
ENV FLASK_APP=oauth.py

ENTRYPOINT ["flask", "run"]
CMD ["--host", "0.0.0.0"]
