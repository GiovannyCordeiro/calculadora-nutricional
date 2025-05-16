#Calculo do IMC( Indice de Massa corporal) Formula: peso divido pela altura ao quadrado. 
def calcular_imc(peso, altura):
    imc = peso/altura**2
    

#Classificação da OMS (Organização Mundial de saúde de acordo com o IMC)
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif 18.5 <= imc < 25:
        classificacao = "Peso normal"
    elif 25 <= imc < 30:
        classificacao = "Sobrepeso"
    elif 30 <= imc < 35:
        classificacao = "Obesidade grau 1"
    elif 35 <= imc < 40:
        classificacao = "Obesidade grau 2"
    else:
        classificacao = "Obesidade grau 3"

    return imc, classificacao



