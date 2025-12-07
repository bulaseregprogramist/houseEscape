"""Базы данных SQL"""

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class SQLDatabases:
    """
    Класс для работы с базами данных SQL
    (Используется SQLAlchemy)
    """
    
    def __init__(self):
        pass
    
    def create_table(self) -> None:
        """
        """
        pass

