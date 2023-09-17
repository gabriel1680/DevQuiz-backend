from flask_openapi3 import OpenAPI, Info
from flask_cors import CORS

from server.player_api import api as player_api
from server.quiz_api import api as quiz_api
from server.doc_api import api as doc_api

info = Info(title='DevQuiz API', version='0.0.1',
            description='DevQuiz API é uma API REST para o jogo quiz de perguntas e respostas')
app = OpenAPI(__name__, info=info)

app.register_api(doc_api)
app.register_api(player_api)
app.register_api(quiz_api)

CORS(app)

