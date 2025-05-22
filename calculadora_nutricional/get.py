class GET:
    def __init__(self, tmb: int, nivel_atividade: int):
        self.tmb = tmb
        self.nivel_atividade = nivel_atividade

    def definir_nivel_atividade(self):
        match self.nivel_atividade:
            case 1:
                return 1.2
            case 2:
                return 1.375
            case 3:
                return 1.55
            case 4:
                return 1.725
            case 5:
                return 1.9
            case _:
                print("Opcao nao condiz, por favor tente novamente")
                return 0

    def calc(self) -> float:
        nivel_atividade = self.definir_nivel_atividade()
        return float(self.tmb) * nivel_atividade
