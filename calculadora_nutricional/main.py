from imc import calcular_imc, salvar_historico_peso, exibir_historico
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

        if opcao == "1":
            try:
                peso = float(input("Digite seu peso (kg): "))
                altura = float(input("Digite sua altura (m): "))
                imc, classificacao = calcular_imc(peso, altura)
                print(f"Seu IMC é: {imc:.2f} - {classificacao}")
                salvar_historico_peso(peso)
            except ValueError:
                print("Entrada inválida. Use números válidos.")
