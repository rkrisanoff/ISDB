#!/usr/bin/python
from enum import Enum
import random as rnd
import string
from typing import NamedTuple, Callable


def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(rnd.choice(letters) for i in range(length))

class FieldTypeDefinition(NamedTuple):
    name: str
    """
    name is unique value that detemrnies field in entity
    """
    generate: Callable[['any'], 'any']
    """
    generate - function returning value from domen for this field type
    """
    toSql: Callable[['any'], 'str']
    """
    To Sql - translate python-value to value in SQL
    """
    


class FieldType(FieldTypeDefinition, Enum):
    INTEGER = FieldTypeDefinition(
        name="INTEGER",
        generate=lambda min, max: rnd.randint(min, max),
        toSql=lambda value: str(value)
    )
    VARCHAR = FieldTypeDefinition(
        name="VARCHAR",
        generate=lambda len: randomword(len),
        toSql=lambda value: str("'"+value+"'")
    )
    BOOLEAN = FieldTypeDefinition(
        name="BOOLEAN",
        generate=lambda: rnd.random() > 0.5,
        toSql=lambda value: "TRUE" if value else "NOT"
    )


class Field:
    type: FieldType
    condition: Callable[['any'], 'bool']
    name: str
    isPK: bool
    """
    flag whether the value is a primary key
    """
    mayBeNull: bool
    """
    flag whether the value is a NULL
    """
    FK: dict[str]

    def __init__(self, name: str, type: FieldType, isPK: bool, mayBeNull: bool, condition, FK: dict[str, (str, str)] = dict()) -> None:
        self.type = type
        self.condition = condition
        self.name = name
        self.isPK = isPK
        self.mayBeNull = mayBeNull


class Entity:
    name: str
    fields: dict[str, Field]

    def __init__(self, name, fields: dict[str, Field]) -> None:
        self.name = name
        self.fields = fields


class EntityFactory:
    config: dict[str, str]

    def __init__(self, config) -> None:
        self.config = config

    def transormToSql(self, entityName, values):
        return f"INSERT INTO {self.config['schema']}.{entityName} ({','.join(values.keys())}) VALUES ({','.join(values.values())});\n"

    def generateInsert(self, entity: Entity) -> dict[str, any]:
        values = dict().fromkeys(entity.fields.keys())
        for field in list(entity.fields.values()):
            value = None
            if field.type == FieldType.INTEGER:
                while not (value := field.type.generate(1, 1000)):
                    value = field.type.generate(1, 1000)
            elif field.type == FieldType.VARCHAR:
                value = field.type.generate(30)
            values[field.name] = field.type.toSql(value)
        return values

    def generateInserts(self, entity: Entity, number):
        return [self.generateInsert(entity) for i in range(number)]

    def generateSqls(self, entities: dict[str, Entity]):
        sqls = dict().fromkeys(entities.keys())
        for entityName,entity in entities.items():
            sqls[entityName] = self.generateInserts(entity,10)
        finalRequst = ""
        for entityName,inserts in sqls.items(): 
            for insert in inserts:
                finalRequst += self.transormToSql(entityName,insert)
        return finalRequst


ef = EntityFactory({"schema": "s284712"})
positronic_brain = Entity("positronic_brain",
           {
               "release_series": Field("release_series", FieldType.INTEGER, True, False, lambda val: True, {}),
               "name": Field("name", FieldType.VARCHAR, False, False, lambda val: len(val) <= 255, {}),
               "speed": Field("speed", FieldType.INTEGER, False, False, lambda val: val > 0, {}),
               "cost": Field("cost", FieldType.INTEGER, False, False, lambda val: val > 0, {})
           }
           )
department = Entity("department",
           {
               "id": Field("id", FieldType.INTEGER, True, False, lambda val: True, {}),
               "extracted_bor_quantity": Field("extracted_bor_quantity", FieldType.INTEGER, False, False, lambda val: val >= 0, {}),
               "current_resource": Field("current_resource", FieldType.INTEGER, False, False, lambda val: val >= 0, {})
           }
           )
entities = {
    "positronic_brain":positronic_brain,
    "department":department
}
print(ef.generateSqls(entities))

