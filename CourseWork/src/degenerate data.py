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
    toSql: Callable[['any'], 'str']
    """
    To Sql - translate python-value to value in SQL
    """


NamesDomain = [
    'Harry',
    'Oliver',
    'Jack',
    'Charlie',
    'Thomas',
    'Jacob',
    'Alfie',
    'Riley',
    'William',
    'James'
]
GenderDomain = ['male', 'gender']


class Domain(Enum):
    def GENDER(): return rnd.choice(GenderDomain)
    def NAME(): return rnd.choice(NamesDomain)
    def AGE(): return rnd.randint(18, 60)
    def FLAG(): return rnd.random() >= 0.5
    def INDEX(): return rnd.randint(1, 1000)
    def POSITIVE_INTEGER(): return rnd.randint(0,20000)


class FieldType(FieldTypeDefinition, Enum):
    INTEGER = FieldTypeDefinition(
        name="INTEGER",
        toSql=lambda value: str(value)
    )
    VARCHAR = FieldTypeDefinition(
        name="VARCHAR",
        toSql=lambda value: str("'"+value+"'")
    )
    BOOLEAN = FieldTypeDefinition(
        name="BOOLEAN",
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
    domain: Domain

    def __init__(self, name: str, type: FieldType, domain: Domain, isPK: bool, mayBeNull: bool, condition, FK: dict[str, (str, str)] = dict()) -> None:
        self.type = type
        self.condition = condition
        self.name = name
        self.isPK = isPK
        self.mayBeNull = mayBeNull
        self.domain = domain

    def getRandomValueFromDomain(self):
        return self.domain()


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
            while not (value := field.getRandomValueFromDomain()):
                value = field.getRandomValueFromDomain()
            values[field.name] = field.type.toSql(value)
        return values

    def generateInserts(self, entity: Entity, number):
        return [self.generateInsert(entity) for i in range(number)]

    def generateSqls(self, entities: dict[str, Entity]):
        sqls = dict().fromkeys(entities.keys())
        for entityName, entity in entities.items():
            sqls[entityName] = self.generateInserts(entity, 10)
        finalRequst = ""
        for entityName, inserts in sqls.items():
            for insert in inserts:
                finalRequst += self.transormToSql(entityName, insert)
        return finalRequst


ef = EntityFactory({"schema": "s284712"})
positronic_brain = Entity("positronic_brain",
                          {
                              "release_series":
                              Field("release_series", FieldType.INTEGER,
                                    Domain.INDEX, True, False, lambda val: True, {}),
                              "name":
                              Field("name", FieldType.VARCHAR, Domain.NAME,
                                    False, False, lambda val: len(val) <= 255, {}),
                              "speed":
                              Field("speed", FieldType.INTEGER, Domain.INDEX,
                                    False, False, lambda val: val > 0, {}),
                              "cost":
                              Field("cost", FieldType.INTEGER, Domain.INDEX,
                                    False, False, lambda val: val > 0, {})
                          }
                          )
department = Entity("department",
                    {
                        "id":
                        Field("id", FieldType.INTEGER, Domain.INDEX,
                              True, False, lambda val: True, {}),
                        "extracted_bor_quantity":
                        Field("extracted_bor_quantity", FieldType.INTEGER,
                              Domain.INDEX, False, False, lambda val: val >= 0, {}),
                        "current_resource":
                        Field("current_resource", FieldType.INTEGER,
                              Domain.INDEX, False, False, lambda val: val >= 0, {})
                    }
                    )
entities = {
    "positronic_brain": positronic_brain,
    "department": department
}
print(ef.generateSqls(entities))
