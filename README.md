# Dependências:

Python 3.6 ou superior:
sudo apt-get install python3.6
pip:
sudo apt-get install python-pip
Bibliotecas:
pip install -r requirements.txt
Curl:
sudo apt-get -y install curl
Git:
sudo apt-get install git

# Executar soluções:
# Solução 1

1. Clonar repositório:
git clone https://github.com/thiagoreiss45/backend-challenge-linx
cd backend-challenge-linx/part-1/src
2. Instalar bibliotecas:
pip install -r requirements.txt
3. Executar apiProdutos.py 
python3 part_1.py
4. Para teste manual executar: 
curl -XPOST http:/127.0.0.1:5000/linx.com/products/ -d '[{"id": "123", "name": "mesa"}]'
5. Para o teste automatizado:
cd backend-challenge-linx/part-1/teste
./testeApi.sh

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
