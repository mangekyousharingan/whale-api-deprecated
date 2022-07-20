FROM python:3.9

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install

COPY . /app/

EXPOSE 80

CMD ["python", "src/main.py"]
