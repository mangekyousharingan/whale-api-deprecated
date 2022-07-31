FROM python:3.9

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN pip install --no-cache-dir --upgrade poetry && \
    poetry config virtualenvs.create false && \
    poetry install

COPY . /app/

CMD ["uvicorn", "src.main:app", "--port", "80", "--host", "0.0.0.0"]
