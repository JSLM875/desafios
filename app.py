from flask import Flask, jsonify, request

app = Flask (__name__)

usuarios = [
{
    'id': 1,
    'nome': 'boba fett',
    'idade': 41

},
{
    'id': 2,
    'nome': 'anakin skywalker',
    'idade': 35
},
{
    'id': 3
    'nome': 'flavin do pneu',   
    'idade': 30
}.

@app.route('/usarios' methods=['GET'])
def consultar_usuarios ():
    return jsonify (usuarios)

@app.route('/usarios/<int:id>', methods=['GET'])
def consultar_usuarios_por_id (id):
    for usuario in usuarios:
      if usuario.get ('id') == id:
         return jsonify (usuarios)    

@app.route('/usarios', methods=['POST'])
def cadastrar_usuarios ():
    novo_usuario = request.get_json()
    usuarios.append (novo_usuario)
    return jsonify (usuarios)

@app.route('/usarios/<int:id>',methods=['PUT'])
def atualizar_por_id (id):
    usuario_atualizado = request.get_json()
    for indice,usuario in enumerate(usuarios):
        if usuario.get('id') == id: 
           usuarios[indice].update(usuario_atualizado)
           return jsonify(usuarios[indice])   

@app.route('/usarios/<int:id>', methods=['DELETE'])
def excluir_usuario_por_id(id):
    for indice,usuario in enumerate(usuarios):
        if usuario.get('id') == id:
         del usuarios[indice]
         return jsonify (usuarios)   

    app.run(port=8000,host='localhost' ,debug=true) 

