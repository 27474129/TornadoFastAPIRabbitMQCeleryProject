CREATE TABLE appeals (
    id SERIAL,
    surname VARCHAR NOT NULL,
    name VARCHAR NOT NULL,
    patronymic VARCHAR NOT NULL,
    phone numeric(15) NOT NULL,
    appeal_text VARCHAR NOT NULL
);