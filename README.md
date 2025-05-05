# 🐆 Chatbot da FURIA (Flask)

Este projeto é um chatbot web interativo que responde perguntas sobre o time de CS da FURIA usando Python + Flask + SerpAPI.

> Criado como desafio técnico para a vaga de Estágio em Engenharia de Software na organização FURIA Esports.

---

## 🔥 Funcionalidades

- Interface web interativa (HTML + CSS)
- Busca de informações via [SerpAPI](https://serpapi.com/)
- Filtro inteligente de temas: responde **apenas** perguntas sobre o time de CS da FURIA
- Sistema de sugestão de perguntas
- Respostas com links e resumos confiáveis
- Verificação de similaridade com `RapidFuzz`
- Interface responsiva e visual personalizado
- 🧠 Delay simulado para imitar raciocínio do bot

---

## 🧠 Tecnologias Utilizadas

- Python 3.11+
- Flask
- HTML5 / CSS3
- SerpAPI
- RapidFuzz
- Render (deploy gratuito)

---

## ⚙️ Como Rodar Localmente

```bash
git clone https://github.com/seu-usuario/chatbot-furia.git
cd chatbot-furia
python -m venv venv
source venv/bin/activate  # ou .\venv\Scripts\activate no Windows
pip install -r requirements.txt