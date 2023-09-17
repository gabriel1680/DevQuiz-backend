from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship

from model.model import Model
from typing import Union
from datetime import datetime


class Player(Model):
    """Representa o modelo persistência de uma player"""

    __tablename__ = 'players'

    id = Column('id', Integer, primary_key=True)
    username = Column('name', String(255))
    created_at = Column('created_at', DateTime, default=datetime.now)

    quizzes = relationship('Quiz', backref='player')

    def __init__(self, username: str, created_at: Union[DateTime, None] = None) -> None:
        """
        Cria uma instância de Player

        Arguments:
            username: nome do jogador
            created_at: data de criação do quiz
        """
        self.username = username

        if created_at:
            self.created_at = created_at
