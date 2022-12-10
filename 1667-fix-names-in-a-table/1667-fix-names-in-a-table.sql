select user_id, concat(UPPER(SUBSTR(Users.name,1,1)),LOWER(SUBSTR(Users.name,2))) name from Users order by user_id;
