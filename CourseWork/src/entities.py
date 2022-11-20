from genModel import Entity, FieldType, Domain, Field, ForeignKeyReference


positronic_brain = Entity("positronic_brain",
                          {
                              "release_series":
                              Field(
                                  name="release_series",
                                  type=FieldType.INTEGER,
                                  domain=Domain.INDEX,
                                  isPK=True,
                                  mayBeNull=False,
                                  condition=lambda: True
                              ),
                              "name":
                              Field(
                                  name="name",
                                  type=FieldType.VARCHAR,
                                  domain=Domain.POSITRONIC_BRAIN,
                                  isPK=False,
                                  mayBeNull=False,
                                  condition=lambda val: len(val) <= 255
                              ),
                              "speed":
                              Field(
                                  name="speed",
                                  type=FieldType.INTEGER,
                                  domain=Domain.NATURAL,
                                  isPK=False,
                                  mayBeNull=False,
                                  condition=lambda val: val > 0
                              ),
                              "cost":
                              Field(
                                  name="cost",
                                  type=FieldType.INTEGER,
                                  domain=Domain.NATURAL,
                                  isPK=False,
                                  mayBeNull=False,
                                  condition=lambda val: val > 0
                              )
                          }
                          )
department = Entity("department",
                    {
                        "id":
                        Field(name="id",
                              type=FieldType.INTEGER,
                              domain=Domain.INDEX,
                              isPK=True,
                              mayBeNull=False,
                              condition=lambda: True
                              ),
                        "extracted_bor_quantity":
                        Field(
                            name="extracted_bor_quantity",
                            type=FieldType.INTEGER,
                            domain=Domain.NONEGATIVE_INTEGER,
                            isPK=False, mayBeNull=False,
                            condition=lambda val: val >= 0
                        ),
                        "current_resource":
                        Field(
                            name="current_resource",
                            type=FieldType.INTEGER,
                            domain=Domain.NONEGATIVE_INTEGER,
                            isPK=False,
                            mayBeNull=False,
                            condition=lambda val: val >= 0
                        )
                    }
                    )
robot = Entity("robot",
               {
                   "id":
                   Field(
                       name="id",
                       type=FieldType.INTEGER,
                       domain=Domain.INDEX,
                       isPK=True,
                       mayBeNull=False,
                       condition=lambda: True,
                       FK=None
                   ),
                   "brain_series":
                   Field(
                       name="brain_series",
                       type=FieldType.INTEGER,
                       domain=Domain.INDEX,
                       isPK=False,
                       mayBeNull=False,
                       condition=lambda: True,
                       FK=ForeignKeyReference(
                           "positronic_brain", "release_series")
                   ),
               }
               )
