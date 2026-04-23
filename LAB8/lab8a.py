docker run --name mysql-test -e MYSQL_ROOT_PASSWORD=root -d -p 3306:3306 mysql

docker exec -it mysql-test mysql -uroot -proot

CREATE DATABASE testdb;
USE testdb
CREATE TABLE users(
    id VARCHAR(10) PRIMARY KEY,
    name VARCHAR(50),
    age INT
    );

INSERT INTO users VALUES('u001','Alice',30);
INSERT INTO users VALUES('u002','Bob',25);

SELECT * FROM users;
