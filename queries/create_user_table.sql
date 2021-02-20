-- :name create_user_table

CREATE TABLE users (
	user_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	email TEXT NOT NULL UNIQUE,
	phone TEXT NOT NULL UNIQUE
);