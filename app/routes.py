from flask import Blueprint, render_template, request
from utils.fetch_data import buscar_no_google
from utils.intention import pergunta_sobre_furia
import random

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
        if not historico:
            historico.append({
                "resposta": "👋 Bem-vindo ao Oráculo Furioso! Estou aqui para responder tudo o que eu puder sobre nossa seleção brasileira de eSports: a <strong>FURIA</strong>! 🐆"
            })

    elif request.method == 'POST':
        pergunta = request.form.get('pergunta')

        if not pergunta:
            historico.append({
                "pergunta": "",
                "erro": "Digite uma pergunta."
            })

        elif not pergunta_sobre_furia(pergunta):
            historico.append({
                "pergunta": pergunta,
                "erro": "⚠️ Só respondo perguntas sobre o time de CS da FURIA 🐆."
            })

        else:
            resultado = buscar_no_google(pergunta)
            if resultado:
                historico.append({
                    "pergunta": pergunta,
                    "resposta": resultado['resumo'],
                    "link": resultado['link']
                })
            else:
                historico.append({
                    "pergunta": pergunta,
                    "erro": "❌ Não encontrei nada sobre isso. Tente outra pergunta."
                })

    sugestao = random.choice(sugestoes)
    return render_template('index.html', historico=historico, sugestao=sugestao)