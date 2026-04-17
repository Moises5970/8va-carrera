def solicitar_nombre():
    """
    se solicita el nombre y se verifica que no sea
    una entrada vacia no otro tipo de dato
    """
    while True:
        nombre = input('Ingresa tu nombre: ').strip()
        if not nombre:
            print("Error: le nombre no puede esta vacio")
        elif not  nombre.replace(" ", "").isalpha():
            print("Error: el nombre solo debe contener caracteres alfabeticos")
        else:
            return nombre


def solicitar_edad():
    """
    Se pide la edad y se verifica que no este vacia 
    y sea del tipo entero
    """
    while True:
        try:
            edad = int(input("Ingresa tu edad: "))
            if edad <= 0:
                print("Error: la edad debe ser mayor a 0")
            else:
                return edad
        except ValueError:
            print("Error: la edad debe ser un numero entero")


def solicitar_genero():
    """
    Se pide que se ingrese un genero, ya sea masculino
    o femenino (M/F)
    """
    while True:
        genero = input("Ingresa tu genero (M/F): ").upper().strip()
        if not (genero == "M" or genero == "F"):
            print("Genero inavlido\n")
        else:
            return genero
