import time
import random

def iniciar_monitoramento_infra():
    print("="*60)
    print("  CITYSYNC - MONITOR DE INFRAESTRUTURA E REDES (TERMINAL) ")
    print("="*60)
    print("Iniciando varredura dos Gateways locais via protocolo MQTT...\n")
    
    status_sensores = ["Online", "Online", "Online", "Bateria Baixa (Nobreak Ativado)", "Offline (Timeout)"]
    locais_teste = ["Smart Gym Center", "Café Tech Hub", "Biblioteca Central"]
    
    for i in range(4):
        local = random.choice(locais_teste)
        tempo_resposta_ms = random.randint(15, 220)
        status_atual = random.choice(status_sensores)
        
        print(f"[LOG REDE] Ping Gateway ({local}): {tempo_resposta_ms}ms")
        
        if tempo_resposta_ms > 150:
            print("   -> ⚠️ [ALERTA DE LATÊNCIA]: Gargalo na rede celular. Ativando Rate Limiting no Firewall...")
            
        if status_atual == "Offline (Timeout)":
            print(f"   -> ❌ [CRÍTICO]: Sensor de porta do '{local}' parou de responder. Verificar cabeamento.")
        elif "Bateria" in status_atual:
            print(f"   -> ⚡ [FALHA MITIGADA]: Queda de energia elétrica detectada no '{local}'. Redundância física ativada (Bateria).")
            
        print("-" * 40)
        time.sleep(1.2)

    print("\n[Varredura Concluída] Todos os perímetros e VLANs operando sob protocolo seguro.")

if __name__ == "__main__":
    iniciar_monitoramento_infra()