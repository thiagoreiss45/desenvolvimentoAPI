from datetime import datetime, timedelta
from flask import Flask, request, abort
from flask_api import status
import json
#oi
app = Flask(__name__)
lista = []  # Lista para colocar requisicoes


class Requisicao(object):
    """ Classe que possui o conteudo do request(corpo json)
    e a sua hora"""
    def __init__(self, conteudo, hora_do_request):
        self.conteudo = conteudo
        self.hora_do_request = hora_do_request


@app.route('/linx.com/products/', methods=['GET', 'POST', 'DELETE', 'PUT'])
def negar_request_igual_por_10min():
    if request.method == 'POST':

        """ Percorre toda a lista de requisicoes,
        checa se a requisicao nova esta incluida,
        se estiver e nao ter 10 minutos de vida, abort (403) """

        dado = request.get_json(force=True)
        data_agora = datetime.now()
        objeto_requisicao = Requisicao(dado, data_agora)

        for i in range(0, len(lista), 2):
            if lista[i] == objeto_requisicao.conteudo:
                if objeto_requisicao.hora_do_request < lista[i+1] + timedelta(minutes=10):
                    print(dado)
                    print("")
                    return f"{status.HTTP_403_FORBIDDEN} Forbidden\n"
        print(dado)
        print("")
        lista.append(objeto_requisicao.conteudo)
        lista.append(objeto_requisicao.hora_do_request)
        return f"{status.HTTP_201_CREATED} OK\n"


if __name__ == '__main__':
    app.run(debug=True, port=5000)
