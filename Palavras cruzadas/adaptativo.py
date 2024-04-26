import palavras
import main
import time
import random

def jogar_adaptativo():
  dificuldades = palavras.dificuldades
  revisao = palavras.revisao

  dificuldade_atual = "facil"
  pontuacao = 0

  while True:
    palavras_cruzadas, respostas, dica = zip(*dificuldades[dificuldade_atual])

    num_clues = 5
    random_indices = random.sample(range(len(palavras_cruzadas)), num_clues)
    palavras_cruzadas = [palavras_cruzadas[i] for i in random_indices]
    respostas = [respostas[i] for i in random_indices]
    dica = [dica[i] for i in random_indices]

    for i, pista in enumerate(palavras_cruzadas):
      print(f"{i + 1}. {pista}")
      print(f"{dica[i]}")

      start_time = time.time()
      palpite = input("Sua resposta em até 10 segundos(sem acentos): ").lower()
      end_time = time.time()

      if end_time - start_time > 10:
        print("Tempo esgotado! Voce perdeu 1 ponto")
        pontuacao -= 1
        print(f"Pontuação atual: {pontuacao}")
        continue

      if palpite == respostas[i]:
        pontuacao += 2
        print("Muito bem! Você acertou! | pontuação atual: {}".format(pontuacao))

      elif palpite != respostas[i]:
        pontuacao -= 1
        print("Ops, essa não era a resposta. A resposta correta é: {}, Pontuação atual: {}".format(respostas[i], pontuacao))

      if pontuacao < 0:
        pontuacao = 0

      if pontuacao >= 7 and dificuldade_atual == "facil":
        dificuldade_atual = "medio"
        pontuacao = 0
        print("Parabéns! Você está indo bem! Vamos aumentar a dificuldade para médio.")
        break
      elif pontuacao >= 7 and dificuldade_atual == "medio":
        dificuldade_atual = "dificil"
        pontuacao = 0
        print("Incrível! Você está arrasando! Vamos aumentar a dificuldade para difícil.")
        
      elif pontuacao >= 17 and dificuldade_atual == "dificil":
        print("Parabens voce venceu o modo adaptativo!!!")
        return 0

      if pontuacao <= -3:
        dificuldade_atual = "facil"
        print("Parece que você está com dificuldade. Vamos diminuir a dificuldade para fácil.")

    print(f"\nSua Pontuação Final é: {pontuacao}")

    continuar = input("Deseja continuar jogando? (s/n): ")
    if continuar.lower() != "s":
      break

jogar_adaptativo()
