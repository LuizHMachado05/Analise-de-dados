import time
import palavras
import random
def main():
    
    dificuldades = palavras.dificuldades
    
    
    print("  Bem Vindo ao jogo de palavras Cruzadas  ")
    print("  Acerte a respostas das perguntas   ")
    print('''
          1. Estudar as perguntas e as respostas
          2. Jogar Singleplayer
          3. Jogar Multiplayer
          4. Jogo Adaptativo
          5. Jogo Personalizado
          6. Sair
    ''')
    
       
    opcao = (input("Digite a opção desejada: "))   
    
    if opcao == "1":       
        import revisão
        retornar = print("Aqui estao as palavras do modo escolhido!!!")
        return 0
    elif opcao == "2":
        import jogar
    elif opcao == "3":
        import multiplayer
    elif opcao == "4":
        import adaptativo
    elif opcao == "5":
        import personalizado
    elif opcao == "6":
        return 0
    else:
        return main()
            
        
if __name__ == "__main__":

 main()

