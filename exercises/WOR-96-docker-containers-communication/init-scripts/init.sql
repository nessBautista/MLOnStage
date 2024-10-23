CREATE TABLE movies (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255),
  release_year INT
);

CREATE TABLE actors (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  birthdate DATE
);

CREATE TABLE directors (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  birthdate DATE
);

INSERT INTO movies (title, release_year) VALUES ('Inception', 2010), ('The Matrix', 1999);
INSERT INTO actors (name, birthdate) VALUES ('Leonardo DiCaprio', '1974-11-11'), ('Keanu Reeves', '1964-09-02');
INSERT INTO directors (name, birthdate) VALUES ('Christopher Nolan', '1970-07-30'), ('Lana Wachowski', '1965-06-21');