from imc import calcular_imc, salvar_historico, exibir_historico
from tmb import TMB

def menu():
    while True:
        print("\nCalculadora Nutriconal")
        print("1. Calcular IMC")
        print("2. Calcular TMB")
        print("3. Calcular GET")
        print("4. Exibir Histórico de Pesos")
        print("5. Sair")

        opcao = input("Escolha o número correspondente a opção que deseja executar: ")
