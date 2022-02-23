FROM python:3.9

ENV POETRY_VERSION=1.1.12
ARG ENVIRONMENT=production

RUN mkdir -p /src/

RUN apt-get update \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  \
    && pip install "poetry==$POETRY_VERSION" \
    && poetry config virtualenvs.create false

COPY poetry.lock poetry.lock
COPY pyproject.toml pyproject.toml

RUN poetry install $(if test "$ENVIRONMENT" = production; then echo "--no-dev"; fi)

COPY src/ /src/
WORKDIR /src/

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]