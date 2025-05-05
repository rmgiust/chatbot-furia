from rapidfuzz import fuzz

PALAVRAS_CHAVE = [
    "furia","fúria", "cs", "cs2", "csgo", "counter strike", "jogadores", "coach", "treinador", "técnico",
    "hltv", "ranking", "torneio", "campeonato", "partida", "lineup", "elenco", "equipe",
    "esports", "história", "títulos", "conquistas",
    "fallen", "gabriel toledo", "kscerato", "kaike cerato", "yuurih", "yuri boian", "chelo", "marcelo cespedes",
    "art", "andrei piovezan", "drop", "andre abreu", "guerri", "nicholas nogueira",
    "iem", "blast", "major", "esl", "dreamhack", "pgl", "qualificatória", "playoffs", "fase de grupos",
    "parceria", "adidas", "uniforme", "merch", "loja oficial", "red bull", "patrocinador"
]

PALAVRAS_PROIBIDAS = [
    "lula", "bolsonaro", "dilma", "pt", "psdb", "presidente", "eleição", "política", "congresso",
    "senado", "governo", "ministerio", "planalto", "palácio", "bolsonarismo", "lulismo"
]

def pergunta_sobre_furia(pergunta: str) -> bool:
    if not pergunta:
        return False

    pergunta = pergunta.lower()

    # ❌ Verifica se contém palavras proibidas
    for proibida in PALAVRAS_PROIBIDAS:
        if proibida in pergunta:
            return False

    palavras_usuario = pergunta.split()

    for termo in PALAVRAS_CHAVE:
        for palavra in palavras_usuario:
            if fuzz.ratio(palavra, termo) > 80:
                return True

    return False
