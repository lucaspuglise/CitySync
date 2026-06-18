import random

locais = [
    {"nome": "Smart Gym Center", "tipo": "Academia", "lotacao": 25, "distancia": 8},
    {"nome": "Café Tech Hub", "tipo": "Coworking", "lotacao": 85, "distancia": 12},
    {"nome": "Biblioteca Central", "tipo": "Estudo", "lotacao": 10, "distancia": 15},
    {"nome": "Parque da Cidade", "tipo": "Lazer", "lotacao": 40, "distancia": 20}
]

def atualizar_lotacao_segura(nome_local, novo_dado):
    """
    TRAVA DE CÓDIGO (MITIGAÇÃO DE SOFTWARE):
    Verifica se o dado recebido do sensor (hardware) é válido antes de aceitar.
    Evita o travamento do sistema por dados corrompidos.
    """
    try:
        lotacao_real = int(novo_dado)
        
        #(If/Else defensivo)
        if lotacao_real < 0:
            print(f"⚠️ ERRO DE SOFTWARE: Sensor do {nome_local} enviou número negativo ({lotacao_real}). Dado rejeitado.")
            return False
        elif lotacao_real > 100:  # Limite de porcentagem de lotação
            print(f"⚠️ ERRO DE SOFTWARE: Sensor do {nome_local} enviou lotação acima de 100% ({lotacao_real}%). Possível falha física.")
            return False
        else:
            for local in locais:
                if local["nome"] == nome_local:
                    local["lotacao"] = lotacao_real
            print(f"✅ DADO SEGURO: Lotação do '{nome_local}' atualizada para {lotacao_real}%.")
            return True
            
    except ValueError:
        print(f"❌ ATAQUE OU FALHA CRÍTICA: O sensor do {nome_local} enviou texto/formato inválido. Bloqueado por segurança.")
        return False

def analisar_momento_saida(nivel_transito, clima):
    print(f"\n--- Análise de Contexto ---")
    print(f"Trânsito: {nivel_transito}% | Clima: {clima}")
    
    if nivel_transito < 50 and clima != "chuva":
        return "✅ RECOMENDADO: Ótimo momento para sair! Trânsito favorável."
    elif nivel_transito >= 50 and nivel_transito < 80:
        return "⚠️ ATENÇÃO: Trânsito moderado. Considere esperar 20 minutos."
    else:
        return "❌ NÃO RECOMENDADO: Trânsito pesado ou clima adverso."

def recomendar_melhor_local(lista_locais):
    print("\n--- Sugestões Personalizadas para Agora ---")
    sugestoes = []
    
    for local in lista_locais:
        if local["lotacao"] < 50:
            sugestoes.append(local)
    
    if not sugestoes:
        return "Poxa, todos os seus lugares favoritos parecem cheios agora."
    
    sugestoes.sort(key=lambda x: x["lotacao"])
    
    for s in sugestoes:
        print(f"📍 {s['nome']} ({s['tipo']})")
        print(f"   Lotação: {s['lotacao']}% | Distância: {s['distancia']} min")
    
    return f"\nO local mais tranquilo é: {sugestoes[0]['nome']}"

def simulador_app():
    print("="*45)
    print("   CITYSYNC - LOGIC ENGINE (AV02 SEGURO)   ")
    print("="*45)
    
    print("\n[Simulando recebimento de dados dos Sensores de Borda]")

    atualizar_lotacao_segura("Smart Gym Center", "30")
    atualizar_lotacao_segura("Café Tech Hub", "-15")
    atualizar_lotacao_segura("Biblioteca Central", "ERRO_TEXTO")
    
    status_transito = random.randint(10, 90)
    climas_possiveis = ["ensolarado", "nublado", "chuva"]
    clima_atual = random.choice(climas_possiveis)
    
    decisao = analisar_momento_saida(status_transito, clima_atual)
    print(decisao)
    
    resultado_local = recomendar_melhor_local(locais)
    print(resultado_local)

if __name__ == "__main__":
    simulador_app()