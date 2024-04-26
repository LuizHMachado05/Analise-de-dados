import main
import palavras


def revisao_pronto():
    dificuldades = palavras.dificuldades
    revisao = palavras.revisao

    nivel_dificuldade = input("Quais perguntas gostaria de revisar? (facil/medio/dificil): ").lower()

    while nivel_dificuldade not in ["facil", "medio", "dificil"]:
        print("Nivel de dificuldade inválido, opções: facil, médio, difícil")
        nivel_dificuldade = input("Quais perguntas gostaria de revisar? (facil/medio/dificil): ").lower()
        print("Opção inválida! Por favor, digite 'facil', 'medio' ou 'dificil'.")

    revisao_done = revisao[nivel_dificuldade.lower()]
    print(revisao_done)
    
 
revisao_pronto()