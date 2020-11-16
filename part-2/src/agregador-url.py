import json

def agregar_url(numero_de_links_por_request):

    """ O algoritmo vai checando se o ID da proxima request e igual a atual,
     e coloca seu link em uma lista, depois e colocada em data_txt,
     isso e feito 'numero_de_links_por_request' vezes por ID"""

    input_inicial = open(input('Digite o nome do arquivo para ser melhorado: '))
    data = input_inicial.readlines()
    # Transformei para json para poder trabalhar melhor com as colunas (indices)
    data_json = [json.loads(line) for line in data]
    # Ordena em ordem alfabetica os ids
    data_json = sorted(data_json, key=lambda indice: indice['productId'])
    data_txt = []
    indice = 0
    while indice < len(data_json):
        lista = []
        #  Fiz um algoritmo flexivel com o numero de links por request
        numero_inicial_link = numero_de_links_por_request
        inicial = indice
        lista.append(data_json[indice]['image'])

        while numero_de_links_por_request > 1:
            if indice != len(data_json)-1:
                if data_json[indice]['productId'] == data_json[indice+1]['productId']:
                    lista.append(data_json[indice+1]['image'])
                    indice += 1
                else:
                    break
            numero_de_links_por_request -= 1
        data_txt.append({"productId": data_json[inicial]['productId'], "image": lista})
        indice += 1
        numero_de_links_por_request = numero_inicial_link

    return data_txt

DATA_TXT = eval(json.dumps(agregar_url(3)))
with open('dump-final', 'w') as f:
    for element in DATA_TXT:
        print(element, file=f)
print ("ARQUIVO CRIADO COM SUCESSO !")
