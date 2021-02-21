-- :name create_user :insert
insert into users (title, first_name, last_name, email, phone)
values (:title, :first_name, :last_name, :email, :phone)

-- :name find_user :one
select * from users where user_id = :user_id

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
select * from users;