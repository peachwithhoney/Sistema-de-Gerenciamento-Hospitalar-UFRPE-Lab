class Paciente:
    _id_counter = 1

    def __init__(self, nome, data_nascimento, genero, endereco, telefone, email, historico_medico, plano_saude):
        self.id = Paciente._generate_id()
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.genero = genero
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.historico_medico = historico_medico
        self.plano_saude = plano_saude
        self.consulta = []
        self.cirurgia = []
        self.tratamento = []
        self.feedback = []
        self.prescricao = []

    
    def _generate_id(cls):
        current_id = cls._id_counter
        cls._id_counter += 1
        return current_id

    def __str__(self):
        return (f"Paciente(ID: {self.id}, Nome: {self.nome}, Data de Nascimento: {self.data_nascimento}, "
                f"Gênero: {self.genero}, Endereço: {self.endereco}, Telefone: {self.telefone}, "
                f"Email: {self.email}, Histórico Médico: {self.historico_medico}, Plano de Saúde: {self.plano_saude})")

class Sistema:
    def __init__(self):
        self.pacientes = []  # Lista de pacientes

    def adicionar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def buscar_paciente_por_id(id, paciente_list):
        for paciente in paciente_list:
            if paciente.id == id:
                return paciente
        print("Paciente não encontrado.")
        return None

    def historico_medico(self):
        
        id = int(input("Digite o ID do paciente: ")) 
        paciente = self.buscar_paciente_por_id(id)

        if paciente:
            print(f"Histórico Médico de {paciente.nome}: {paciente.historico_medico}")
        else:
            print("Paciente não encontrado.")

    def escolher_plano_saude(self):
        while True:
            print("Escolha o plano de saúde:")
            print("1. Unimed")
            print("2. Amil")
            print("3. SULAMÉRICA")
            print("4. Bradesco")
            print("5. HAPVIDA")
            opcao = input("Digite o número correspondente à opção desejada: ")

            if opcao == "1":
                return "Unimed"
            elif opcao == "2":
                return "Amil"
            elif opcao == "3":
                return "SULAMÉRICA"
            elif opcao == "4":
                return "Bradesco"
            elif opcao == "5":
                return "HAPVIDA"
            else:
                print("Opção inválida. Escolha uma opção correta.")

    def cadastrar_paciente(self):
        
        nome = input("Digite o nome do paciente: ")
        data_nascimento = input("Digite a data de nascimento do paciente: ")
        genero = input("Digite o gênero do paciente: ")
        endereco = input("Digite o endereço do paciente: ")
        telefone = input("Digite o telefone do paciente: ")
        email = input("Digite o email do paciente: ")
        historico_medico = input("Digite o histórico médico do paciente: ")
        plano_saude = self.escolher_plano_saude()
        
        paciente = Paciente(nome, data_nascimento, genero, endereco, telefone, email, historico_medico, plano_saude)
        self.adicionar_paciente(paciente)
        print(f"Paciente {nome} cadastrado com sucesso!")

    def atualizar_paciente(self):
       
        id = int(input("Digite o ID do paciente: "))
        paciente = self.buscar_paciente_por_id(id)

        if paciente:
            print(f"Paciente encontrado: {paciente}")

            print(f"O que deseja atualizar no paciente {paciente.nome}?")
            print("1. Nome")
            print("2. Data de Nascimento")
            print("3. Gênero")
            print("4. Endereço")
            print("5. Telefone")
            print("6. Email")
            print("7. Histórico Médico")
            print("8. Plano de Saúde")
            opcao = input("Digite o número correspondente à opção desejada: ")
            if opcao == "1":
                novo_nome = input("Digite o novo nome: ")
                paciente.nome = novo_nome
                print("Nome atualizado com sucesso!")
            elif opcao == "2":
                nova_data_nascimento = input("Digite a nova data de nascimento: ")
                paciente.data_nascimento = nova_data_nascimento
                print("Data de nascimento atualizada com sucesso!")
            elif opcao == "3":
                novo_genero = input("Digite o novo gênero: ")
                paciente.genero = novo_genero
                print("Gênero atualizado com sucesso!")
            elif opcao == "4":
                novo_endereco = input("Digite o novo endereço: ")
                paciente.endereco = novo_endereco
                print("Endereço atualizado com sucesso!")
            elif opcao == "5":
                novo_telefone = input("Digite o novo telefone: ")
                paciente.telefone = novo_telefone
                print("Telefone atualizado com sucesso!")
            elif opcao == "6":
                novo_email = input("Digite o novo email: ")
                paciente.email = novo_email
                print("Email atualizado com sucesso!")
            elif opcao == "7":
                novo_historico_medico = input("Digite o novo histórico médico: ")
                paciente.historico_medico = novo_historico_medico
                print("Histórico médico atualizado com sucesso!")
            elif opcao == "8":
                novo_plano_saude = input("Digite o novo plano de saúde: ")
                paciente.plano_saude = novo_plano_saude
                print("Plano de saúde atualizado com sucesso!")
            else:
                print("Opção inválida.")
        else:
            print("Paciente não encontrado.")

    def excluir_paciente_por_id(self):
       
        id = int(input("Digite o ID do paciente: "))
        paciente = self.buscar_paciente_por_id(id)

        if paciente:
            print(f"Paciente encontrado: {paciente}")
            confirmacao = input("Tem certeza que deseja excluir este paciente? (Sim/Não)").strip().lower()
            if confirmacao == "sim":
                self.pacientes.remove(paciente)
                print("Paciente excluído com sucesso!")
            else:
                print("Ação Cancelada")
        else:
            print("Paciente não encontrado.")

    def visualizar_todos_pacientes(self):
       
        if not self.pacientes:
            print("Não há pacientes cadastrados.")
        else:
            print("Lista de pacientes:")
            for paciente in self.pacientes:
                print(paciente)

    def visualizar_pacientes(self):
       
        visualizar_todos = input("Deseja visualizar todos os pacientes? (Sim/Não)").strip().lower()
        if visualizar_todos == "sim":
            self.visualizar_todos_pacientes()
        elif visualizar_todos == "não":
            visualizar_unico = input("Deseja ver algum paciente em específico? (Sim/Não)").strip().lower()
            if visualizar_unico == "sim":
                input("Digite o ID do paciente: ")
                self.buscar_paciente_por_id(id)
            elif visualizar_unico == "não":
                print("Nada a ser exibido.")
            else:
                print("Opção inválida.")
        else:
            print("Opção inválida.")

    def menu(self):
        
        while True:
            print("\nMenu:")
            print("1. Cadastrar Paciente")
            print("2. Atualizar Paciente")
            print("3. Excluir Paciente")
            print("4. Visualizar Pacientes")
            print("5. Histórico Médico")
            print("6. Sair")

            opcao = input("Digite o número da opção desejada: ")
            if opcao == "1":
                self.cadastrar_paciente()
            elif opcao == "2":
                self.atualizar_paciente()
            elif opcao == "3":
                self.excluir_paciente_por_id()
            elif opcao == "4":
                self.visualizar_pacientes()
            elif opcao == "5":
                self.historico_medico()
            elif opcao == "6":
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")
