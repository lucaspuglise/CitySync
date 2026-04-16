import random

# Em um cenário real, esses dados viriam de APIs (Google Maps, OpenWeather)
locais = [
    {"nome": "Smart Gym Center", "tipo": "Academia", "lotacao": 25, "distancia": 8},
    {"nome": "Café Tech Hub", "tipo": "Coworking", "lotacao": 85, "distancia": 12},
    {"nome": "Biblioteca Central", "tipo": "Estudo", "lotacao": 10, "distancia": 15},
    {"nome": "Parque da Cidade", "tipo": "Lazer", "lotacao": 40, "distancia": 20}
]

def analisar_momento_saida(nivel_transito, clima):
    """
    Decide se é um bom momento para sair de casa.
    transito: 0 a 100 (baixo a alto)
    clima: 'ensolarado', 'nublado', 'chuva'
    """
    print(f"\n--- Análise de Contexto ---")
    print(f"Trânsito: {nivel_transito}% | Clima: {clima}")
    
    if nivel_transito < 50 and clima != "chuva":
        return "✅ RECOMENDADO: Ótimo momento para sair! Trânsito favorável."
    elif nivel_transito >= 50 and nivel_transito < 80:
        return "⚠️ ATENÇÃO: Trânsito moderado. Considere esperar 20 minutos."
    else:
        return "❌ NÃO RECOMENDADO: Trânsito pesado ou clima adverso. Fique mais um pouco."

def recomendar_melhor_local(lista_locais):
    """
    Filtra os locais mais vazios e próximos.
    """
    print("\n--- Sugestões Personalizadas para Agora ---")
    sugestoes = []
    
    for local in lista_locais:
        # Lógica: Se a lotação for menor que 50%, é uma boa sugestão
        if local["lotacao"] < 50:
            sugestoes.append(local)
    
    if not sugestoes:
        return "Poxa, todos os seus lugares favoritos parecem cheios agora."
    
    # Ordena por menor lotação (o mais vazio primeiro)
    sugestoes.sort(key=lambda x: x["lotacao"])
    
    for s in sugestoes:
        print(f"📍 {s['nome']} ({s['tipo']})")
        print(f"   Lotação: {s['lotacao']}% | Distância: {s['distancia']} min")
    
    return f"\nO local mais tranquilo é: {sugestoes[0]['nome']}"

def simulador_app():
    print("="*30)
    print("   CITYSYNC - LOGIC ENGINE   ")
    print("="*30)
    
    # Simulando entrada de dados de sensores e APIs
    status_transito = random.randint(10, 90)
    climas_possiveis = ["ensolarado", "nublado", "chuva"]
    clima_atual = random.choice(climas_possiveis)
    
    # 1. Analisar se vale a pena sair
    decisao = analisar_momento_saida(status_transito, clima_atual)
    print(decisao)
    
    # 2. Se for uma boa hora (ou se o usuário insistir), recomendar locais
    if status_transito < 80:
        resultado = recomendar_melhor_local(locais)
        print(resultado)
    else:
        print("\nAguardando melhoria no trânsito para sugerir rotas.")

# Execução do simulador
simulador_app()