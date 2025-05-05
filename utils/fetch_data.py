import requests
import os
from dotenv import load_dotenv

load_dotenv()
SERPAPI_KEY = os.getenv("SERPAPI_KEY")

def buscar_no_google(pergunta: str) -> dict | None:
    try:
        if not SERPAPI_KEY:
            raise ValueError("API key do SerpAPI não encontrada no .env")

        params = {
            "q": pergunta,
            "hl": "pt-br",
            "gl": "br",
            "api_key": SERPAPI_KEY,
        }

        response = requests.get("https://serpapi.com/search", params=params)
        data = response.json()

        resultados = data.get("organic_results", [])
        if not resultados:
            return None

        for resultado in resultados:
            link = resultado.get("link", "")
            snippet = resultado.get("snippet", "")

            # Ignora redes sociais e resultados fracos
            if any(site in link for site in ["facebook", "instagram", "twitter", "tiktok", "linkedin", "pinterest"]):
                continue

            if snippet and len(snippet) > 80:
                return {
                    "resumo": snippet,
                    "link": link
                }

        # Fallback: retorna primeiro resultado mesmo que o snippet seja curto
        if resultados:
            primeiro = resultados[0]
            return {
                "resumo": primeiro.get("snippet", "Informação encontrada, mas sem descrição detalhada."),
                "link": primeiro.get("link", "")
            }

        return None

    except Exception as e:
        print(f"[Erro na busca SerpAPI]: {e}")
        return None