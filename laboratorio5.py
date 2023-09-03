peso = float(input("Ingresa tu peso (kg): "))
altura = float(input("Ingresa tu altura (m): "))

imc = peso / (altura ** 2)

if imc < 18.5:
        categoria = "Bajo peso"
elif imc < 25:
        categoria = "Peso normal"
elif imc < 30:
        categoria = "Sobrepeso"
else:
        categoria = "Obesidad"

print("Tu Índice de Masa Corporal (IMC) es:", imc)
print("Categoría:", categoria)

