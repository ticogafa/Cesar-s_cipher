def cifrar_caractere(caractere, deslocamento):
    codigo = ord(caractere)
    
    # Verifica se o caractere é uma letra maiúscula
    if 65 <= codigo <= 90:
        codigo = (codigo - 65 + deslocamento) % 26 + 65
    
    # Verifica se o caractere é uma letra minúscula
    if 97 <= codigo <= 122:
        codigo = (codigo - 97 + deslocamento) % 26 + 97
    
    return chr(codigo)


def cifra_de_cesar(mensagem, deslocamento):
    mensagem_cifrada = ""
    
    for caractere in mensagem:
        mensagem_cifrada += cifrar_caractere(caractere, deslocamento)
    
    return mensagem_cifrada


mensagem = input("Digite a mensagem a ser cifrada: ")
deslocamento = int(input("Digite o valor do deslocamento: "))

# Converte o deslocamento para um valor válido entre 0 e 25
deslocamento = deslocamento % 26

mensagem_cifrada = cifra_de_cesar(mensagem, deslocamento)
print("Mensagem cifrada:", mensagem_cifrada)