from info import categorias, medallas
from inputs import solicitar_nombre, solicitar_edad, solicitar_genero
from rules import calcular_medallas, seleccionar_categoria, seleccionar_promocion


def ejecutar_inscripcion():
    """
    funcion encagada de ejecutra las demas funciones y 
    porcesa la iformacion obtenida para impirmir
    datos de usuario, costos y estado de medallas
    """
    med = medallas
    
    print("¡¡¡BIENVENIDO A LA INSCRIPCION DE LA CARRERA DE LAS ESTRELLAS!!!\n")
    
    nombre1 = solicitar_nombre()
    edad1 = solicitar_edad()
    genero1 = solicitar_genero()
    cat1 = seleccionar_categoria(categorias)
    mensaje1, med = calcular_medallas(med,1)
    
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
        Medalla: {mensaje1}
        ''')
        exit()
    elif cp == "P":
        nombre2 = solicitar_nombre()
        edad2 = solicitar_edad()
        genero2 = solicitar_genero()
        cat2 = seleccionar_categoria(categorias)
        mensaje2, med = calcular_medallas(med,1)
        
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
            Medalla: {mensaje1} | {mensaje2}
            ''')
        else:
            print("Los precios son diferentes, no es posible la inscripcion")
            exit()


ejecutar_inscripcion()