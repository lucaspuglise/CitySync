# CitySync — Meu App de Cidade Inteligente 🏙️

Este é o nosso projeto para a matéria de Introdução à Computação no CEUB. A ideia é um aplicativo que ajuda as pessoas a decidirem a melhor hora de sair de casa, vendo se os lugares estão cheios ou vazios e como está o trânsito.

🔗 Link do Design [Ver no Figma](https://www.figma.com/make/di6XBjKasy3GHcr1rpuwbO/Cidade-Inteligente?p=f&fullscreen=1 )

## 🚀 O que o app faz?

- Avisa a hora de sair: Ele olha se tem muito trânsito ou se está chovendo para te dar um conselho.

- Mostra lugares vazios: Ele lista quais lugares (academia, café, etc) estão mais tranquilos no momento.

- Dá dicas: Sugere coisas legais para fazer dependendo do clima.

## 🛠️ Como foi feito

Software (Lógica)

Usei Python básico para criar a lógica:

- Condições (If/Else): Para decidir se o trânsito/clima está bom ou ruim.

- Listas: Para guardar os nomes dos lugares e as informações de cada um.

- Sorteio (Random): Como ainda não foram conectadas APIs de mapa e clima, usei o Python para "sortear" o trânsito e o clima para testar.

## Hardware (Ideia)

Para funcionar de verdade, o app precisaria de:

Sensores na porta dos lugares: Para contar quantas pessoas entraram (obviamente apenas lugares seletos).

GPS: Para localizar o usuário.

Servidor: Para guardar os dados de todos os possíveis lugares da cidade.

## O que tem no código?

O arquivo logica.py tem uma lista de lugares e algumas funções para comparar os números e dizer qual o melhor lugar para ir agora.