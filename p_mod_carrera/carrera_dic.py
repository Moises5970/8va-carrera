categorias = {
        1: {"nombre": "Infantil", "precio": 50, "dist": " 2 vueltas"},
        2: {"nombre": "Primaria 1ro-3ro", "precio": 50, "dist": "3 vueltas"},
        3: {"nombre": "Primaria 4to-6to", "precio": 50, "dist": "4 vueltas"},
        4: {"nombre": "Secundaria", "precio": 80, "dist": "7 km"},
        5: {"nombre": "Preparatoria", "precio": 80, "dist": "7 km"},
        6: {"nombre": "Universitarios", "precio": 80, "dist": "7 km"},
        7: {"nombre": "Empleados/Iglesia 22-39", "precio": 80, "dist": "7 km"},
        8: {"nombre": "Empleados/Iglesia 40-49", "precio": 80, "dist": "7 km"},
        9: {"nombre": "Empleados/Iglesia 50 y +", "precio": 80, "dist": "7 km"}
    }

medallas = 99

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

def seleccionar_categoria(categorias):
    """
    imprimir categorias y recibir la selccecion del
    usuario
    """
    for id, info in categorias.items():
        print(f"{id}. {info['nombre']} ({info['dist']}) — ${info['precio']}")
    
    while True:
        try:
            cat = int(input("Ingresa tu categoria "))
            if cat in categorias:
                return cat
        except ValueError:
            print("Error: Ingresa una opcion valida")

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

def calcular_medallas(cant):
    """
    actualiza la cantidad de medallas y muestra si el
    particioante alcanzo o no medallas 
    """
    global medallas
    medallas += cant
    if medallas <= 100:
        return "Alcanzo medalla"
    else:
        return "Lo siento, no alcanzo medalla"

def ejecutar_inscripcion():
    """
    funcion encagada de ejecutra las demas funciones y 
    porcesa la iformacion obtenida para impirmir
    datos de usuario, costos y estado de medallas
    """
    nombre1 = solicitar_nombre()
    edad1 = solicitar_edad()
    genero1 = solicitar_genero()
    cat1 = seleccionar_categoria(categorias)
    medalla1 = calcular_medallas(1)
    
    cp = seleccionar_promocion()
    
    #primera catergoria
    info_cat = categorias[cat1]
    
    #costo 1
    costo1 = info_cat["precio"]
    
    if cp == "I":
        print(f'''
        Nombre: {nombre1}
        Edad: {edad1}
        Genero: {genero1}
        Categoria: {cat1}
        Costo: {costo1}
        Medalla: {medalla1}
        ''')
        exit()
    elif cp == "P":
        nombre2 = solicitar_nombre()
        edad2 = solicitar_edad()
        genero2 = solicitar_genero()
        cat2 = seleccionar_categoria(categorias)
        medalla2 = calcular_medallas(1)
        
        #segundo catergoria
        info_cat2 = categorias[cat2]
        
        #costo 2
        costo2 = info_cat2["precio"]
        
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