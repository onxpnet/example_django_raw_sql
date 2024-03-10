FROM python:3.12-slim-bookworm AS base
# FROM gcr.io/distroless/python3-debian12:latest

# install pdm dependencies
RUN python -m pip install pdm --no-cache-dir

FROM base AS build
WORKDIR /app
COPY . /app
RUN pdm build

FROM python:3.12-alpine AS deployment
RUN addgroup -S nonroot \
    && adduser -S nonroot -G nonroot
WORKDIR /app
COPY --from=build /app/dist/*.whl .
RUN chown -R nonroot /app/*whl
USER nonroot
RUN pip install *.whl --no-cache-dir --prefer-binary
WORKDIR /home/nonroot/.local/lib/python3.12/site-packages/
RUN pip install granian
EXPOSE 8000
CMD ["python", "-m", "granian", "--host", "0.0.0.0", "--interface", "wsgi", "djangosql.wsgi:application"]

# Runing docker images
# docker run -e "SECRET_KEY=kunci_rahasia" -e "ALLOWED_HOSTS=*" -e "DEBUG=True" -p 8000:8000 django_sql
# alternative docker-compose.yml -> docker compose up / docker compose restart