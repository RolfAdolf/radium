FROM python:3.9

RUN mkdir /app

WORKDIR /app

RUN pip install poetry

COPY poetry.lock pyproject.toml .

RUN poetry config virtualenvs.create false

RUN poetry install

COPY . .

RUN chmod a+x docker/*.sh

CMD ["bash", "docker/run_main_test.sh"]
