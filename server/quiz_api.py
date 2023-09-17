from flask_openapi3 import APIBlueprint, Tag

from model import Session
from model.quiz import Quiz
from model.player import Player
from schema.error_schema import ErrorResponse
from schema.quiz_schema import CreateQuizRequest, GetQuizRequest, QuizListResponse, \
    QuizResponse, quiz_to_output

quiz_tag = Tag(
    name='Quiz', description='Operações relativas ao quiz')

api = APIBlueprint('/player/<int:player_id>/quizzes',
                   __name__, abp_tags=[quiz_tag])


@api.post('/players/<int:player_id>/quizzes',
          responses={'201': QuizResponse, '404': ErrorResponse})
def create_quiz(form: CreateQuizRequest, path: GetQuizRequest):
    db = Session()

    player_id = path.player_id
    player_exists = db.query(Player).get(player_id)
    if not player_exists:
        error_message = 'Jogado com ID "{}" não foi encontrado'.format(player_id)
        return {'message': error_message}, 404

    quiz = Quiz(player_id, form.score)

    db.add(quiz)
    db.commit()

    return quiz_to_output(quiz), 201


@api.delete('/players/<int:player_id>/quizzes/<int:quiz_id>',
            responses={'204': None, '404': ErrorResponse, '422': ErrorResponse})
def remove_quiz(path: GetQuizRequest):
    db = Session()

    player = db.query(Player).get(path.player_id)
    if not player:
        error_message = 'Player não encontrado'
        return {'message': error_message}, 404

    quiz = db.query(Quiz).get(path.quiz_id)
    if not quiz:
        error_message = 'Quiz não encontrado'
        return {'message': error_message}, 404

    db.delete(quiz)
    db.commit()

    return '', 204


@api.get('/players/<int:player_id>/quizzes', responses={'200': QuizListResponse})
def get_quizzes(path: GetQuizRequest):
    db = Session()
    quizzes = db.query(Quiz).filter(Quiz.player_id == path.player_id).all()

    if not quizzes:
        return {'quizzes': []}, 200

    output = list(map(lambda quiz: quiz_to_output(quiz), quizzes))
    db.close()
    return {'quizzes': output}, 200
