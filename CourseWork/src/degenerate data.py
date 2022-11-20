#!/usr/bin/python

from genModel import EntityFactory
import entities

ef = EntityFactory({"schema": "s284712"})

entities = {
    "positronic_brain": entities.positronic_brain,
    "department": entities.department,
    "robot": entities.robot
}
numbers = {
    "positronic_brain": 5,
    "department": 5,
    "robot": 15
}
print(ef.generateSqlRequests(entities,numbers))
