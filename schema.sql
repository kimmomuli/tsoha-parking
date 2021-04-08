CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    admin INTEGER,
    visible INTEGER
);

CREATE TABLE parkinglot (
    id SERIAL PRIMARY KEY,
    owner_id INTEGER REFERENCES users,
    reserved INTEGER,
    who_reserved_id INTEGER,
    description TEXT,
    price INTEGER,
    time TIMESTAMP,
    visible INTEGER
);

CREATE TABLE location(
    id SERIAL PRIMARY KEY,
    parkinglot_id INTEGER REFERENCES parkinglot,
    city TEXT,
    address TEXT
);

CREATE TABLE comments(
    id SERIAL PRIMARY KEY,
    parkinglot_id INTEGER REFERENCES parkinglot,
    user_id INTEGER REFERENCES users,
    comment TEXT
);

CREATE TABLE stars(
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    parkinglot_id INTEGER REFERENCES parkinglot,
    star_count INTEGER,
    star_sum INTEGER
);
