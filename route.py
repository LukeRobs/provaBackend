from flask import Flask ,app , request
from flask.json import jsonify
import json

app = Flask(__name__)

LivroReceitas = [
    {
        "Título": "Bolo01",
        "Lista de ingredientes": [
            "ingrediente01"
            "ingrediente02"
            "ingrediente03"
        ],

        "modo": "modo01",
        "Redimento": "Redimento01"
        
    },
   
]

#cadastrar
@app.route("/cadastrar", methods=["POST","GET"])
def Cadastro():
    if request.method == "GET":
        return jsonify(LivroReceitas)
    elif request.method == "POST":
        newcadastro = json.loads(request.data)
        LivroReceitas.append(newcadastro)
        return jsonify({
            "menssagem" : "Cadastrado",
            "newValue": newcadastro

        }) 
   
@app.route('/cadastrar/<int:indice>', methods=['GET', 'PUT', 'DELETE'])
def cadastroID(indice):
    try:
        LivroReceitas[indice]
    except IndexError:
        message = 'Receita ID {} Não Encontrada'.format(indice)
        return jsonify({
            "message": message,
            "status": "Error!"
        })
    except:
        message = 'Aconteceu um erro inesperado'
        return jsonify({
            "message": message,
            "status": "Error!"
        })
    
    if request.method == 'GET':
        return LivroReceitas[indice]

    elif request.method == 'PUT':
       
        newValue = json.loads(request.data)

        LivroReceitas[indice] = newValue
        return jsonify({
            "message": "Updated!",
            "newValue": newValue
        })
    elif request.method == 'DELETE':
        print(indice)
        LivroReceitas.pop(indice)
        return jsonify({
            "message": "Deleted!",
            "arrayAtual": LivroReceitas
        })


if __name__ == '__main__':
    app.run(debug=True)

  



