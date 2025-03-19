def registrar_personas():
    
    personas = []


    cantidad = int(input("Ingrese la cantidad de personas a registrar: "))

    for i in range(cantidad):
        print(f"\nRegistrando persona {i+1}:")
        nombre = input("Ingrese el nombre: ")
        edad = int(input("Ingrese la edad: "))
        nota = float(input("Ingrese la nota: "))

        personas.append([nombre, edad, nota])

    return personas


def mostrar_resultados(personas):

    print("\nLista de personas ingresadas:")
    print("{:<20} {:<10} {:<5}".format("Nombre", "Edad", "Nota"))
    for persona in personas:
        print("{:<20} {:<10} {:<5}".format(persona[0], persona[1], persona[2]))

    personas_ordenadas = sorted(personas, key=lambda x: x[2], reverse=True)

    print("\nLista ordenada por nota (de mayor a menor):")
    print("{:<20} {:<10} {:<5}".format("Nombre", "Edad", "Nota"))
    for persona in personas_ordenadas:
        print("{:<20} {:<10} {:<5}".format(persona[0], persona[1], persona[2]))


def main():

    personas = registrar_personas()

    mostrar_resultados(personas)


if __name__ == "__main__":
    main()
