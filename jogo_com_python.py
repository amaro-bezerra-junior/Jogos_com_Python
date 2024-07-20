import random
import pandas as pd

# Função para escolher uma das categorias propostas pelo jogo
def escolher_palavra(categoria):
    df = pd.read_excel('Listagem.xlsx', sheet_name=categoria)
    escolha = random.choice(df.index)
    palavra = df.iloc[escolha, 0]
    dica = df.iloc[escolha, 1]
    return palavra, dica

# Função para montar as linhas
def exibir_tabuleiro(palavra_escolhida, letras_adivinhadas):
    display = ''
    for letra in palavra_escolhida:
        if letra == ' ' or letra in letras_adivinhadas:
            display += letra + ' '
        else:
            display += '_ '
    return display.strip()

# Função para jogar
def jogar_forca():
    while True:
        print("********** Bem-vindo ao Jogo da Forca! **********")
        print()
        print("********** Regras **********")
        print()
        print("Escolha uma das categorias abaixo para iniciar o jogo.")
        print("Considere a acentuação das letras para acertar!")
        print()
        print("Escolha uma categoria:")
        print("1. Frutas")
        print("2. Futebol")
        print("3. Países")
        print("4. Comidas")
        print("5. Profissões")
        print()

        opcao = input("Digite o número da categoria escolhida: ").strip()

        if opcao == "1":
            categoria = "Frutas"
        elif opcao == "2":
            categoria = "Futebol"
        elif opcao == "3":
            categoria = "Países"
        elif opcao == "4":
            categoria = "Comidas"
        elif opcao == "5":
            categoria = "Profissões"
        else:
            print("Categoria inválida. Tente novamente.")
            continue

        palavra_escolhida, dica = escolher_palavra(categoria)
        letras_adivinhadas = [' ']
        tentativas = 5

        print(f"\nDica: {dica}")

        while tentativas > 0:
            print("\nPalavra:", exibir_tabuleiro(palavra_escolhida, letras_adivinhadas))
            print(f"Tentativas restantes: {tentativas}")
            tentativa = input("Adivinhe uma letra: ").upper()

            if tentativa in letras_adivinhadas:
                print("Você já adivinhou essa letra. Tente outra.")
            elif tentativa in palavra_escolhida:
                letras_adivinhadas.append(tentativa)
                print("Boa! Você adivinhou uma letra.")
            else:
                letras_adivinhadas.append(tentativa)
                tentativas -= 1
                print("Letra errada. Tente novamente.")

            if all(letra in letras_adivinhadas for letra in palavra_escolhida):
                print(f"\nParabéns! Você adivinhou a palavra: {palavra_escolhida}")
                break
        else:
            print(f"\nVocê perdeu! A palavra era: {palavra_escolhida}")

        jogar_novamente = input("\nDeseja jogar novamente? (s/n): ").strip().lower()
        if jogar_novamente != 's':
            print("Obrigado por jogar! Até a próxima.")
            break

# Iniciar o jogo da Forca
if __name__ == "__main__":
    jogar_forca()
