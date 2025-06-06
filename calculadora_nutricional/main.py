from .imc import calcular_imc, salvar_historico_peso, exibir_historico_peso
from .tmb import TMB

def menu():
    while True:
        print("\nCalculadora Nutricional")
        print("1. Calcular IMC")
        print("2. Calcular TMB")
        print("3. Calcular GET")
        print("4. Exibir Histórico de Pesos")
        print("5. Sair")

        opcao = input("Escolha o número correspondente a opção que deseja executar: ")

        if opcao == "1":
            try:
                peso = float(input("Digite seu peso (kg): "))
                altura = float(input("Digite sua altura (Ex.: 1.75): "))
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
            try:
                peso = int(input("Digite seu peso (kg): "))
                altura = int(input("Digite sua altura (cm): "))
                idade = int(input("Digite sua idade (anos): "))
                genero = input("Digite seu gênero (Ex.: male/female): ")
                tmb = TMB(peso, altura, idade)
                valor_tmb = tmb.calc(genero)

                print("\nNíveis de atividade física:")
                print("1. Sedentário (pouco ou nenhum exercício)")
                print("2. Levemente ativo (exercício leve 1 a 3 dias/semana)")
                print("3. Moderadamente ativo (exercício moderado 3 a 5 dias/semana)")
                print("4. Muito ativo (exercício pesado 6 a 7 dias/semana)")
                print("5. Extremamente ativo (exercício muito intenso ou trabalho físico pesado)")

                nivel = input("Escolha o nível de atividade (1-5): ")
                fatores = {
                    "1": 1.2,
                    "2": 1.375,
                    "3": 1.55,
                    "4": 1.725,
                    "5": 1.9
                }

                fator = fatores.get(nivel)
                if fator:
                    get = valor_tmb * fator
                    print(f"Seu Gasto Energético Total (GET) é: {get:.2f} kcal")
                else:
                    print("Nível de atividade inválido.")
            except Exception as e:
                print("Erro ao calcular GET. Verifique os dados inseridos.")


        elif opcao == "4":
            exibir_historico_peso()

        elif opcao == "5":
            print("Sessão Encerrda.")
            break
        
        else:
            print("Opção inválida. Por favor, escolha um número entre 1 e 5.")

if __name__ == "__main__":
            menu()


