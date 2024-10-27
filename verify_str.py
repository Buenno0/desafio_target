def count_letter_a(text):
    # Converte o texto para minúsculas e conta quantas vezes a letra 'a' aparece
    count = text.lower().count('a')
    return count

def main():
    # Solicita ao usuário que digite uma string
    text = input("Digite uma string: ")
    # Conta quantas vezes a letra 'a' aparece na string fornecida
    count = count_letter_a(text)
    
    # Verifica se a letra 'a' foi encontrada e imprime a mensagem correspondente
    if count > 0:
        print(f"A letra 'a' foi encontrada {count} vezes.")
    else:
        print("A letra 'a' não foi encontrada.")

if __name__ == "__main__":
    main()
