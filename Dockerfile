FROM python:3.9

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN pip install --no-cache-dir --upgrade poetry && \
    poetry config virtualenvs.create false && \
    poetry install

COPY /src /app/src/

WORKDIR /app/src/

CMD ["python", "main.py"]

# TODO: add entrypoint