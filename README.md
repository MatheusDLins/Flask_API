# Flask_API
API flask desenvolvida para gestão de salas de aula
O arquivo requiriments.txt encontra-se no código
Após acessar o arquivo api.py podemos rodar o comando "python api.py" para deixar a API online.
Essa API foi desenvolvida atravez do VScode em um ambiente virtual e utilizando o Python 3.8.3
Lembre de importa o requests no inicio de qualquer exemplo

Podemos acessar pela url local: http://127.0.0.1:5000/

A API pode gerenciar salas, atualmente as salas estão em um dicionário com outro dicionário dentro que pode ser visto ao acessar o link(http://127.0.0.1:5000/)

<h1>Criando novas Salas</h1>

Podemos cadastrar novas salas usando o seguinte código de exemplo:

url = ('http://127.0.0.1:5000')
criar = requests.post(url, json={"Sala": "Linux"})

irá criar uma nova sala com nome "Linux", com a data de início e fim zeradas que posteriormente podem ser agendadas.
<h1>Lista de Salas</h1>

Podemos listar as salas entrando na url(http://127.0.0.1:5000/salas)

podemos usar esses dados usando o seguinte comando na IDE:

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
Podemos agendar Salas usando o método put e passando na url /agendar/ e o número referente a sala que deseja ser agendada

agendando = requests.put("http://127.0.0.1:5000/agendar/2",json={"data_inicio":[2022,6,24],"data_final":[2022,7,28]})
print(agendando.json())

Aqui estamos agendando a sala 2 para o dia 24/06/2022 até 28/07/2022, e seu estatos muda automaticamente para ocupado = True

Lembre que nenhuma sala já agendada pode ser agendada sem que já tenha acabado o agendamento, o programa ao inicializar percorre a lista de salas para verificar se alguma sala já foi desocupada e zerando as datas da mesma e colocando o status de ocupado = False
