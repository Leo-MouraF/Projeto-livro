from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        "id": 1,
        "titulo": "Titulo do livro 1",
        "autor": "Nome do autor",
    },
    {
        "id": 2,
        "titulo": "Titulo do livro 2",
        "autor": "Nome do autor",
    },
    {
        "id": 3,
        "titulo": "Titulo do livro 3",
        "autor": "Nome do autor",
    },
]


# consultar todos
@app.route("/livros", methods=["GET"])
def obter_livros():
    return jsonify(livros)


# consultar por id
@app.route("/livros/<int:livro_id>", methods=["GET"])
def obter_livro_id(livro_id):
    for livro in livros:
        if livro.get("id") == livro_id:
            return jsonify(livro)
    return f"Livro não encontrado. ID inexistente."


# editar
@app.route("/livros/<int:livro_id>", methods=["PUT"])
def editar_livro(livro_id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get("id") == livro_id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
    return f"Ocorreu um erro inesperado!"


# Criar livro
@app.route("/livros", methods=["POST"])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)


# excluir
@app.route("/livros/<int:livro_id>", methods=["DELETE"])
def excluir_livro(livro_id):
    for indice, livro in enumerate(livros):
        if livro.get("id") == livro_id:
            del livros[indice]
            return jsonify(livros)


app.run(port=5000, host="localhost", debug=True)
