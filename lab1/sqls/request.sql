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
WHERE
    child.gender = 'male'
GROUP BY
    child.id,
    friendship.child_id,
    game_participation.child_id,
    game_instance.id,
    game.id,
    friendship.power
HAVING
    (
        (count(*) > 5)
        OR (
            count(*) <= 5
            AND friendship.power = 99
        )
    );