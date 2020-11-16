# Dependências:

Flask 1.1.1: pip install FLask

# Executar soluções:
# Solução 1
Para solução 1, deve-se executar o apiProdutos.py, e fazer requisições com o curl, exemplo:

Terminal 1: 
$ python apiProdutos.py

Terminal 2: 
$ curl -X POST -H 'Content-Type: application/json' http://127.0.0.1:5000/api/echo-json -d '[{"id": "123", "name": "mesa"}]'

Ou executar o testeApi.sh, que fará requisições automáticas:

Terminal 2: 
$ ./testeApi.sh

# Solução 2

Deve-se executar agregador-url.py e informar o nome do arquivo que será transformado em um dump melhorado, exemplo:

Terminal:
$ python agregador-url.py

Digite o nome do arquivo de dump: 'input-dump'
ARQUIVO CRIADO COM SUCESSO !

# Teste da API de produtos

O script testeApi.sh fará requisições a cada segundo, a primeira será com 'id' = 0, e continuará até 'id' = 599, para totalizar 10 minutos (ou mais). Além disso, o script fará requisições com 'id' = 0 a cada 10 segundos, para testar se está bloqueando (lançar 403 Forbidden). Notar que após 10 minutos, a requisição com 'id' = 0 será permitida (200).

# Teste agregador de URLs

Para testar o programa, eu utilizei o dump fornecido, input-dump, e basta fornecê-lo como entrada do programa e o programa criará outro arquivo, dump-final, que estará com o mínimo de requests necessárias.
