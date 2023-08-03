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
    if leitura not in code:
        print('Utilizador inexistente')
    passe = str(input('Digite a sua senha: ')).strip()
    print(f'Seja bem-vindo ')
