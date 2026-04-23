docker run --name pg-test -e POSTGRES_PASSWORD=root -d -p 5432:5432 postgres

docker exec -it pg-test psql -U postgres

CREATE TABLE users(
id TEXT PRIMARY KEY,
name TEXT,
age INT
);

INSERT INTO users VALUES('p01','ganesh',30);
INSERT INTO users VALUES('p02','suresh',40);
SELECT * FROM users;
