from style import estilo
from usuario import code, nomes, senha

def main():
    estilo('Convivio do Futungo')
    print('''
1 - Registrar uma compra
2 - Ultima factura
3 - Mudar de utilizador
4 - Fecho do programa
''')
          
def user():
    estilo('SISTEMA DE LOGIN')
    leitura = str(input('Digite o seu codigo funcionario: ')).strip()
    while True:
        if leitura not in code:
            print('Utilizador inexistente')
            leitura = str(input('Digite novamente o codigo de funcionario: ')).strip()
        else:
            break
    passe = str(input('Digite a sua senha: ')).strip()
    while True:
        if passe not in senha:
            print('Codigo incorrecto')
            passe = str(input('Por favor digite novamente: ')).strip()
        else:
            break

    #Condicoes de code e senha
    if leitura == code[0] and passe == senha[0]:
        print(f'Seja bem-vindo {nomes[0]}')
    elif leitura == code[1] and passe == senha[1]:
        print(f'Seja bem-vindo {nomes[1]}')
    elif leitura == code[2] and passe == senha[2]:
        print(f'Seja bem-vindo {nomes[2]}')
    elif leitura == code[3] and passe == senha[3]:
        print(f'Seja bem-vindo {nomes[3]}')
    else:
        print(f'Codigo ou senha incorrecta')
