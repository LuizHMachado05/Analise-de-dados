import main
import palavras
import random
import jogar
import time

def jogar():
  dificuldades = palavras.dificuldades
  revisao = palavras.revisao
  
  nivel_dificuldade = input("Escolha o nível de dificuldade (facil/medio/dificil): ").lower()   
  pontuacao = 0
  
  while nivel_dificuldade not in ["facil", "medio", "dificil"]:
        print("Nivel de dificuldade inválido, opções: facil, médio, difícil")
        nivel_dificuldade = input("Escolha o nível de dificuldade (facil/medio/dificil): ").lower()
 
  dificuldade_setada = nivel_dificuldade      
  palavras_cruzadas, respostas, dica = zip(*dificuldades[dificuldade_setada.lower()]) 
    
  num_clues = 5
  random_indices = random.sample(range(len(palavras_cruzadas)), num_clues)
  random_indices = random.sample(range(len(dica)), num_clues)
  palavras_cruzadas = [palavras_cruzadas[i] for i in random_indices]
  respostas = [respostas[i] for i in random_indices]
  dica = [dica[i] for i in random_indices]
  pontuacao_por_acerto = 2
  pontuacao_max = 10
  pontos_perdidos = 1
  

               
  if dificuldade_setada == "facil":
        mensagem_correto = "Muito bem! Você acertou! | pontuação atual: {}"
        mensagem_incorreto = "Ops, essa não era a resposta. A resposta correta é: {}, Pontuação atual: {}"
        print("Pontuação por rodada = 2")
        print("Pontos perdidos por erro = 1")
        
  elif dificuldade_setada == "medio":
        mensagem_correto = "Parabéns! Você acertou! | pontuação atual: {}"
        mensagem_incorreto = "Hmm, essa não era a resposta certa, A resposta correta é: {}, Pontuação atual: {}"
        print("Pontuação por rodada = 2")
        print("Pontos perdidos por erro = 1")
        
  elif dificuldade_setada == "dificil":
        mensagem_correto = "Muito bem! Você acertou! | pontuação atual: {}"
        mensagem_incorreto = "Ops, essa não era a resposta, A resposta correta é: {} | Pontuação atual: {}"
        print("Pontuação por rodada = 2")
        print("Pontos perdidos por erro = 1")
        
        
    
  for i, pista in enumerate(palavras_cruzadas):
        print(f"{i + 1}. {pista}")   
        print(f"{dica[i]}")
        
        start_time = time.time()
        palpite = input("Sua resposta em até 10 segundos(sem acentos): ").lower()
        end_time = time.time()

        if end_time - start_time > 10:
          print("Tempo esgotado! Voce perdeu 1 ponto")
          pontuacao -= pontos_perdidos
          print(f"Pontuação atual: {pontuacao}")
          continue
        
        if palpite == respostas[i]:
          pontuacao += pontuacao_por_acerto
          print(mensagem_correto.format(pontuacao))
          
        elif palpite != respostas[i]:
          pontuacao -= pontos_perdidos
          print(mensagem_incorreto.format(respostas[i], pontuacao))
          
        if pontuacao < 0:
            pontuacao = 0
                 
  print(f"\nSua Pontuação Final é: {pontuacao} de {pontuacao_max}")
    
jogar()