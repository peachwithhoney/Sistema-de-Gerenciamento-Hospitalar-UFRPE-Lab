class Feedback:
    def __init__(self, comentario, avaliacao, paciente, medico=None, enfermeiro=None):
        self.comentario = comentario
        self.avaliacao = avaliacao
        self.paciente = paciente
        self.medico = medico
        self.enfermeiro = enfermeiro

        def __str__(self):
            return f"Comentário: {self.comentario}\nAvaliação: {self.avaliacao}\nPaciente: {self.paciente}\nMédico: {self.medico}\nEnfermeiro: {self.enfermeiro}"
        
        def visualizar_detalhes(self):
            detalhes = {
                "Comentário": self.comentario,
                "Avaliação": self.avaliacao,
                "Paciente": self.paciente,
            }
            if self.medico:
                detalhes["Médico"] = self.nome
            elif self.enfermeiro:
                detalhes["Enfermeiro"] = self.enfermeiro.nome
            return detalhes