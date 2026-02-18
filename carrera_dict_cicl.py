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

#medallas
medallas = 99
corredores = 1

while corredores <= 3:
    # datos
    nombre = input("Ingresa tu nombre: ")
    if nombre:
        try:
            edad = int(input("Ingresa tu edad: "))
            if edad:
                genero = input("Genero (M/F): ").upper()
                if (genero == 'M' or genero == 'F'):
                    try:
                        print("--- Categorías Disponibles ---")
                        for id, info in categorias.items():
                            print(f"{id}. {info['nombre']} ({info['dist']}) — ${info['precio']}")
                        cat = int(input("Ingresa tu categoria "))
                        if cat in categorias:
                            cp = input('Individual o Pareja (I/P): ').upper()
                            
                            corredores += 1
                            medallas += 1
                            
                            corr1 = corredores - 1
                            
                            if medallas <= 100:
                                cant = "Alcanzo medalla"
                            else:
                                cant = 'Lo siento'
                            
                            match cp:
                                case 'I':
                                    medallas += 1
                                    cor1 = medallas
                                    
                                    #primera catergoria
                                    info_cat = categorias[cat]

                                    #costo 1
                                    costo = info_cat["precio"]
                                    
                                    print(f'''
                                    Nombre: {nombre}
                                    Edad: {edad}
                                    Genero: {genero}
                                    Categoria: {info_cat["nombre"]}
                                    costo: {costo}
                                    Numero: {corr1}
                                    Medalla: {cant}
                                    ''')
                                case 'P':
                                    nombreii = input("Ingresa el segundo nombre: ")
                                    if nombreii:
                                        try:
                                            edadii = int(input("Ingresa tu edad: "))
                                            if edadii:
                                                generoii = input("Genero (M/F): ").upper()
                                                if (generoii == 'M' or generoii == 'F'):
                                                    try:
                                                        catii = int(input("Ingresa tu categoria "))
                                                        if catii in categorias:
                                                            #primera catergoria
                                                            info_cat = categorias[cat]
                                                            
                                                            #costo 1
                                                            costo = info_cat["precio"]
                                                            
                                                            #segunda categoria
                                                            info_cat2 = categorias[catii]
                                                            
                                                            #costo 2
                                                            costoii = info_cat2["precio"]
                                                            
                                                            # Regla de Parejas
                                                            if costo == costoii:
                                                                total= 80 if costo == 50 else 150
                                                            
                                                                corredores += 1
                                                                corr2 = corredores - 1
                                                                medallas += 1
                                                                
                                                                if medallas <= 100:
                                                                    cant2 = "Alcanzo medalla"
                                                                else:
                                                                    cant2 = 'Lo siento'
                                                                
                                                                print(f'''
                                                                Nombre: {nombre} | {nombreii}
                                                                Edad: {edad} | {edadii}
                                                                Genero: {genero} | {generoii}
                                                                Categoria: {info_cat["nombre"]} | {info_cat2["nombre"]}
                                                                costo: {total}
                                                                Numero: {corr1} | {corr2}
                                                                Medalla: 
                                                                    {nombre} {cant}
                                                                    {nombreii} {cant2}
                                                                ''')
                                                            else:
                                                                print("Error: Las categorías tienen precios distintos.")
                                                        else:
                                                            print("Error: la categoria no debe estar vacio")
                                                    except:
                                                        print("Error: debe ser un numero entero")
                                                else:
                                                    print("Error: genero invalido")
                                            else:
                                                print("Error: la edad no debe estar vacio")
                                        except:
                                            print("Error: la edad no debe estar vacio")
                                    else:
                                        print("Error: el nombre no debe estar vacio") 
                        else:
                            print("Error: la categoria no debe estar vacio")
                    except:
                        print("Error: debe ser un numero entero")
                else:
                    print("Error: genero invalido")
            else:
                print("Error: la edad no debe estar vacio")
        except:
            print("Error: la edad no debe estar vacio")
    else:
        print("Error: el nombre no debe estar vacio")
