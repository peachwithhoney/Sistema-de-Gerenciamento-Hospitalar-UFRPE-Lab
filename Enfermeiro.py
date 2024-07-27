class Enfermeiro:
    def __init__(self, nome, COFEN, telefone, especialidade, departamento):
        self.nome = nome
        self.COFEN = COFEN
        self.telefone = telefone
        self.especialidade = especialidade
        self.departamento = departamento
        self.consulta = []
        self.procedimento = []
        self.ponto = []
        self.paciente = []
        self.feedback = []

        def adicionar_paciente(self, paciente):
            if paciente not in self.paciente:
                self.paciente.append(paciente)
                paciente.enfermeiro = self

        def remover_paciente(self, paciente):
            if paciente in self.paciente:
                self.paciente.remove(paciente)
                paciente.enfermeiro = None

        def atualizar_paciente(self, paciente_id, novo_dado):
            for paciente in self.paciente:
                if paciente.id == paciente_id:
                    paciente.atualizar_dados(novo_dado)
        
        def visualizar_paciente(self, paciente_id):
            for paciente in self.paciente:
                if paciente.id == paciente_id:
                    return paciente.visualizar_dados()
                
        def registrar_observacao(self, paciente_id, observacao):
            for paciente in self.paciente:
                if not hasattr(paciente, 'observacao'):
                    paciente.observacao = []
                paciente.observacao.append(observacao)

        def administrar_tratamento(Self, paciente_id, tratamento):
            paciente = self.paciente[paciente_id]
            if not hasattr(paciente, 'tratamento'):
                paciente.tratamento = []
            paciente.tratamento.append(tratamento)

        def registrar_consulta(self, consulta):
            self.consulta.append(consulta)

        def atualizar_consulta(self, consulta_id, novo_dado):
            for consulta in self.consulta:
                if consulta.id == consulta_id:
                    consulta.atualizar_dados(novo_dado)

        def visualizar_consulta(self, consulta_id):
            for consulta in self.consulta:
                if consulta.id == consulta_id:
                    return consulta.visualizar_dados()
                
        def registrar_procedimento(self, procedimento):
            self.procedimento.append(procedimento)

        def atualizar_procedimento(self, procedimento_id, novo_dado):
            self.procedimento[procedimento_id] = novo_dado

        def visualizar_procedimento(self, procedimento_id):
            return self.procedimento[procedimento_id]
        
        def registrar_ponto(self, entrada_saida, horario):
            self.ponto.append({"entrada_saida": entrada_saida, "horario": horario})

        def visualizar_ponto(self):
            return self.ponto
        
        def fornecer_feedback(self, feedback):
            self.feedback.append(feedback)