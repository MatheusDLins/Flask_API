# Flask_API
API flask desenvolvida para gestão de salas de aula
Após acessar o arquivo api.py podemos rodar o comando "python api.py" para deixar a API online.
Essa API foi desenvolvida atravez do VScode e utilizando o Python 3.8.3

Podemos acessar pela url local: http://127.0.0.1:5000/

A API pode gerenciar salas, atualmente as salas estão em um dicionário com outro dicionário dentro que pode ser visto ao acessar o link(http://127.0.0.1:5000/)

<h1>Criando novas Salas</h1>

Podemos cadastrar novas salas usando o seguinte código de exemplo:

criar = requests.post(url, json={"Sala": "Linux", 'data': [2022,6,21], 'tempo': 2})

irá criar uma nova sala com nome "Linux", com a data de início do curso e o tempo que será usada a sala

<h1>Lista de Salas</h1>

Podemos listar as salas entrando na url(http://127.0.0.1:5000/salas)

podemos usar esses dados usando o seguinte comando:
lista = requests.get("http://127.0.0.1:5000/salas")
print(lista.json())

<h1>Busca por nome</h1>

Podemos buscar por determinado nome de sala apenas adicionando o nome ao url:

http://127.0.0.1:5000/busca/Python%20Fundamentals

Lembrando de substituir o espaço por %20, uma maneira de fazer isso seria:

busca_url = ("http://127.0.0.1:5000/busca/")
busca = "Python Fundamentals"
busca_formatada = busca.replace(' ', '%20')
resultado = busca_url+busca_formatada
print(resultado)

<h1>Agendar sala</h1>
Podemos agendar Salas usando o método put e passando na url o número referente a sala que deseja ser agendada

agendando = requests.put("http://127.0.0.1:5000/agendar/2",json={'data':[2022,8,22],'tempo':5})
print(agendando.json())

Aqui estamos agendando a sala 2 para o dia 22/08/2022 por 5 dias e o status dela caso não esteja ocupada ira ser mudado automaticamente asdkasdsad
