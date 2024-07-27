class Especialidade:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao
        self.medico = []
        self.consulta = []
        self.tratamento = []

    def __str__(self):
        return f"{self.nome} - {self.descricao}"
    
    def adicionar_medico(self, medico):
        if medico not in self.medico:
            self.medico.append(medico)
            medico.especialidade = self

    def remover_medico(self, medico):
        if medico in self.medico:
            self.medico.remove(medico)
            medico.especialidade = None

    def listar_medicos(self):
        return [medico.nome for medico in self.medico]
    
    def adicionar_consulta(self, consulta):
        if consulta not in self.consulta:
            self.consulta.append(consulta)
            consulta.especialidade = self

    def listar_consultas(self):
        return [consulta.data for consulta in self.consulta]
    
    def adicionar_tratamento(self, tratamento):
        if tratamento not in self.tratamento:
            self.tratamento.append(tratamento)
            tratamento.especialidade = self

    def listar_tratamentos(self):
        return [tratamento.nome for tratamento in self.tratamento]
    
    