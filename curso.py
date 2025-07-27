altura = float(input('Digite a altura: '))
peso = float(input('Digite a peso: '))
imc = peso / (altura * altura)
if imc < 18.5:
    print('Você está abaixo do peso!')
elif imc <= 24.9:
    print('Peso ideal!')
elif imc <= 29.9:
    print('Sobrepeso!')
elif imc <= 34.9:
    print('Obesidade grau 1')
elif imc <= 39.9:
    print('Obesidade grau 2')
elif imc >= 40:
    print('Obesidade grau 3')
