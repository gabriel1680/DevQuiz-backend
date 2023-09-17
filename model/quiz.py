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
    answered_at = Column('answered_at', DateTime, default=datetime.now)

    def __init__(self, player_id: int, score: str, answered_at: Union[DateTime, None] = None) -> None:
        """
        Cria uma instância de Quiz

        Arguments:
            player_id: id do jogador
            score: pontuação obtida
            answered_at: data em que o quiz foi respondido
        """
        self.player_id = player_id
        self.score = score

        if answered_at:
            self.answered_at = answered_at
