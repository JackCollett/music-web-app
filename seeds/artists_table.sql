DROP TABLE IF EXISTS artists;
DROP SEQUENCE IF EXISTS artists_id_seq;


CREATE SEQUENCE IF NOT EXISTS artists_id_seq;
CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    artist text,
    genre text
);

INSERT INTO artists (artist) VALUES ('Pixies');
INSERT INTO artists (artist) VALUES ('ABBA');
INSERT INTO artists (artist) VALUES ('Taylor Swift');
INSERT INTO artists (artist) VALUES ('Nina Simone');