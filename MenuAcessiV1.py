# Menu com funcionalidades iniciais 

opcao = ''  # Variável para armazenar a opção do menu

# O loop principal que mantém o programa rodando até o usuário escolher sair
while opcao != '4':
    
    # Mostrar o menu
    print("\n------- Menu Principal ------")
    print("1. Registrar Alerta para Passageiros")
    print("2. Previsão de Manutenção")
    print("3. Verificar Notificações Recebidas")
    print("4. Sair")

    # Recebe a opção do usuário
    opcao = input("Selecione uma opção de 1 a 4: ")

    # Verifica qual opção foi selecionada
    if opcao == '1':
        # Registrar Alerta para Passageiros
        print("\n--- Registrar Alerta ---")
        alerta = input("Digite o alerta a ser enviado para os passageiros: ")

        if alerta:  # Verificação se entrada não é vazia
            print("Seu alerta foi registrado com sucesso! O seu alerta foi:", alerta)
        else:
            print("Nenhum alerta registrado. Entrada inválida.")
    
    elif opcao == '2':
        # Previsão de Manutenção
        print("\n--- Previsão de Manutenção ---")
        manutencao = input("Digite o tipo de manutenção ou previsão (Ex: Revisão Técnica, Falha Imediata): ")

        if manutencao:  # Verificar se a entrada não é vazia
            print("Previsão de manutenção registrada e agendada. A manuntenção foi:", manutencao)
        else:
            print("Nenhuma previsão registrada. Entrada inválida.")
    
    elif opcao == '3':
        # Verificar Notificações Recebidas
        print("\n--- Verificar Notificações ---")
        notificacoes = ["Alerta de atraso na linha 8", "Previsão de manutenção na linha 9"]

        if notificacoes:
            print("Notificações recebidas:")
            for notificacao in notificacoes:
                print(f"- {notificacao}")
        else:
            print("Nenhuma notificação no momento.")
    
    elif opcao == '4':
        # Encerrar o programa
        print("Programa finalizado. Até logo!")
    
    else:
        # Caso o usuário insira uma opção inválida
        print("Opção inválida. Por favor, selecione uma opção valida.")
