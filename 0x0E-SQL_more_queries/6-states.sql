-- creates database, table in database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
    id INT NOT PRIMARY KEY AUTO_INCREMENT,
    name VARHCAR(256) NOT NULL);
