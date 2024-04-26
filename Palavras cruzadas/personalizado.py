import main
import palavras
import time

revisao = palavras.revisao
dificuldades = {}

def criar_palavras_cruzadas():
    dificuldade = input("Pressione s para começar a criar: ").lower()
    num_perguntas = int(input("Digite o número de perguntas: "))

    palavras_cruzadas = []
    respostas = []
    dicas = []

    for i in range(num_perguntas):
        pergunta = input(f"Digite a pergunta {i + 1}: ")
        resposta = input(f"Digite a resposta {i + 1}: ")
        dica = input(f"Digite a dica {i + 1}: ")

        palavras_cruzadas.append(pergunta)
        respostas.append(resposta)
        dicas.append(dica)

    dificuldades[dificuldade] = list(zip(palavras_cruzadas, respostas, dicas))

    print("Suas palavras cruzadas personalizadas foram criadas com sucesso!")

    
    jogar_palavras_cruzadas(dificuldade)


def jogar_palavras_cruzadas(dificuldade):
    print("\nJogando palavras cruzadas...\n")
    print("Palavras Cruzadas:")
    for i, (pergunta, resposta, _) in enumerate(dificuldades[dificuldade]):
        print(f"{i + 1}. {pergunta}")

    respostas_corretas = 0
    total_perguntas = len(dificuldades[dificuldade])
    for pergunta, resposta, _ in dificuldades[dificuldade]:
        start_time = time.time()
        palpite = input("Sua resposta em até 10 segundos(sem acentos): ").lower()
        end_time = time.time()

        if end_time - start_time > 10:
          print("Tempo esgotado! Voce perdeu a pergunta")
          continue
        if palpite == resposta.lower():
            print("Resposta correta!")
            respostas_corretas += 1
        else:
            print(f"Resposta incorreta. A resposta correta é: {resposta}")

    print("\nFim do jogo!")
    print(f"Você acertou {respostas_corretas} de {total_perguntas} perguntas.")
    retornar = input("Voce quer criar um novo jogo? (s/n) ")
    if retornar.lower() == "s":
        personalizado()
    else:
        return 0
    

def personalizado():
        print("\nMenu:")
        print("1. Criar e jogar palavras cruzadas")
        print("2. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_palavras_cruzadas()
        elif opcao == "2":
            print("Saindo...")
            return 0
        else:
            print("Opção inválida!")

personalizado()

