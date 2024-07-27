class Departamento:
    def __init__(self, nome, localizacao):
        self.nome = nome
        self.localizacao = localizacao
        self.medico = []
        self.enfermeiro = []
        self.consulta = []
        self.procedimento = []
        self.recurso_equipamento = []

    def adicionar_medico(self, medico):
        if medico not in self.medico:
            self.medico.append(medico)
            medico.departamento = self

    def remover_medico(self, medico):
        if medico in self.medico:
            self.medico.remove(medico)
            medico.departamento = None

    def listar_medicos(self):
        return [medico.nome for medico in self.medico]
    
    def adicionar_enfermeiro(self, enfermeiro):
        if enfermeiro not in self.enfermeiro:
            self.enfermeiro.append(enfermeiro)
            enfermeiro.departamento = self

    def remover_enfermeiro(self, enfermeiro):
        if enfermeiro in self.enfermeiro:
            self.enfermeiro.remove(enfermeiro)
            enfermeiro.departamento = None

    def listar_enfermeiros(self):
        return [enfermeiro.nome for enfermeiro in self.enfermeiro]
    
    def adicionar_consulta(self, consulta):
        if consulta not in self.consulta:
            self.consulta.append(consulta)
            consulta.departamento = self

    def listar_consultas(self):
        return [consulta.data for consulta in self.consulta]
    
    def adicionar_procedimento(self, procedimento):
        if procedimento not in self.procedimento:
            self.procedimento.append(procedimento)
            procedimento.departamento = self

    def listar_procedimentos(self):
        return [procedimento.nome for procedimento in self.procedimento]
    
    def adicionar_recurso_equipamento(self, recurso_equipamento):
        if recurso_equipamento not in self.recurso_equipamento:
            self.recurso_equipamento.append(recurso_equipamento)
            recurso_equipamento.departamento = self

    