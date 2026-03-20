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
            print("Errore, el nombre solo debe contener caracteres alfabeticos")
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
            print("Genero inavlido")
        else:
            return genero

def seleccionar_categoria():
    """
    imprimir categorias y recibir la selccecion del
    usuario
    """
    print('''
    1. Infantil - Preescolar (2 vueltas) — $50
    2. Primaria 1ro-3ro (3 vueltas) — $50
    3. Primaria 4to-6to (4 vueltas) — $50
    4. Secundaria (7 km) — $80
    5. Preparatoria (7 km) — $80
    6. Universitarios (7 km) — $80
    7. Empleados/Iglesia 22-39 (7 km) — $80
    8. Empleados/Iglesia 40-49 (7 km) — $80
    9. Empleados/Iglesia 50 y + (7 km) — $80
    ''')
    
    while True:
        try:
            cat = int(input("Ingresa tu categoria "))
            if 1 <= cat <= 9:
                return cat
        except ValueError:
            print("Error: Ingresa una opcion valida")

def asignar_costos(cat):
    """
    asignar el valor del costo de acuerdo con la 
    categoria ingresada
    """
    if cat == 1:
        costo = 50
    elif cat == 2:
        costo = 50
    elif cat == 3:
        costo = 50
    elif cat == 4:
        costo = 80
    elif cat == 5:
        costo = 80
    elif cat == 6:
        costo = 80
    elif cat == 7:
        costo = 80
    elif cat == 8:
        costo = 80
    elif cat == 9:
        costo = 80
    
    return costo

# medallas
def calcular_medallas(cant):
    """
    actualiza la cantidad de medallas y muestra si el
    particioante alcanzo o no medallas 
    """
    medallas = 99
    medallas += cant
    if medallas <= 100:
        return "Alcanzo medalla"
    else:
        return "Lo siento, no alcanzo medalla"

def seleccionar_promocion():
    """
    se pregunta la modalidad para aplicar la promocion
    y verificar que sea una de las dos opciones (I/P)
    """
    while True:
        cp = input('Individual o Pareja (I/P): ').upper()
        if not (cp == 'I' or cp == 'P'):
            print('Error: ingrese una opcion valida')
        else:
            return cp

def ejecutar_inscripcion():
    """
    funcion encagada de ejecutra las demas funciones y 
    porcesa la iformacion obtenida para impirmir
    datos de usuario, costos y estado de medallas
    """
    nombre1 = solicitar_nombre()
    edad1 = solicitar_edad()
    genero1 = solicitar_genero()
    cat1 = seleccionar_categoria()
    costo1 = asignar_costos(cat1)
    medalla1 = calcular_medallas(1)
    
    cp = seleccionar_promocion()
    
    if cp == "I":
        print(f'''
        Nombre: {nombre1}
        Edad: {edad1}
        Genero: {genero1}
        Categoria: {cat1}
        costo: {costo1}
        Medalla: {medalla1}
        ''')
        exit()
    elif cp == "P":
        nombre2 = solicitar_nombre()
        edad2 = solicitar_edad()
        genero2 = solicitar_genero()
        cat2 = seleccionar_categoria()
        costo2 = asignar_costos(cat2)
        medalla2 = calcular_medallas(1)
        if costo1 == costo2:
            total = 80 if (costo2 == 50) else 150
            
            print(f'''
            Nombre: {nombre1} | {nombre2}
            Edad: {edad1} | {edad2}
            Genero: {genero1} | {genero2}
            Categoria: {cat1} | {cat2}
            Costo: {total}
            Medalla: {medalla1} | {medalla2}
            ''')
        else:
            print("Los precios son diferentes, no es posible la inscripcion")
            exit()

# Iniciar el programa
if __name__ == "__main__":
    ejecutar_inscripcion()
