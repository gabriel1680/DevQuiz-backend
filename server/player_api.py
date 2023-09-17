from flask_openapi3 import APIBlueprint, Tag
from model import Session

from model.player import Player
from schema.error_schema import ErrorResponse
from schema.player_schema import CreatePlayerRequest, GetPlayerRequest,\
    PlayerResponse, player_to_output


player_tag = Tag(
    name='Player', description='Criação e alteração das informações do jogador')
api = APIBlueprint('/players', __name__, abp_tags=[player_tag])


@api.post('/players', responses={'201': PlayerResponse, '400': ErrorResponse})
def create_player(form: CreatePlayerRequest):
    db = Session()

    player = Player(form.username)

    player_exists = db.query(Player).filter(
        Player.name == player.name).first()
    if player_exists:
        error_message = 'O username {} já está em uso'.format(
            player.name)
        return {'message': error_message}, 400

    db.add(player)
    db.commit()

    return player_to_output(player), 201
