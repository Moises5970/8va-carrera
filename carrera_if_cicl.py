medallas = 99
continuar = True
corredores = 0

while continuar:
    nombre = input("Ingresa tu nombre: ")
    if nombre:
        edad = int(input("Ingresa tu edad: "))
        if edad:
            genero = input("Genero (M/F): ").upper()
            if (genero == 'M' or genero == 'F'):
                #categorias
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
                
                try:
                    cat = int(input("Ingresa tu categoria: "))
                    if 1 <= cat <= 9:
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
                            
                        corredores += 1
                        medallas += 1
                        
                        corr1 = corredores
                        
                        if medallas <= 100:
                            cant = "Alcanzo medalla"
                        else:
                            cant = 'Lo siento'
                            
                        #Costos y promociones
                        cp = input('Individual o Pareja (I/P): ').upper()
                        if cp == "I":
                            
                            print(f'''
                            Nombre: {nombre}
                            Edad: {edad}
                            Genero: {genero}
                            Categoria: {cat}
                            costo: {costo}
                            numero: {corr1}
                            {cant}
                            ''')
                            
                        elif cp == "P":
                            nombreii = input("Ingresa el segundo nombre: ")
                            if nombreii:
                                try:
                                    edadii = int(input("Ingresa la segunda edad: "))
                                    if edadii:
                                        generoii = input("Genero (M/F): ").upper()
                                        if (genero == 'M' or genero == 'F'):
                                            try:
                                                catii = int(input("Ingresa la segunda categoria "))
                                                
                                                if  1 <= catii <= 9:
                                                    if catii == 1:
                                                        costoii = 50
                                                    elif catii == 2:
                                                        costoii = 50
                                                    elif catii == 3:
                                                        costoii = 50
                                                    elif catii == 4:
                                                        costoii = 80
                                                    elif catii == 5:
                                                        costoii = 80
                                                    elif catii == 6:
                                                        costoii = 80
                                                    elif catii == 7:
                                                        costoii = 80
                                                    elif catii == 8:
                                                        costoii = 80
                                                    elif catii == 9:
                                                        costoii = 80
                                                        
                                                    if costo == costoii:
                                                        total= 80 if (costo == 50 and costoii == 50) else 150
                                                        
                                                        corredores += 1
                                                        corr2 = corredores
                                                        medallas += 1
                                                        
                                                        if medallas <= 100:
                                                            cant2 = "Alcanzo medalla"
                                                        else:
                                                            cant2 = 'Lo siento'
                                                        
                                                        print(f'''
                                                        Nombre: {nombre} | {nombreii}
                                                        Edad: {edad} | {edadii}
                                                        Genero: {genero} | {generoii}
                                                        Categoria: {cat} | {catii}
                                                        costo: {total}
                                                        Numeros: {corr1} | {corr2}
                                                        Medalla: 
                                                            {nombre} {cant}
                                                            {nombreii} {cant2}
                                                        ''')
                                                    else:
                                                        print('Error: los precios son diferentes')
                                                else:
                                                    print("Error: categoria inavlida")
                                            except:
                                                print("Error: debe ser un numero entero y no estra vacio")
                                        else:
                                            print("Error: genero vacio.")
                                except:
                                    print("Error: la edad debe ser un numero y no debe estar vacia.")
                            else:
                                print("Error: el nombre no puede estar vacio")
                    else:
                        print("Error: categoria invalida")
                except:
                    print("Error: categoria vacia")
            else:
                print("Error: genero invalido.")
        else:
            print("Error: La edad debe ser entero y no estra vacia")
    else:
        print("Error: el nombre no puede estar vacio")
    
    decicion = input("¿Quieres seguir inscibiendo? (Y/N)").upper()
    if decicion == "N":
        continuar = False
        print("Gracias por tu trabajo")
