import json

from flask import Flask, render_template, request, jsonify
from utils.pesquisas_db import retornar_anos_modelo, retornar_modelos
from utils.plot_graph import plot_unitario
from math_model.variacao_media import variacao_media

app = Flask(__name__)


@app.route('/menu', methods=["POST"])
def carregar_index():
    return render_template('index.html')


@app.route('/')
def carregar_login():
    return render_template('login.html')


@app.route('/cadastro')
def carregar_cadastro():
    return render_template('cadastro.html')


@app.route('/analiseUnitaria')
def carregar_analise_unitaria():
    modelos_json = retornar_modelos()
    modelos_json = json.loads(modelos_json)
    modelos = [v['modelo'] for v in modelos_json.values()]
    #modelos = modelos_json['modelo']
    return render_template('analiseUnitaria.html', modelos=modelos)


@app.route('/analisar', methods=['POST'])
def analisar():
    marca = 'Fiat'
    modelo = request.form['modelo']
    ano_modelo = request.form['ano_modelo']
    print(f'marca: {marca}, modelo:{modelo}, ano_modelo:{ano_modelo}')
    image_base64, dataFrame = plot_unitario(marca, modelo, ano_modelo)
    variacao_media(dataFrame)
    return render_template('analiseDados.html', image_base64=image_base64)


@app.route('/analiseComparativa')
def carregar_analise_comparativa():
    return render_template('analiseComparativa.html')



@app.route('/pesquisar_ano_modelo', methods=['GET'])
def pesquisar_ano_modelo():
    modelo_carro = request.args.get('modelo')
    res = retornar_anos_modelo(modelo_carro)
    res = json.loads(res)
    anos_modelo = [v['ano_modelo'] for v in res.values()]

    return jsonify(anos_modelo)


app.run()
