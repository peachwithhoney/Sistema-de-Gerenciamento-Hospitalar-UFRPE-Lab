class Cirurgia:
    def __init__(self, tipo, descricao, data, hora, paciente, medico, enfermeiro, departamento, observacoes):
        self.tipo = tipo
        self.descricao = descricao
        self.data = data
        self.hora = hora
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
        else:
            print("Índice inválido.")

    def visualizar_detalhe(self):
        return {
            "tipo": self.tipo,
            "descricao": self.descricao,
            "data": self.data,
            "hora": self.hora,
            "paciente": self.paciente,
            "medico": self.medico,
            "enfermeiro": self.enfermeiro,
            "departamento": self.departamento,
            "observacoes": self.observacoes
        }	
    