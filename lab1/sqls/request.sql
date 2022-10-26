SELECT 
game_instance.id as game_instance_id,
    game.id as game_type_id,
    game.name as game_name,
    child.id as child_id,
    child.name as child_name
FROM (
        child 
        JOIN friendship ON child.id = friendship.child_id
        JOIN game_participation ON friendship.child_id = game_participation.child_id
        JOIN game_instance ON game_participation.game_instance_id = game_instance.id
        JOIN game ON game_instance.game_id = game.id

    )
group By 
child.id,
    game_instance.id,
    game.id,
    game_participation.child_id,
    game_participation.game_instance_id,
    friendship.child_id,
    friendship.adult_id
having (
        child.gender = 'male'
        and (
            (count(*) > 2)
            or (
                count(*) <= 2
                and friendship.power = 99
            )
        )
    );