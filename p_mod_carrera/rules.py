def calcular_medallas(medallas, cant):
    """
    actualiza la cantidad de medallas y muestra si el
    particioante alcanzo o no medallas 
    """
    if medallas + cant <= 100:
        medallasNew = medallas + cant
        return "Alcanzo medalla", medallasNew
    else:
        return "Lo siento, no alcanzo medalla", medallas


def seleccionar_categoria(categorias):
    """
    imprimir categorias y recibir la selccecion del
    usuario
    """
    for id, info in categorias.items():
        print(f"{id}. {info['nombre']} ({info['dist']}) — ${info['precio']}")
    
    while True:
        try:
            cat = int(input("\nIngresa tu categoria: "))
            if cat in categorias:
                return cat
        except ValueError:
            print("Error: Ingresa una opcion valida\n")


def seleccionar_promocion():
    """
    se pregunta la modalidad para aplicar la promocion
    y verificar que sea una de las dos opciones (I/P)
    """
    while True:
        cp = input('Individual o Pareja (I/P): ').upper()
        if not (cp == 'I' or cp == 'P'):
            print('Error: ingrese una opcion valida\n')
        else:
            return cp