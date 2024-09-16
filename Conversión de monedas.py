def convertir_monedas():
    tasa_cambio = 19.20
    while True:
        opcion = input("""¿Qué quieres convertir?
1. Pesos a Dólares  
2. Dólares a Pesos
""")
        if opcion == '1':
            pesos = float(input("Introduce la cantidad de pesos: "))
            dolares = pesos / tasa_cambio
            print(f"{pesos} pesos equivalen a {dolares:.2f} dólares.")
        elif opcion == '2':
            dolares = float(input("Introduce la cantidad de dólares: "))
            pesos = dolares * tasa_cambio
            print(f"{dolares} dólares equivalen a {pesos:.2f} pesos.")
        else:
            print("Opción inválida.")
        otra = input("¿Quieres hacer otra conversión? (s/n): ").lower()
        if otra != 's':
            print("Gracias por usar el convertidor de monedas. ¡Adiós!")
            break
convertir_monedas()
