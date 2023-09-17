from flask_openapi3.models.common import Field
from pydantic import BaseModel

from model.player import Player
from schema.quiz_schema import QuizResponse, quiz_to_output


class CreatePlayerRequest(BaseModel):
    """Definição do objeto da requisição de criação 
    de um novo player"""

    username: str = Field(..., description='Nome do jogador',
                          example='spiderman01')


class GetPlayerRequest(BaseModel):
    """Definição da busca por informações do jogador"""

    id: int = 1


class PlayerResponse(BaseModel):
    """Definição da resposta de criação ou busca de um jogador"""

    id: int = 1
    username: str = 'dark_knight004'


def player_to_output(player: Player) -> dict:
    """Mapeia o modelo de player para a visualização do cliente
    """

    return {
        "id": player.id,
        "username": player.username,
    }
