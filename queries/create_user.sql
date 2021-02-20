-- :name create_user :insert

insert into users (title,first_name,last_name,email,phone) values (:title,:first_name,:last_name,:email,:phone)