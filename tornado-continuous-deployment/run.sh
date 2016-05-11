#!/bin/bash

docker build -t islomar/tornado-poc .
docker run --name tornado-poc -d -p 8888:8888 islomar/tornado-poc 
docker commit -m "Blabla" islomar/tornado-poc:v1
docker push islomar/tornado-poc

docker pull islomar/tornado-poc

docker run -d -P islomar/tornado-poc python hello-world.py


docker run --name tornado-nginx -v nginx.conf:/etc/nginx/nginx.conf:ro -d nginx

docker history islomar/tornado-poc
docker inspect tornado-poc
docker logs -f tornado-poc

docker exec tornado-poc ls
docker exec tornado-poc curl http://localhost:8888