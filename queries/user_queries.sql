-- :name create_user :insert
insert into users (title, first_name, last_name, email, phone)
values (:title, :first_name, :last_name, :email, :phone)

-- :name find_user_id :one
select user_id, title, first_name, last_name, email, phone from users where user_id = :user_id

-- :name find_user_email :one
select user_id, title, first_name, last_name, email, phone from users where email = :user_email

-- :name find_user_phone :one
select user_id, title, first_name, last_name, email, phone from users where phone = :user_phone

-- :name update_user
UPDATE users
SET 
title = :title,
first_name = :first_name,
last_name = :last_name,
email = :email,
phone = :phone
WHERE user_id = :user_id;

-- :name delete_user
DELETE FROM users 
WHERE user_id = :user_id;

-- :name get_users :many
select user_id, title, first_name, last_name, email, phone from users;

-- :name get_count
SELECT COUNT(first_name) FROM users;