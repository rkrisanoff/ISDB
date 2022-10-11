#!/usr/bin/python


import random as rnd

schema = "s284712"


def insertCommand(table, **kwargs):
    keys = list(kwargs.keys())
    values = list(kwargs.values())
    values = [f"'{i}'" if isinstance(
        i, str) and i != "NULL" else str(i) for i in values]
    return f"INSERT INTO {schema}.{table} ({','.join(keys)}) VALUES ({','.join(values)});\n"


names = [
    ["John", "Ivan", "Gans", "Li","Spartak","Nikita"],
    ["Anna", "Kate", "Nastya", "Ekaterina","Youlya","Maria"]
    ]
games = [
    ("Hiding games", True),
    ("Chinese whispers", False)
]
records = {
    "E_CHILD": [],
    "E_ADULT": [],
    "E_GAME": [],
    "E_GAME_INSTANCE": [],
    "E_GAME_PARTICIPATION": [],
    "E_GAME_WATCHING": [],
    "E_FRIENDSHIP": []
}
for i in range(len(names[0])):
    gender = rnd.randint(0, 1)
    name = names[gender][rnd.randint(0, len(names[gender]))-1]
    age = rnd.randint(0, 18)
    records["E_CHILD"].append(insertCommand(
        table="E_CHILD", id=i, name=name, age=age, gender=bool(gender)))

for i in range(len(names[0])):
    gender = rnd.randint(0, 1)
    name = names[gender][rnd.randint(0, len(names[gender]))-1]
    age = rnd.randint(18, 50)
    is_accept_as_friend=rnd.randint(0, 1)
    records["E_ADULT"].append(insertCommand(
        table="E_ADULT", id=i, name=name, age=age, gender=bool(gender)))

for name, is_competitive in games:
    records["E_GAME"].append(insertCommand(
        table="E_GAME", name=name, is_competitive=is_competitive))
game_instances = list(range(10))
for i in game_instances:
    game = rnd.randint(0, len(games)-1)
    records["E_GAME_INSTANCE"].append(insertCommand(
        table="E_GAME_INSTANCE",
        id=i,
        name_of_the_game=games[game][0],
        won_child_id=rnd.randint(
            0, len(names[0])-1) if games[game][1] else "NULL"
    ))
for i in range(10):
    game = rnd.randint(0, len(games)-1)
    records["E_GAME_PARTICIPATION"].append(insertCommand(
        table="E_GAME_PARTICIPATION",
        child_id=rnd.randint(0, len(names)-1),
        game_instance_id=rnd.randint(0, len(game_instances)-1)
    ))
for i in range(10):
    game = rnd.randint(0, len(games))
    records["E_GAME_WATCHING"].append(insertCommand(
        table="E_GAME_WATCHING",
        adult_id=rnd.randint(0, len(names)-1),
        game_instance_id=rnd.randint(0, len(game_instances)-1)
    ))

for i in range(10):
    records["E_FRIENDSHIP"].append(insertCommand(
        table="E_FRIENDSHIP",
        child_id=rnd.randint(0, len(names[0])-1),
        adult_id=rnd.randint(0, len(names[0])-1)
    ))


print("".join(["".join(record) for record in list(records.values())]))
