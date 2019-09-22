FROM python:3.7

ENV PYTHONUNBUFFERED 1
ENV POETRY_VERSION "0.12.17"

WORKDIR /app
ADD . /app

RUN pip install --upgrade pip

ENV PATH $HOME/.poetry/bin:$PATH
ENV PYTHONPATH .

RUN pip install --no-cache-dir poetry==${POETRY_VERSION}
RUN poetry config settings.virtualenvs.create false

# install poetry dependencies
ADD pyproject.toml .
ADD poetry.lock .

RUN poetry install

EXPOSE $PORT

CMD ["manage.py runserver 0.0.0.0:$PORT"]
