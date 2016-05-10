Last python version: 3.5.1

https://hub.docker.com/_/python/

docker run -p hostPort:containerPort

#Manual installation
virtualenv -p /usr/local/bin/python3.5 tornado-ve
workon tornado-ve
pip install -r requirements.txt
python hello-world.py
http://localhost:8888/
#deactivate tornado-ve