#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

"""Define declarative base"""
Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

"""Establish connection to MySQL server"""
engine = create_engine('mysql://username:password@localhost:3306/database_name')

"""Create all the tables"""
Base.metadata.create_all(engine)

"""Bind a sessionmaker"""
Session = sessionmaker(bind=engine)
session = Session()

