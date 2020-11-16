# Dependências:

Python 3.6 ou superior:<br/>
```
sudo apt-get install python3.6
pip:
sudo apt-get install python-pip
```
Bibliotecas:<br/>
```
pip install -r requirements.txt
```
Curl:<br/>
```
sudo apt-get -y install 
```
Git:<br/>
```
sudo apt-get install git
```

# Executar soluções:
# Solução 1

1. Clonar repositório:<br/>
```
git clone https://github.com/thiagoreiss45/backend-challenge-linx 
cd backend-challenge-linx/part-1/src
```
2. Instalar bibliotecas:<br/>
```
pip install -r requirements.txt
```
3. Executar apiProdutos.py <br/>
```
python3 apiProdutos.py
```
4. Para teste manual executar: <br/>
```
curl -XPOST http:/127.0.0.1:5000/linx.com/products/ -d '[{"id": "123", "name": "mesa"}]'
```
5. Para o teste automatizado:<br/>
```
cd backend-challenge-linx/part-1/teste
./testeApi.sh
```
# Solução 2

1. Executar o programa:<br/>
```
cd backend-challenge-linx/part-2/src
python3 agregador-url.py
```

2. Digitar o arquivo, no caso:<br/>
```
input-dump
```

# Teste da API de produtos

O script testeApi.sh fará requisições a cada segundo, a primeira será com 'id' = 0, e continuará até 'id' = 599, para totalizar 10 minutos (ou mais). Além disso, o script fará requisições com 'id' = 0 a cada 10 requisições, para testar se está bloqueando (lançar 403 Forbidden). Notar que após 10 minutos, não haverá 403 Forbidden, pois a requisição id=0 está liberada.

# Teste agregador de URLs

Para testar o programa, eu utilizei o dump fornecido, input-dump, e basta fornecê-lo como entrada do programa e o programa criará outro arquivo, dump-final, que estará com o mínimo de requests necessárias.
