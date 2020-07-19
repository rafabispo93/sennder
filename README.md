# Sennder Python Back-end Assignment: Movie List

This is the Python backend challenge for a position at Sennder
More details you can find at 

## Deploy to Heroku

You can deploy this app yourself to Heroku to play with.

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Building

It is best to use the python `virtualenv` tool to build locally:

```sh
$ python -m venv venv
$ source venv/bin/activate or ./venv/Scripts/activate (Windows)
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py runserver
```

Then visit `http://localhost:8000/movies/` to view the app.

## Deploy to Heroku

Run the following commands to deploy the app to Heroku:

```sh
$ git clone https://github.com/rafabispo93/sennder.git
$ cd sennder
$ heroku create
$ git push heroku master:master
$ heroku open
```
