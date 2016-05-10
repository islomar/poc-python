#!/bin/bash

docker build -t islomar/tornado-poc .
docker run -p 8888:8888 islomar/tornado-poc