'''
Criação de um aplicativo para um salão de beleza, 
onde os clientes podem agendar serviços, 
escolher profissionais e 
visualizar seus agendamentos futuros. Baseado em CRUD (Create, Read, Update, Delete) 
para gerenciar os agendamentos e os profissionais disponíveis.

DESCRIÇÃO DO PROJETO:
Este sistema é uma ferramenta de gestão para Salões de Beleza que permite realizar 
o ciclo completo de um agendamento (CRUD): cadastrar clientes, consultar a agenda, 
alterar serviços, cancelar registros e gerar relatórios financeiros simples.

'''


# 1. Configuração Inicial (Tabela de Preços e Variáveis de Armazenamento)
tabela_precos = {
    'corte': 30.0,
    'tintura': 20.0,
    'completo': 45.0
}

# Variáveis para guardar o agendamento atual (Estado inicial)
nome_cliente = "Ninguém"
cliente_telefone = "0000-0000"
servico_escolhido = "Nenhum"
valor_servico = 0.0

print('\n== Bem-vindo ao sistema de gerenciamento do Salão de Beleza! ===\n')

while True:
    # Exibição do Menu
    print("\n=== GESTÃO DO SALÃO ===")
    print("1. Agendar Cliente")
    print("2. Ver Agenda")
    print("3. Mudar Serviço")
    print("4. Cancelar Agendamento")
    print("5. Relatorio de Serviços")
    print("0. Sair")

    escolha = input("\nEscolha uma opção: ")

    if escolha == '1':
        print("\n--- Cadastrar cliente ---")
        nome_cliente = input("Digite o nome do cliente: ")
        cliente_telefone = input("Digite o telefone do cliente: ")
        
        print(f"Serviços disponíveis: {list(tabela_precos.keys())}")
        servico = input("Digite o serviço desejado: ").lower()
        
        # Busca o preço no dicionário e guarda nas nossas variáveis
        valor_servico = tabela_precos.get(servico, 0.0)
        
        if valor_servico > 0:
            servico_escolhido = servico
            print(f">> Sucesso! {nome_cliente} agendado para {servico_escolhido}.")
        else:
            print(">> Erro: Serviço inválido. Agendamento incompleto.")

    elif escolha == '2':
        print("\n--- Exibindo agenda ---")
        if nome_cliente == "Ninguém":
            print("A agenda está vazia no momento.")
        else:
            print(f"CLIENTE: {nome_cliente}")
            print(f"TELEFONE: {cliente_telefone}")
            print(f"SERVIÇO: {servico_escolhido.capitalize()}")

    elif escolha == '3':
        print("\n--- Mudando serviço ---")
        if nome_cliente != "Ninguém":
            novo_servico = input(f"Novo serviço para {nome_cliente}: ").lower()
            novo_valor = tabela_precos.get(novo_servico, 0.0)
            
            if novo_valor > 0:
                servico_escolhido = novo_servico
                valor_servico = novo_valor
                print(">> Serviço atualizado com sucesso!")
            else:
                print(">> Erro: Novo serviço não encontrado.")
        else:
            print(">> Não há agendamento ativo para alterar.")

    elif escolha == '4':
        print("\n--- Cancelando agendamento ---")
        nome_cliente = "Ninguém"
        cliente_telefone = "0000-0000"
        servico_escolhido = "Nenhum"
        valor_servico = 0.0
        print(">> O agendamento foi removido do sistema.")

    elif escolha == '5':
        print("\n--- Gerando relatório de serviços ---")
        if valor_servico > 0:
            print(f"Resumo: 1 atendimento pendente ({servico_escolhido}).")
            print(f"Valor total a receber: R${valor_servico:.2f}")
        else:
            print("Sem faturamento pendente.")

    elif escolha == '0':
        print("Saindo do sistema. Até logo!")
        # Comando para o programa não fechar imediatamente no Windows
        input('\nPressione Enter para sair...') 
        break

    else:
        print("Opção inválida. Por favor, tente novamente.")