'''punto 1'''
a1 = (5 + 5) * 5
b1 = 5 + (5 * 5)
c1 = 5 % 2
d1 = (5 - (6 / 3)) * 2
print("Los resultados de a1, b1, c1 y d1 son:", a1, b1, c1, d1)

'''punto 2'''
a2 = 7
b2 = 3

op1 = a2 != b2
op2 = a2 == b2
op3 = a2 > b2
op4 = (a2 + b2) < 2
op5 = ((a2 > 7) and (b2 == 3))
op6 = ((a2 < 7) or (b2 == 3))
op7 = ((a2 < 7) or (b2 != 3))

print("Los resultados de las 7 operaciones son:")
print(op1, op2, op3, op4, op5, op6, op7) 

'''punto 4'''
nota_taller1 = float(input("Ingrese la nota del Taller 1 (20%): "))
nota_taller2 = float(input("Ingrese la nota del Taller 2 (15%): "))
nota_cuestionario1 = float(input("Ingrese la nota del Cuestionario 1 (22%): "))
nota_cuestionario2 = float(input("Ingrese la nota del Cuestionario 2 (10%): "))
nota_proyecto_final = float(input("Ingrese la nota del Proyecto Final (33%): "))

nota_definitiva = (nota_taller1 * 0.20) + (nota_taller2 * 0.15) + (nota_cuestionario1 * 0.22) + (nota_cuestionario2 * 0.10) + (nota_proyecto_final * 0.33)

print(f"La nota definitiva del estudiante es: {nota_definitiva:.2f}")


'''punto 5'''

metros = float(input("Ingrese la cantidad de metros: "))
millas = metros / 1609.34  # 1 metro equivale a 0.000621371 millas
print(f"{metros} metros equivalen a {millas:.2f} millas.")

'''punto 6'''
salario_minimo_actual = float(input("Ingrese el salario mínimo actual: "))
incremento_porcentaje = 4.2 / 100  # Convertimos el incremento a porcentaje
nuevo_salario_minimo = salario_minimo_actual * (1 + incremento_porcentaje)
print(f"El nuevo salario mínimo para el próximo año será: {nuevo_salario_minimo:.2f}")

'''punto 7'''
pesos_colombianos = float(input("Ingrese la cantidad de pesos colombianos: "))
tasa_cambio_dolar = 3768.51  # Tasa de cambio actual de pesos colombianos a dólares
dolares = pesos_colombianos / tasa_cambio_dolar
print(f"{pesos_colombianos} pesos colombianos equivalen a {dolares:.2f} dólares.") 

