import json

from flask import Flask, render_template, request, jsonify
from utils.pesquisas_db import retornar_anos_modelo, retornar_modelos
from utils.plot_graph import plot_unitario, plot_comparatorio
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
    # modelos = modelos_json['modelo']
    return render_template('analiseUnitaria.html', modelos=modelos)


@app.route('/analisar', methods=['POST'])
def analisar():
    marca = 'Fiat'
    modelo = request.form['modelo']
    ano_modelo = request.form['ano_modelo']
    print(f'marca: {marca}, modelo:{modelo}, ano_modelo:{ano_modelo}')
    image_base64, dataFrame, tendencia_porcentagem = plot_unitario(marca, modelo, ano_modelo)
    previsao, preco_final = variacao_media(dataFrame)
    return render_template('analiseDados.html',
                           image_base64=image_base64,
                           previsao=previsao,
                           preco_final=preco_final,
                           tendencia_porcentagem=tendencia_porcentagem)


@app.route('/analisar-comparativo', methods=['POST'])
def analisar_comparativo():
    modelo = []
    modelo.append(request.form['modelo1'])
    modelo.append(request.form['modelo2'])

    ano_modelo = []
    ano_modelo.append(request.form['ano_modelo1'])
    ano_modelo.append(request.form['ano_modelo2'])

    marca = 'Fiat'
    print(f'marca: {marca}, modelo:{modelo}, ano_modelo:{ano_modelo}')
    image_base64, dataFrame1, dataFrame2, tendencia_porcentagem = plot_comparatorio(marca, modelo, ano_modelo)

    previsao_1, preco_final_1 = variacao_media(dataFrame1)
    previsao_2, preco_final_2 = variacao_media(dataFrame2)

    previsao = [previsao_1, previsao_2]
    preco_final = [preco_final_1, preco_final_2]

    return render_template('analiseDadosComparativos.html',
                           image_base64=image_base64,
                           previsao=previsao,
                           preco_final=preco_final,
                           tendencia_porcentagem=tendencia_porcentagem)


@app.route('/analiseComparativa')
def carregar_analise_comparativa():
    modelos_json = retornar_modelos()
    modelos_json = json.loads(modelos_json)
    modelos = [v['modelo'] for v in modelos_json.values()]
    return render_template('analiseComparativa.html', modelos=modelos)


@app.route('/pesquisar_ano_modelo', methods=['GET'])
def pesquisar_ano_modelo():
    modelo_carro = request.args.get('modelo')
    res = retornar_anos_modelo(modelo_carro)
    res = json.loads(res)
    anos_modelo = [v['ano_modelo'] for v in res.values()]

    return jsonify(anos_modelo)


app.run()
