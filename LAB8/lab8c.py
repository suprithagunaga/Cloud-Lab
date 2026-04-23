docker run --name mysql1 -e MYSQL_ROOT_PASSWORD=root -p 3306:3306 -d mysql:8

docker exec -it mysql1 mysql -uroot -proot
CREATE DATABASE shop;

 USE shop;

CREATE TABLE customers(
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100),
city VARCHAR(100)
);

CREATE TABLE orders(
id INT AUTO_INCREMENT PRIMARY KEY,
customer_id INT,
product VARCHAR(100),
amount INT,
FOREIGN KEY(customer_id) REFERENCES customers(id)
 );

('Alice','new york'),
('Bob','chicago'),
('Charlie','los angeles');

INSERT INTO orders (customer_id,product,amount) VALUES
    (1,'LAPTOP',1200),
    (1,'MOUSE',25),
    (2,'PHONE',800),
    (3,'TABLET',300),
    (2,'KEYBOARD',45);

 SELECT o.id,o.product,o.amount
  FROM orders o
  JOIN customers c ON o.customer_id=c.id
  WHERE c.name='Alice';

SELECT c.name,o.product,o.amount
 FROM customers c
 JOIN orders o ON c.id=o.customer_id
 WHERE o.amount > 500;


 SELECT name
     FROM customers
     WHERE id NOT IN( SELECT DISTINCT customer_id FROM orders);

 SELECT c.name,SUM(o.amount )AS total_spent
    -> FROM customers c
    -> JOIN orders o ON c.id=o.customer_id
    -> GROUP BY c.name
    -> ORDER BY total_spent DESC;
