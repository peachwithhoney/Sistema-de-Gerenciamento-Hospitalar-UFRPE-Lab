class Ponto:
    def __int__(self, funcionario, entrada_saida, horario):
        self.funcionario = funcionario
        self.entrada_saida = entrada_saida
        self.horario = horario

        def __str__(self):
            return f"{self.funcionario} - {self.entrada_saida} - {self.horario}"
        
        def visualizar_detalhes(self):
            return {
                "funcionario": self.funcionario,
                "entrada_saida": self.entrada_saida,
                "horario": self.horario
            }	