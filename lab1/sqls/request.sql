SELECT name
FROM s284712.game
WHERE (
        s284712.game.id in (
            select game_id
            from s284712.game_instance
            WHERE s284712.game_instance.id in (
                    select game_instance_id
                    from s284712.GAME_PARTICIPATION
                    where child_id in (
                            select id as child_id
                            from s284712.child
                            where age = (
                                    select min(age)
                                    from (
                                            select child_id,
                                                name,
                                                age
                                            from (
                                                    select id as child_id,
                                                        name,
                                                        age,
                                                        count(*) as count_of_friends
                                                    from s284712.child
                                                        right join s284712.friendship on s284712.child.id = s284712.friendship.child_id
                                                    group by id
                                                    order by id
                                                ) as child_friendship_describe
                                            where (
                                                    (child_friendship_describe.count_of_friends > 2)
                                                    or (
                                                        child_friendship_describe.count_of_friends <= 2
                                                        and child_friendship_describe.child_id in (
                                                            select child_id
                                                            from s284712.friendship
                                                            where s284712.friendship.power = 99
                                                        )
                                                    )
                                                )
                                        ) as child_conditions
                                )
                    )
            )
        )
);
-- select id as child_id,
--     name,
--     age,
--     count(*) as count_of_friends,
--     max(power) as has_99_friendship_power
-- from s284712.child
--     right join s284712.friendship on s284712.child.id = s284712.friendship.child_id
-- group by id
-- order by id;