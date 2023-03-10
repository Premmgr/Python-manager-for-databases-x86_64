CREATE DATABASE IF NOT EXISTS stage_db;
CREATE TABLE clients (
    profile_name INTEGER,
    url VARCHAR(255),
    client_id INTEGER,
    ticket INTEGER,
    comment TEXT
);

USE stage_db;

INSERT INTO stage_db (profile_name, url, client_id, ticket, comment)
VALUES ('demo-client#1234', 'https://example.come/123456767874', 'CLIENT1_012345678', 1234567, 'active user');
