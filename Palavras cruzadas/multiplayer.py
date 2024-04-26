# prompt: Introduza um modo multiplayer onde dois ou mais 
# jogadores possam competir para acertar mais respostas

import random
import palavras
import time

def jogar_multiplayer():
  dificuldades = palavras.dificuldades
  revisao = palavras.revisao

  nivel_dificuldade = input("Escolha o nível de dificuldade (facil/medio/dificil): ").lower()
  dificuldade_setada = nivel_dificuldade
  while nivel_dificuldade not in ["facil", "medio", "dificil"]:
    print("Nivel de dificuldade inválido, opções: facil, médio, difícil")
    nivel_dificuldade = input("Escolha o nível de dificuldade (facil/medio/dificil): ").lower()
    dificuldade_setada = nivel_dificuldade

  palavras_cruzadas, respostas, dica = zip(*dificuldades[dificuldade_setada.lower()])

  num_jogadores = int(input("Quantos jogadores irão participar? "))
  jogadores = {}
  for i in range(num_jogadores):
    nome = input(f"Digite o nome do jogador {i+1}: ")
    jogadores[nome] = 0

  num_rodadas = int(input("Quantas rodadas vocês querem jogar? "))

  for rodada in range(num_rodadas):
    random_indices = random.sample(range(len(palavras_cruzadas)), num_jogadores)
    palavras_cruzadas_rodada = [palavras_cruzadas[i] for i in random_indices]
    respostas_rodada = [respostas[i] for i in random_indices]
    dica_rodada = [dica[i] for i in random_indices]

    for i, jogador in enumerate(jogadores):
      print(f"\nVez do jogador {jogador}")
      print(f"{i + 1}. {palavras_cruzadas_rodada[i]}")
      print(f"{dica_rodada[i]}")
      

      start_time = time.time()
      palpite = input("Sua resposta em até 10 segundos(sem acentos): ").lower()
      end_time = time.time()

      if end_time - start_time > 10:
          print("Tempo esgotado! Voce perdeu 1 ponto")
          jogadores[jogador] -= 1
          print(f"Pontuação atual: {jogadores[jogador]}")
          continue

      if palpite == respostas_rodada[i]:
        jogadores[jogador] += 2
        print(f"Parabéns {jogador}, você acertou! Sua pontuação atual é: {jogadores[jogador]}")
      else:
        jogadores[jogador] -= 1
        print(f"Ops {jogador}, essa não era a resposta. A resposta correta é: {respostas_rodada[i]}")
        print(f"Sua pontuação atual é: {jogadores[jogador]}")
        
      scores = list(jogadores.values())
  if scores.count(max(scores)) > 1:
    print("\nEmpate!")
  else:
    vencedor = max(jogadores, key=jogadores.get)
    print(f"\nParabéns {vencedor}, você venceu o jogo!")
    

jogar_multiplayer()
