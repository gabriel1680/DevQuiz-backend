from datetime import datetime
from typing import Union

from model.model import Model
from sqlalchemy import Column, DateTime, ForeignKey, Integer


class Quiz(Model):
    """Representa o modelo persistência de um quiz"""

    __tablename__ = 'quizzes'

    id = Column('id', Integer, primary_key=True)
    player_id = Column('player_id', Integer, ForeignKey('players.id'))
    score = Column('score', Integer)
    created_at = Column('created_at', DateTime, default=datetime.now)

    def __init__(self, player_id: int, score: str, created_at: Union[DateTime, None] = None) -> None:
        """
        Cria uma instância de Quiz

        Arguments:
            player_id: id do jogador
            score: pontuação obtida
            created_at: data de criação da quiz
        """
        self.player_id = player_id
        self.title = score

        if created_at:
            self.created_at = created_at
