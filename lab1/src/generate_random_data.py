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
    ["John", "Ivan", "Gans", "Li", "Spartak", "Nikita"],
    ["Anna", "Kate", "Nastya", "Ekaterina", "Youlya", "Maria"]
]

games = [
    ("Hiding games", True),
    ("Chinese whispers", False)
]
GAMES_NAME = 0
GAMES_COMPENTITIVE = 1
game_instances = list(range(10))

questions = [
    "WHO I AM?","WHERE I AM?","FOR WHAR I AM?","WHY I AM SO UNHAPPY?","HOW ADULTS HAVE GROWN OUT OF THESE WONDERFUL CREATURES?"
]
records = {
    "CHILD": [],
    "ADULT": [],
    "GAME": [],
    "GAME_INSTANCE": [],
    "GAME_PARTICIPATION": [],
    "GAME_WATCHING": [],
    "FRIENDSHIP": [],
    "QUESTION": []
}
for i in range(len(names[0])):
    gender = rnd.randint(0, 1)
    name = names[gender][rnd.randint(0, len(names[gender]))-1]
    age = rnd.randint(0, 18)
    records["CHILD"].append(insertCommand(
        table="CHILD", id=i, name=name, age=age, gender=bool(gender)))

for index in range(len(names[0])):
    gender = rnd.randint(0, 1)
    name = names[gender][rnd.randint(0, len(names[gender]))-1]
    age = rnd.randint(18, 50)
    is_accept_as_friend = rnd.randint(0, 1)
    records["ADULT"].append(insertCommand(
        table="ADULT", id=index, name=name, age=age, gender=bool(gender)))

for index, (name, is_competitive) in enumerate(games):
    records["GAME"].append(insertCommand(
        table="GAME", id=index, name=name, is_competitive=is_competitive))


for i in game_instances:
    game = rnd.randint(0, len(games)-1)
    records["GAME_INSTANCE"].append(insertCommand(
        table="GAME_INSTANCE",
        id=i,
        game_id=rnd.randint(0,len(games)-1),
        won_child_id=rnd.randint(
            0, len(names[0])-1) if games[game][GAMES_COMPENTITIVE] else "NULL"
    ))
for i in range(10):
    game = rnd.randint(0, len(games)-1)
    records["GAME_PARTICIPATION"].append(insertCommand(
        table="GAME_PARTICIPATION",
        child_id=rnd.randint(0, len(names)-1),
        game_instance_id=rnd.randint(0, len(game_instances)-1)
    ))
for i in range(10):
    game = rnd.randint(0, len(games)-1)
    records["GAME_WATCHING"].append(insertCommand(
        table="GAME_WATCHING",
        adult_id=rnd.randint(0, len(names)-1),
        game_instance_id=rnd.randint(0, len(game_instances)-1)
    ))

for i in range(10):
    records["FRIENDSHIP"].append(insertCommand(
        table="FRIENDSHIP",
        child_id=rnd.randint(0, len(names[0])-1),
        adult_id=rnd.randint(0, len(names[0])-1),
        power=rnd.randint(0,100)
    ))

for i in range(5):
    records["QUESTION"].append(insertCommand(
        table="QUESTION",
        adult_id=rnd.randint(0, len(names[0])-1),
        content=questions[rnd.randint(0,len(questions)-1)],
        priority=rnd.randint(0,100)
    ))


print("".join(["".join(record) for record in list(records.values())]))
