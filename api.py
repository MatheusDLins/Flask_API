from flask import Flask, request
import datetime

app = Flask(__name__)

#Exibir utf-8 sem quebrar os caracters
app.config['JSON_AS_ASCII'] = False

#data atual
datah=datetime.datetime.now()
data_hoje = [datah.year, datah.month, datah.day]

sala_data = {
    1:{
        'id':1,
        'Sala': "Python Fundamentals",
        "data_inicio": [2022,5,21],
        "data_final":[2022,5,28],
        "ocupado": True
    },
    2: {
        'id':2,
        "Sala": "Python for API and Devops Integration",
        "data_inicio": [2022,4,21],
        "data_final":[2022,5,20],
        "ocupado": True
    }
}




def response_sala():
    return {"salas": list(sala_data.values())}

#atualizacao
#verificar data dos cursos
def atualizar():
    for i in sala_data:
        data_teste1 = {x:sala_data[x]['data_inicio'] for x in range (1, len(sala_data)+1)}
        data_ini = data_teste1[i]

        data_teste2 = {x:sala_data[x]['data_final'] for x in range (1, len(sala_data)+1)}
        data_fim = data_teste2[i]


        ocupado = {x:sala_data[x]['ocupado'] for x in range (1, len(sala_data)+1)}
        if data_hoje > data_ini and data_hoje > data_fim:

            if i in sala_data:
                sala_data[i]["data_inicio"] = [0000,0,00]
                sala_data[i]["data_final"] = [0000,0,00]
                sala_data[i]["ocupado"] = False
    return response_sala()

atualizar()

#rota inicial
@app.route("/")
def list_sala():
    return response_sala()


    


#Cadastrar uma nova sala de aula
@app.route("/", methods=["POST"])
def create_sala():
    body = request.json

    #pegando todos os ids existentes
    ids = list(sala_data.keys())

    if ids:
        new_id = ids[-1] + 1
    else:
        new_id = 1

    sala_data[new_id] = {
        'id': new_id,
        'Sala': body["Sala"],
        'data_inicio': [0000,0,00],
        'data_final': [0000,0,00],
        'ocupado': False


    }
    return response_sala()

#deletar sala
@app.route("//<int:sala_id>",methods=["DELETE"])
def delete(sala_id: int):
    sala = sala_data.get(sala_id)

    if sala:
        del sala_data[sala_id]

    return response_sala()


#editar sala
@app.route("//<int:sala_id>",methods=["PUT"])
def update(sala_id:int):
    body = request.json
    sala = body.get("Sala")
    #data_inicio = body.get("data_inicio")
    #data_final = body.get("data_final")
    #ocupado = body.get("ocupado")

    if sala_id in sala_data:
        sala_data[sala_id]["Sala"] = sala
        #sala_data[sala_id]["data_inicio"] = data_inicio
        #sala_data[sala_id]["data_final"] = data_final
        #sala_data[sala_id]["ocupado"] = ocupado

    return response_sala()

#lista de salas
@app.route('/salas')
def listar_salas():
    lista_de_salas = {x:sala_data[x]['Sala'] for x in range (1, len(sala_data)+1)}
    return lista_de_salas

#busca de salas
@app.route("/busca/<nome>")
def busca_salas(nome):
    lista_de_salas = {x:sala_data[x]['Sala'] for x in range (1, len(sala_data)+1)}
    for i in lista_de_salas:
        if lista_de_salas[i] == nome:
            return(sala_data[i])
            break

#agendamento
@app.route("/agendar/<int:sala_id>",methods=["PUT"])
def agendamento(sala_id:int):    

    #verificando se a sala está ocupada
    lista_de_ocupados = {x:sala_data[x]['ocupado'] for x in range (1, len(sala_data)+1)}

    if lista_de_ocupados[sala_id] == False:
        lista_de_ocupados[sala_id] = True
        body = request.json
        data_inicio = body.get("data_inicio")
        data_final = body.get("data_final")
        ocupado = body.get("ocupado")

        if sala_id in sala_data:
            sala_data[sala_id]["data_inicio"] = data_inicio
            sala_data[sala_id]["data_final"] = data_final
            sala_data[sala_id]["ocupado"] = True

    else:
        print("erro")
    return response_sala()   

app.run(debug=True)