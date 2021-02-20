# PugSQL Demo

A very top level demo of working with PugSQL in place of using an ORM

## Setup

* run `pipenv install -r requirements.txt`
* create your SQLite3 database in the top directory
* create a `.env` file with the following values: `DATABASE="<path to sqlite DB>"`
* On first time running `app.py` use the `create` option to make the user table:

`python app.py create`

* you can then use the below make_users method to populate the table

## Available methods

* make_users - takes a number for the number of fake uses you want to create
* find - takes an id and returns the user
* update - takes an id and a string for first_name
* delete - takes an user id and deletes the row

e.g. `python app.py make_users 50` - this will create 50 dummy users

