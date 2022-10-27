/*markdown
## Шаг первый
Выбираем и выводим список всех детей
*/

SELECT
    *
FROM
    child
GROUP BY
    child.id
ORDER BY
    child.id;

/*markdown
## Шаг second

Находим количество всех дружб (с помощью оператора иннер джойн)
*/

SELECT
    child.id AS child_id,
    child.name AS child_name,
    friendship.adult_id as adult_id,
    friendship.power as power,
    friendship.power=99 as "равео 99"
FROM
    (
        child
        JOIN friendship ON child.id = friendship.child_id
    )
GROUP BY
    child.id,
    friendship.child_id,
    friendship.adult_id
ORDER BY
    child.id,
    friendship.adult_id;

SELECT
    child.id AS child_id,
    child.name AS child_name,
    count (child.id)  as friends_count
FROM
    (
        child
        JOIN friendship ON child.id = friendship.child_id
    )
GROUP BY
    child.id
ORDER BY
    child.id;

SELECT
    child.id AS child_id,
    child.name AS child_name
FROM
    (
        child
        JOIN friendship ON child.id = friendship.child_id
    )
GROUP BY
    child.id,
    friendship.power
HAVING
    (
        child.gender = 'male'
        AND (
            (count(*) > 5)
            OR (
                count(*) <= 5
                AND friendship.power = 99
            )
        )
    )
ORDER BY child.id    ;

SELECT
    child.id AS child_id,
    child.name AS child_name,
    game_participation.game_instance_id
FROM
    (
        child
        JOIN friendship ON child.id = friendship.child_id
        JOIN game_participation ON child.id = game_participation.child_id
    )
GROUP BY
    child.id,
    game_participation.game_instance_id,
    friendship.power
HAVING
    (
        child.gender = 'male'
        AND (
            (count(*) > 5)
            OR (
                count(*) <= 5
                AND friendship.power = 99
            )
        )
    )
ORDER BY child.id    ;

SELECT
    child.id AS child_id,
    child.name AS child_name,
    game_instance.id AS game_instance_id,

    game_instance.game_id
FROM
    (
        child
        JOIN friendship ON child.id = friendship.child_id
        JOIN game_participation ON friendship.child_id = game_participation.child_id
        JOIN game_instance ON game_participation.game_instance_id = game_instance.id
    )
GROUP BY
    child.id,
    friendship.child_id,
    game_participation.child_id,
    game_instance.id,
    friendship.power
HAVING
    (
        child.gender = 'male'
        AND (
            (count(*) > 5)
            OR (
                count(*) <= 5
                AND friendship.power = 99
            )
        )
    );

SELECT
    game.id AS game_type_id,
    game.name AS game_name,
    game_instance.id AS game_instance_id,
    child.id AS child_id,
    child.name AS child_name
FROM
    (
        child
        JOIN friendship ON child.id = friendship.child_id
        JOIN game_participation ON friendship.child_id = game_participation.child_id
        JOIN game_instance ON game_participation.game_instance_id = game_instance.id
        JOIN game ON game_instance.game_id = game.id
    )
GROUP BY
    child.id,
    friendship.child_id,
    game_participation.child_id,
    game_instance.id,
    game.id,
    friendship.power
HAVING
    (
        child.gender = 'male'
        AND (
            (count(*) > 5)
            OR (
                count(*) <= 5
                AND friendship.power = 99
            )
        )
    );