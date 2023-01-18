print(" --calculadora de masa corporal--")
print()
nombre = nombre =input("Por Favor ingrese su nombre y apellido: ")
edad =int(input("Por Favor ingrese su edad: "))
sexo = input("ingrese su sexo 'Masculino o Femenino': ")
peso = float(input("Favor ingrese su peso (expresado en KG 'ejemplo 70.5'): "))
estatura = float(input("Ingrese su estatura (expresado en CM 'ejemplo 1.70'): "))

IMC =  peso / (estatura * estatura)


if IMC < 18.5:
  print(f"Hola {nombre}; edad: {edad} anios, sexo: {sexo}, tienes un IMC de: ", round(IMC))
  print(f"CUIDADO!!! {nombre}: estas bajo de peso, debes comer mas!")
elif IMC >= 18.5 and IMC <= 24.9999:
  print(f"Hola {nombre}; edad: {edad} anios, sexo: {sexo}, tienes un IMC de: ", round(IMC))
  print(f"{nombre}: estas normal, FELICIDADES!!!")
elif IMC >= 25 and IMC <= 29.9999:
  print(f"Hola {nombre}; edad: {edad} anios, sexo: {sexo}, tienes un IMC de: ", round(IMC))
  print(f"{nombre}: estas con sobrepeso.")
elif IMC >= 30 and IMC <= 34.9999:
  print(f"Hola {nombre}; edad: {edad} anios, sexo: {sexo}, tienes un IMC de: ", round(IMC))
  print(f"{nombre}: estas con Obesidad moderada grado I.")
elif IMC >= 35 and IMC <= 39.9999:
  print(f"Hola {nombre}; edad: {edad} anios, sexo: {sexo}, tienes un IMC de: ", round(IMC))
  print(f"{nombre}: estas con Obesidad severa grado II.")
elif IMC > 40:
  print(f"Hola {nombre};  edad: {edad} anios, sexo: {sexo}, tienes un IMC de: ", round(IMC))
  print(f"{nombre}: estas con Obesidad critica grado III.")