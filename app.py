from flask import Flask, request, jsonify, send_from_directory
from pathlib import Path

app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent


def binario_para_decimal(binario):
    """Converte uma string binária para um número decimal."""
    binario = binario.strip()
    if not binario:
        raise ValueError("Digite um número binário.")
    if any(c not in "01" for c in binario):
        raise ValueError("Um número binário pode conter apenas 0 e 1.")
    return int(binario, 2)


def decimal_para_binario(decimal):
    """Converte uma string contendo um inteiro decimal para binário."""
    decimal = decimal.strip()
    if not decimal:
        raise ValueError("Digite um número decimal.")
    try:
        numero = int(decimal)
    except ValueError:
        raise ValueError("Digite um número decimal inteiro válido.")
    if numero < 0:
        raise ValueError("Digite um número decimal maior ou igual a zero.")
    return bin(numero)[2:]


@app.route("/")
def index():
    """Entrega o arquivo index.html."""
    return send_from_directory(BASE_DIR, "index.html")


@app.route("/style.css")
def style():
    """Entrega o arquivo CSS."""
    return send_from_directory(BASE_DIR, "style.css")


@app.route("/script.js")
def script():
    """Entrega o arquivo JavaScript."""
    return send_from_directory(BASE_DIR, "script.js")


@app.route("/converter", methods=["POST"])
def converter():
    """Recebe uma conversão do frontend e retorna o resultado em JSON."""
    dados = request.get_json(silent=True) or {}
    tipo = dados.get("tipo")
    valor = dados.get("valor", "")

    try:
        if tipo == "binario_decimal":
            resultado = binario_para_decimal(valor)
        elif tipo == "decimal_binario":
            resultado = decimal_para_binario(valor)
        else:
            raise ValueError("Tipo de conversão inválido.")

        return jsonify({"sucesso": True, "resultado": str(resultado)})
    except ValueError as erro:
        return jsonify({"sucesso": False, "erro": str(erro)}), 400


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
