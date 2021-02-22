# PugSQL Demo

A very top level demo of working with PugSQL in place of using an ORM. Uses FastAPI to also create a uvicron app API which can be used to query the database. Full docs can be found at: `http://127.0.0.1:8000/docs` (once you have the API running)

## Files

* `api.py` - the FastAPI app. Run using: `uvicorn api:app`
* `utilities.py` - a file containing database ultility methods for set up and manual testing
* `db.py` - module containing the database methods that are used to create, update, dlete and find users
* `models.py` - a collection of Pydantic models used by FastAPI to validate data where needed

## Setup

* run `pipenv install -r requirements.txt`
* create your SQLite3 database in the top directory
* create a `.env` file with the following values: `DATABASE="<path to sqlite DB>"`
* On first time running `app.py` use the `create` option to make the user table:

`python app.py create`

* you can then use the below `create` method to populate the table

## Available methods

* create-table - creates the inital User table
* create - takes a number for the number of fake uses you want to create
* find - takes an id and returns the user
* update - takes an id and a string for first_name
* delete - takes an user id and deletes the row

e.g. `python app.py create 50` - this will create 50 dummy users
