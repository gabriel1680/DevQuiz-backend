from flask_openapi3 import APIBlueprint, Tag
from model import Session

from model.player import Player
from schema.error_schema import ErrorResponse
from schema.player_schema import CreatePlayerRequest, GetPlayerRequest,\
    PlayerResponse, UpdatePlayerRequest, player_to_output


player_tag = Tag(
    name='Player', description='Criação e alteração das informações do jogador')
api = APIBlueprint('/players', __name__, abp_tags=[player_tag])


@api.post('/players', responses={'201': PlayerResponse, '400': ErrorResponse})
def create_player(body: CreatePlayerRequest):
    db = Session()

    player = Player(body.username)

    player_exists = db.query(Player).filter(
        Player.username == player.username).first()
    if player_exists:
        error_message = 'O username {} já está em uso'.format(
            player.username)
        return {'message': error_message}, 400

    db.add(player)
    db.commit()

    return player_to_output(player), 201


@api.patch('/players/<int:id>', responses={'204': PlayerResponse, '400': ErrorResponse,
                                           '404': ErrorResponse})
def update_player(body: UpdatePlayerRequest, path: GetPlayerRequest):
    db = Session()

    player = db.query(Player).get(path.id)
    if not player:
        error_message = 'O jogado com o ID "{}" não foi encontrado'.format(
            path.id)
        return {'message': error_message}, 404

    player_exists = db.query(Player).filter(
        Player.username == body.username).first()
    if player_exists:
        error_message = 'O username {} já está em uso'.format(
            player.username)
        return {'message': error_message}, 400

    player.username = body.username
    db.commit()

    return '', 204


@api.get('/players/<int:id>', responses={'200': PlayerResponse, '404': ErrorResponse})
def get_player(path: GetPlayerRequest):
    db = Session()

    player = db.query(Player).get(path.id)

    if not player:
        error_message = 'O jogado com o ID "{}" não foi encontrado'.format(
            path.id)
        return {'message': error_message}, 404

    db.add(player)
    db.commit()

    return player_to_output(player), 200
