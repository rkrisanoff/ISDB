CREATE TABLE s284712.E_GAME (
    name VARCHAR(50) PRIMARY KEY,
    is_competitive BOOLEAN NOT NULL
);

CREATE TABLE s284712.E_CHILD (
    id SERIAL PRIMARY KEY, 
    name VARCHAR(50) NOT NULL,
    age INTEGER DEFAULT 0,
    gender BOOLEAN NOT NULL
);

CREATE TABLE s284712.E_ADULT (
    id SERIAL PRIMARY KEY, 
    name VARCHAR(50) NOT NULL,
    age INTEGER DEFAULT 0,
    gender BOOLEAN NOT NULL
);

CREATE TABLE s284712.E_GAME_INSTANCE (
    id SERIAL PRIMARY KEY, 
    name_of_the_game VARCHAR(50) NOT NULL,
    won_child_id INT 
    );

CREATE TABLE s284712.E_GAME_PARTICIPATION (
    child_id SERIAL,
    game_instance_id SERIAL,
    PRIMARY KEY (child_id,game_instance_id)
);

CREATE TABLE s284712.E_GAME_WATCHING (
    adult_id SERIAL,
    game_instance_id SERIAL,
    PRIMARY KEY (adult_id,game_instance_id)
);


ALTER TABLE s284712.E_GAME_INSTANCE ADD FOREIGN KEY (name_of_the_game) REFERENCES s284712.E_GAME (name);
ALTER TABLE s284712.E_GAME_INSTANCE ADD FOREIGN KEY (won_child_id) REFERENCES s284712.E_CHILD (id);
ALTER TABLE s284712.E_GAME_PARTICIPATION ADD FOREIGN KEY (game_instance_id) REFERENCES s284712.E_GAME_INSTANCE (id);
ALTER TABLE s284712.E_GAME_PARTICIPATION ADD FOREIGN KEY (child_id) REFERENCES s284712.E_CHILD (id);
ALTER TABLE s284712.E_GAME_WATCHING ADD FOREIGN KEY (game_instance_id) REFERENCES s284712.E_GAME_INSTANCE (id);
ALTER TABLE s284712.E_GAME_WATCHING ADD FOREIGN KEY (adult_id) REFERENCES s284712.E_ADULT (id);


