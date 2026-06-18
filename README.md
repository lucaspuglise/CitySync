# CitySync — Meu App de Cidade Inteligente 🏙️

Este é o meu projeto para a matéria de Introdução à Computação no CEUB. A ideia é um aplicativo que ajuda as pessoas a decidirem a melhor hora de sair de casa em Brasília, analisando se os estabelecimentos estão cheios ou vazios e como está o trânsito.

🔗 Link do Design [Ver no Figma](https://www.figma.com/make/di6XBjKasy3GHcr1rpuwbO/Cidade-Inteligente?p=f&fullscreen=1)

---

## 🚀 O que o app faz?
- **Avisa a hora de sair:** Avalia o trânsito e o clima para dar um conselho se vale a pena sair de casa.
- **Mostra lugares vazios:** Lista estabelecimentos parceiros (como academias e cafés) e aponta quais estão mais tranquilos no momento.
- **Segurança Ativa:** Garante que os dados de lotação sejam reais e que o sistema não caia por falhas ou dados corrompidos.
    
# 🛠️ Atualizações do aplicativo CitySync (2.0):
 - Melhoria no layout e navegação, trazendo mais modernidade e fluidez;
 - Mais botões interativos, melhorando a imersão;
 - Adição da função "tema", podendo alterar para o modo "escuro" ou "noite".
 - Adição de sensores: agora com a atuação de sensores nos locais em questão para ainda mais precisão.

---

## 🛠️ Como foi feito (Atualizado AV02)

### 💻 Software (Lógica e Segurança)
O sistema foi desenvolvido em Python básico e expandido com defesas lógicas:
- **Condições (If/Else):** Para tomada de decisão sobre o contexto da cidade.
- **Listas:** Armazenamento dos estabelecimentos e seus metadados.
- **Travas de Código (Mitigação):** O arquivo `logica.py` agora possui uma função defensiva com estruturas `try/except` e condicionais que validam os dados dos sensores, descartando na hora textos maliciosos, números negativos ou valores irreais.

### 🔌 Infraestrutura de Redes (Fluxo do Dado)
Explicamos detalhadamente como a informação viaja com segurança da ponta até o usuário:
1. **Borda (Sensores):** Sensores de fluxo nas portas coletam os dados e transmitem via **LoRaWAN** (baixo consumo de banda e alta bateria).
2. **Processamento (Nuvem):** Um Gateway central recebe esses dados e envia para o servidor em nuvem usando **4G/5G** através do protocolo **MQTT** (conexão leve e constante que evita o desperdício de dados).
3. **Interface (Usuário):** O servidor processa e entrega as informações para o aplicativo do usuário final utilizando **Wi-Fi/Rede Móvel** via protocolo **HTTPS** (criptografia essencial para proteger a localização do cidadão).

---

## 📂 O que tem no repositório?

- `logica.py`: Contém a inteligência do aplicativo, a simulação de funcionamento dos locais e a **trava de segurança de software** contra inputs inválidos.
- `monitor_terminal.py`: Script focado em infraestrutura que simula a varredura da rede em tempo real, testando a latência dos gateways (simulando regras de Firewall) e monitorando a queda de energia nos sensores (simulando a redundância por baterias físicas).

---

## 👥 Autor
- Lucas Puglise