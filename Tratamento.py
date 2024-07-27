class Tratamento:
    def __int__(self, tipo, descricao, custo, paciente, medico, enfermeiro, departamento):
        self.tipo = tipo
        self.descricao = descricao
        self.custo = custo
        self.paciente = paciente
        self.medico = medico
        self.enfermeiro = enfermeiro
        self.departamento = departamento
        self.observacoes = []

        def adicionar_observacao(self, observacao):
            self.observacoes.append(observacao)

        def atualizar_observacao(self, index, nova_observacao):
            if 0 <= index < len(self.observacoes):
                self.observacoes[index] = nova_observacao

        def visualizar_detalhes(self):
            return {
                "tipo": self.tipo,
                "descricao": self.descricao,
                "custo": self.custo,
                "paciente": self.paciente,
                "medico": self.medico,
                "enfermeiro": self.enfermeiro,
                "departamento": self.departamento,
                "observacoes": self.observacoes
            }
        
