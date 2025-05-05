# 🐆 Chatbot da FURIA (Flask)

Este projeto é um chatbot web interativo que responde perguntas sobre o time de CS da FURIA usando Python + Flask + SerpAPI.

> Criado como desafio técnico para a vaga de Estágio em Engenharia de Software na organização FURIA Esports.

---

## 🔥 Funcionalidades

- Interface web interativa (HTML + CSS)
- Busca de informações via [SerpAPI](https://serpapi.com/)
- Filtro inteligente de temas: responde **apenas** perguntas sobre o time de CS da FURIA
- Reconhecimento de erros de digitação (fuzzy match com RapidFuzz)
- Sugestão aleatória de pergunta a cada acesso
- Respostas com links e resumos confiáveis
- Resposta simulada com delay para imitar raciocínio do bot
- Logo da FURIA no fundo + widget da HLTV na interface
- Layout responsivo e estilizado

---

## 🧠 Tecnologias Utilizadas

- Python 3.13.2+
- Flask
- HTML5 / CSS3
- JavaScript
- SerpAPI
- RapidFuzz
- Render (deploy gratuito)

---

## ⚙️ Como Rodar Localmente

```bash
git clone https://github.com/rmgiust/chatbot-furia.git
cd chatbot-furia
python -m venv venv
venv\Scripts\activate  # (Windows)
pip install -r requirements.txt