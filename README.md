# FFWEBAPP

## Quickstart
```
$ pip install -r requirements.txt
$ docker run --rm --name mongodb -p 27017:27017 -d mongo:3.6
$ docker exec -it mongodb mongo
> use TestDatabase
switched to db TestDatabase
> db.createCollection("TestCollection")
{ "ok" : 1 }
> quit()
$ python3 flaskMain.py
```