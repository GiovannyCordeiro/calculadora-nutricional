from imc import calcular_imc, salvar_historico_peso, exibir_historico_peso
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


        elif opcao == "2":
            try:
                peso = int(input("Digite seu peso (kg): "))
                altura = int(input("Digite sua altura (cm): "))
                idade = int(input("Digite sua idade (anos): "))
                genero = input("Digite seu gênero (Ex.: male/female): ")
                tmb = TMB(peso, altura, idade)
                resultado = tmb.calc(genero)
                print(f"Seu TMB é: {resultado} kcal")
            except Exception as e:
                print("Erro ao calcular TMB. Verifique se os dados estão corretos.")

        elif opcao == "3":
            print("Função de cálculo do GET ainda não implementada.")

        elif opcao == "4":
            exibir_historico_peso()

        elif opcao == "5":
            print("Sessão Encerrda.")
            break

        if __name__ == "__main__":
            menu()


