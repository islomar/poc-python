FROM python:3-onbuild

# upgrade
RUN pip install --upgrade pip
RUN apt-get update && apt-get install -y vim
EXPOSE 8888

CMD [ "python", "./hello-world.py" ]