from style import estilo

def main():
    estilo('Convivio do Futungo')
    print('''
1 - Registrar uma compra
2 - Ultima factura
3 - Mudar de utilizador
4 - Fecho do programa
''')
          
def user():
    estilo('LOGIN DO SISTEMA')
    nome = str(input('Digite o seu nome: '))
    code = input('Digite o seu codigo de funcionario: ')
    print(f'Seja bem-vindo {nome}')