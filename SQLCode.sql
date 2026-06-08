CREATE DATABASE bank_db;

USE bank_db;

CREATE TABLE accounts (
    account_no INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    balance DECIMAL(10,2)
);