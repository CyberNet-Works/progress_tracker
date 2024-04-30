CREATE TABLE Movies (
    id int,
    title varchar(200),
    release_year int,
    genre varchar(200)
);

INSERT INTO
    Movies (id, title, release_year, genre)

VALUES 
    (1, "The Social Network", 2010, "Drama"),
    (2, "The Imitation Game", 2014, "Drama / Thriller");

    SELECT * FROM Movies;