import os

restaurantes = [{'nome': 'Praça', 'categoria': 'Pastelão', 'ativo': True},
                {'nome': 'Pizzaria do Jânio', 'categoria': 'Pizza', 'ativo':False},
                {'nome': 'Cantina', 'categoria': 'Italiana', 'ativo': False}
                ]

def nome_do_programa():
    '''Esta função é responsável por exibir o texto de início do app'''
    print('''
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░ 
''')

def exibir_opcoes():
    '''Esta função é responsável por exibir as opções disponiveis para interagir'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alterar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''Esta função é responsável por exibir uma menságem de encerramento do app'''
    os.system('cls')
    print('Finalizando  app')

def exibir_subtitulo(texto):
    '''Esta função é responsável por facilitar a colocação de subtitulos'''
    os.system('cls')
    linha = '*' * (len(texto) + 2)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''Esta função é responsável por cadastrar novos restaurantes'''
    os.system('cls')
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria de restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria': categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    input('\nTecle Enter para voltar ao menu principal: ')
    main()

def opcao_invalida():
    '''Esta função é responsável por exibir uma mensagem quando um caractere ou texto inválido seja digitado'''
    exibir_subtitulo('Opção inválida')
    input('Tecle Enter para voltar ao menu principal: ')
    main()

def listar_restaurantes():
    '''Esta função é responsável por listar os restaurantes'''
    exibir_subtitulo('Listando os restaurantes')
    print(f"{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'status'}")
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    input('\nTecle Enter para voltar ao menu principal: ')
    main()

def alternar_estado_restaurante():
    '''Esta função é responsável por alterar o estado do restaurante entre ativado e desativado'''
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
            input('\nTecle Enter para voltar ao menu principal: ')
            main()
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
        input('\nTecle Enter para voltar ao menu principal: ')
        main()

def escolher_opcao():
    '''Esta função é responsável por identificar qual opção foi  escolhida pelo usuário'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''Função principal q inicia o programa'''
    os.system('cls')
    nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()