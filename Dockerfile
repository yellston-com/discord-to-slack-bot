FROM python:3.8-slim AS builder

ENV POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false \
    \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    \
    PYSETUP_PATH="/opt/pysetup"

ENV PATH="$POETRY_HOME/bin:$PATH"

RUN apt-get update && \
    apt-get install --no-install-recommends -y curl && \
    apt-get clean

RUN curl -sSL https://install.python-poetry.org/ | python -

ENV POETRY_NO_INTERACTION=1

# packages install
RUN mkdir /app
WORKDIR /app
COPY . /app/

RUN poetry install

CMD [ "poetry", "run", "python", "discord_notify/main.py" ]
