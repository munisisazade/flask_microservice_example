FROM alpine:3.10.3

LABEL maintainer.name="Munis Isazade" \
      maintainer.email="munisisazade@gmail.com"

WORKDIR /code

COPY . .

RUN apk update --no-cache \
&& apk upgrade --no-cache \
&& apk add --no-cache python3 \
&& apk add libffi-dev \
&& apk add --no-cache --virtual .build-deps python3-dev postgresql-dev gcc musl-dev \
&& python3 -m venv .venv \
&& . .venv/bin/activate \
&& pip install --no-cache-dir -U pip \
&& pip install --no-cache-dir -r requirements.txt \
&& rm -f requirements.txt \
&& apk del .build-deps

ENV PATH="/code/.venv/bin:$PATH"

CMD ["python","-u","run.py"]
