import Cirurgia

class Medico:
    _id_counter = 1

    def __init__(self, nome, data_nascimento, telefone, email, especialidade, CRM, departamento):
        self.id = Medico._generate_id()
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.telefone = telefone
        self.email = email
        self.especialidade = especialidade
        self.CRM = CRM
        self.departamento = departamento
        self.consulta = []
        self.cirurgia = []
        self.tratamento = []
        self.feedback = []
        self.exame = []

        def _generate_id(cls):
            current_id = cls._id_counter
            cls._id_counter += 1
            return current_id
        
        def __str__(self):
            return (f"Medico(ID: {self.id}, Nome: {self.nome}, Data de Nascimento: {self.data_nascimento}, Telefone: {self.telefone}, Email: {self.email}, Especialidade: {self.especialidade}, CRM: {self.CRM}, Departamento: {self.departamento})")
        
        def cadastrar_medico(medico_list):
            nome = input("Digite o nome do médico: ")
            data_nascimento = input("Digite a data de nascimento do médico: ")
            telefone = input("Digite o telefone do paciente: ")
            email = input("Digite o email do paciente: ")
            especialidade = input("Digite a especialidade do médico: ")
            CRM = input("Digite o CRM do médico: ")
            departamento = input("Digite o departamento do médico: ")
                        
            medico = Medico(nome, data_nascimento, telefone, email, especialidade, CRM, departamento)
            medico_list.append(medico)

            print(f"Médico {nome} cadastrado com sucesso!")

        def buscar_medico_por_id(id, medico_list):
            for medico in medico_list:
                if medico.id == id:
                    return medico
            print("Médico não encontrado.")

        def atualizar_medico(medico_list):
            id = int(input("Digite o ID do médico que deseja atualizar: "))
            medico = buscar_medico_por_id(id, medico_list)

            if medico:
                print(f"Médico encontrado: {medico}")

                print(f"O que deseja atualizar no médico {medico.nome}?")
                print("1. Nome")
                print("2. Data de Nascimento")
                print("3. Telefone")
                print("4. Email")
                print("5. Especialidade")
                print("6. CRM")
                print("7. Departamento")

                opcao = int(input("Digite o número correspondente à opção desejada: "))

                if opcao == 1:
                    medico.nome = input("Digite o novo nome do médico: ")
                elif opcao == 2:
                    medico.data_nascimento = input("Digite a nova data de nascimento do médico: ")
                elif opcao == 3:
                    medico.telefone = input("Digite o novo telefone do médico: ")
                elif opcao == 4:
                    medico.email = input("Digite o novo email do médico: ")
                elif opcao == 5:
                    medico.especialidade = input("Digite a nova especialidade do médico: ")
                elif opcao == 6:
                    medico.CRM = input("Digite o novo CRM do médico: ")
                elif opcao == 7:
                    medico.departamento = input("Digite o novo departamento do médico: ")

                print("Médico atualizado com sucesso!")

            def excluir_medico_por_id(medico_list):
                id = int(input("Digite o ID do médico que deseja excluir: "))
                medico = buscar_medico_por_id(id, medico_list)

                if medico:
                    medico_list.remove(medico)
                    print(f"Médico {medico.nome} excluído com sucesso!")

            def visualizar_medicos(medico_list):
                if not medico_list:
                    print("Não há médicos cadastrados.")
                else:
                    print("Lista de médicos:")
                    for medico in medico_list:
                        print(medico)

            def adicionar_consulta(self, consulta):
                self.consultas.append(consulta)

            def atualizar_consulta(self, consulta_id, novos_dados):
                self.consultas[consulta_id] = novos_dados

            def cancelar_consulta(self, consulta_id):
                self.consultas.pop(consulta_id)

            def visualizar_consultas(self):
                return self.consultas

            def adicionar_cirurgia(self, cirurgia):
                self.cirurgias.append(cirurgia)

            def atualizar_cirurgia(self, cirurgia_id, novos_dados):
                self.cirurgias[cirurgia_id] = novos_dados

            def visualizar_cirurgias(self):
                return self.cirurgias

            def adicionar_tratamento(self, tratamento):
                self.tratamentos.append(tratamento)

            def atualizar_tratamento(self, tratamento_id, novos_dados):
                self.tratamentos[tratamento_id] = novos_dados

            def visualizar_tratamentos(self):
                return self.tratamentos

            def visualizar_pacientes(self):
                paciente = []

                for consulta in self.consulta:
                    if consulta.paciente not in paciente:
                        paciente.append(consulta.paciente)
                
                for consulta in self.cirurgia:
                    if Cirurgia.paciente not in paciente:
                        paciente.append(Cirurgia.paciente)
                        
                for tratamento in self.tratamento:
                    if tratamento.paciente not in paciente:
                        paciente.append(tratamento.paciente)
                return paciente
