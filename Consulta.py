class Consulta:
    def __init__(self, data, hora, motivo, observacao, paciente, medico, departamento):
        self.data = data
        self.hora = hora
        self.motivo = motivo
        self.observacao = observacao
        self.paciente = paciente
        self.medico = medico
        self.departamento = departamento
        self.tratamento = []

        def atualizar_observacao(self, nova_observacao):
            self.observacao = nova_observacao

        def visualizar_detalhe(self):
            return {
                "data": self.data,
                "hora": self.hora,
                "motivo": self.motivo,
                "observacao": self.observacao,
                "paciente": self.paciente.nome,
                "medico": self.medico.nome,
                "departamento": self.departamento.nome,
            }
        
         
