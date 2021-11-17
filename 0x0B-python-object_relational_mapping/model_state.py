#!/usr/bin/python3
"""lists all cities of argument's state using hbtn_0e_4_usa"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import Integer

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, primary_key=True, unique=True)
    name = Column(String(128), nullable=False)
