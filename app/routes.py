from flask import Blueprint, render_template, request, jsonify
from utils.fetch_data import buscar_no_google  # Importa a função de busca
import random
from utils.intention import pergunta_sobre_furia  # Importando o filtro para perguntas sobre a FURIA

main = Blueprint('main', __name__)
historico = []

# Sugestões aleatórias para dica de uso
sugestoes = [
    "Quem é o coach da FURIA?",
    "Quando a FURIA foi fundada?",
    "Quem é o melhor jogador da FURIA?",
    "A FURIA está no próximo Major?",
    "Quantos títulos a FURIA tem?"
]

@main.route('/', methods=['GET', 'POST'])
def index():
    global historico

    if request.method == 'GET':
        historico.clear()  # Limpa tudo ao acessar a página
        historico.append({
            "resposta": "👋 Bem-vindo ao Oráculo Furioso! Estou aqui para responder tudo o que eu puder sobre nossa seleção brasileira de eSports: a <strong>FURIA</strong>! 🐆"
        })

    elif request.method == 'POST':
        pergunta = request.form.get('pergunta')
        resposta = {}

        if not pergunta:
            resposta['erro'] = "Digite uma pergunta."
        elif not pergunta_sobre_furia(pergunta):  # Filtra perguntas fora do contexto
            resposta['erro'] = "❌ Pergunta fora do contexto da FURIA. Tente algo relacionado ao time de CS da FURIA."
        else:
            # Chama a função de busca e pega o resumo e link
            resultado = buscar_no_google(pergunta)
            if resultado:
                resposta['resumo'] = resultado.get('resumo')
                resposta['link'] = resultado.get('link')
            else:
                resposta['erro'] = "❌ Não encontrei nada sobre isso. Tente outra pergunta."

        return jsonify(resposta)  # Retorna a resposta em JSON para o frontend

    sugestao = random.choice(sugestoes)
    return render_template('index.html', historico=historico, sugestao=sugestoes)
