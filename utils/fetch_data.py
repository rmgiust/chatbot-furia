import requests
from dotenv import load_dotenv
import os

# Carregar as variáveis de ambiente do .env
load_dotenv()
SERPAPI_KEY = os.getenv("SERPAPI_KEY")

def buscar_no_google(pergunta: str) -> dict | None:
    try:
        if not SERPAPI_KEY:
            raise ValueError("API key do SerpAPI não encontrada no .env")

        # Refinando a busca para adicionar a palavra "altura" à consulta
        params = {
            "q": pergunta,  # A busca deve ser direta, sem filtros extras
            "hl": "pt-br",
            "gl": "br",
            "api_key": SERPAPI_KEY,
        }

        # Faz a requisição para o SerpAPI
        response = requests.get("https://serpapi.com/search", params=params)

        # Verificando se a resposta foi bem-sucedida
        if response.status_code != 200:
            print(f"[Erro na requisição SerpAPI]: Status code {response.status_code}")
            return None

        # Processando os dados retornados
        data = response.json()

        # Verificando se há resultados
        resultados = data.get("organic_results", [])
        if not resultados:
            return None

        # Buscando o snippet e link do resultado
        for resultado in resultados:
            link = resultado.get("link", "")
            snippet = resultado.get("snippet", "")

            # Filtro de resultados mais relevantes
            if "altura" in snippet or "cm" in snippet:  # Filtro para resultados com altura ou cm
                return {
                    "resumo": snippet,
                    "link": link
                }

        # Caso não encontre um bom snippet, vamos retornar o primeiro resultado
        if resultados:
            primeiro = resultados[0]
            return {
                "resumo": primeiro.get("snippet", "Informação encontrada, mas sem descrição detalhada."),
                "link": primeiro.get("link", "")
            }

        return None

    except requests.exceptions.RequestException as e:
        print(f"[Erro de requisição]: {e}")
        return None
    except ValueError as e:
        print(f"[Erro de valor]: {e}")
        return None
    except Exception as e:
        print(f"[Erro desconhecido]: {e}")
        return None