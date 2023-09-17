from typing import List

from sqlalchemy import Enum
from flask_openapi3.models.common import Field
from pydantic import BaseModel

from model.quiz import Quiz


class CreateQuizRequest(BaseModel):
    """Definição do objeto da requisição de criação 
    de um novo quiz"""

    score: int = Field(..., description='Pontuação obtida', example=12)


class QuizResponse(BaseModel):
    """Definição da resposta de criação ou busca de um quiz"""

    id: int = 1
    player_id: int = 1
    score: int = 12


class QuizListResponse(BaseModel):
    """Definição da resposta de listagem de quizzes"""

    quizzes: List[QuizResponse]


class GetQuizRequest(BaseModel):
    """Definição da busca de uma quiz"""

    player_id: int = Field(...,
                           description='Id da player que a quiz pertence', example=1)
    quiz_id: int = Field(..., description='Id da quiz', example=1)


class GetQuizzesRequest(BaseModel):
    """Definição da busca de quizzes de um jogador"""

    player_id: int = Field(...,
                           description='Id do jogador a quem o quiz pertence', example=1)


def quiz_to_output(quiz: Quiz) -> dict:
    """Mapeia o modelo de quiz para a visualização do cliente
    """
    return {
        'id': quiz.id,
        'player_id': quiz.player_id,
        'score': quiz.score,
    }
