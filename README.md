# django_sql

```sh
# Runing docker images
docker run -e "SECRET_KEY=kunci_rahasia" -e "ALLOWED_HOSTS=*" -e "DEBUG=True" -p 8000:8000 django_sql
# alternative docker-compose.yml -> docker compose up / docker compose restart
```

```sh
# pull images dari docker-compose
docker compose pull
# build compose
docker compose build
# run compose
docker compose up
# jalanin compose dengan daemon
docker compose up -d
# restart compose
docker compose restart
# stop compose
docker compose down

# masuk ke container
docker exec -it <container_id/container_name> /bin/sh
```