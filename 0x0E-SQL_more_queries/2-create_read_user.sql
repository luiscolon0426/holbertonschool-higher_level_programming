-- Creates database hbtn_0d_2 and the user_0d_2 / password?
CREATE DATABASE IF NOT EXISTS hbtn_0d_02;
CREATE USER IF NOT EXISTS 'user_0d_2' @'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_od_2.* TO 'user_0d_2' @'localhost';