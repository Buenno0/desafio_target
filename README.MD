# Desafio Técnico - Verificação de Número na Sequência de Fibonacci

```python
def is_in_fibonacci(number):
    # Inicializar a sequência de Fibonacci com os dois primeiros números
    sequence = [0, 1]
    
    # Gerar números de Fibonacci até que o último número seja maior ou igual ao número de entrada
    while sequence[-1] < number:
        # Adicionar o próximo número de Fibonacci na sequência
        sequence.append(sequence[-1] + sequence[-2])
    
    # Verificar se o número de entrada está na sequência gerada
    return number in sequence

# Ler um número inteiro de entrada do usuário
number = int(input("Digite um número: "))

# Verificar se o número pertence à sequência de Fibonacci e exibir a mensagem apropriada
if is_in_fibonacci(number):
    print(f"O número {number} pertence à sequência de Fibonacci.")
else:
    print(f"O número {number} não pertence à sequência de Fibonacci.")
```

# Desafio Técnico - Contagem da Letra 'A' em uma String

```python 
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

```

# Desafio 3
### Ao final do processamento, o valor da variável SOMA será 77.

# Desafio 4
a) 1, 3, 5, 7, 9

b) 2, 4, 8, 16, 32, 64, 128

c) 0, 1, 4, 9, 16, 25, 36, 49

d) 4, 16, 36, 64, 100

e) 1, 1, 2, 3, 5, 8, 13

f) 2, 10, 12, 16, 17, 18, 19, 27

# Desafio 5
* Ligue o primeiro interruptor e espere alguns minutos.
* Desligue o primeiro interruptor e ligue o segundo.
* Deixe o terceiro interruptor desligado.
* Vá para a sala das lâmpadas e observe:

# Resposta
* ### Lâmpada acesa: está ligada ao segundo interruptor.
* ### Lâmpada apagada e quente: está ligada ao primeiro interruptor.
* ### Lâmpada apagada e fria: está ligada ao terceiro interruptor.