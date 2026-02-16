#datos
nombre = input("Ingresa tu nombre: ")
if nombre:
    try:
        edad = int(input("Ingresa tu edad: "))
        if edad:
            genero = input("Genero (M/F): ").upper()
            if not (genero == 'M' or genero == 'F'):
                print("Error: genero invalido.")
    except:
        print("Error: la edad debe ser un numero y no debe estar vacia.")
else:
    print("Error: le nombre no puede etar vacio")

#medallas
medallas = 99

#costo
costo = 0
costoii = 0

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

cat = int(input("Ingresa tu categoria "))

if 1 <= cat <= 9:
    # costo
    match cat:
        case 1 | 2 | 3:
            costo = 50
        case 4 | 5 | 6 | 7 | 8 | 9:
            costo = 80

    #Costos y promociones
    cp = input('Individual o Pareja (I/P): ').upper()
    if  (cp == 'I' or cp == 'P'):
        try:

                #match case
            match cp:
                case "I":
                        cor1 = medallas + 1
                        status = "¡Ganada!" if cor1 <= 100 else "Agotada"
                        print(f'''
                        Nombre: {nombre}
                        Edad: {edad}
                        Genero: {genero}
                        Categoria: {cat}
                        costo: {costo}
                        Medalla: {status}
                        ''')
                case 'P':
                
                    #datos
                    nombreii = input("Ingresa tu nombre: ")
                    if nombreii:
                        try:
                            edadii = int(input("Ingresa tu edad: "))
                            if edadii:
                                generoii = input("Genero (M/F): ").upper()
                                if (generoii == 'M' or generoii == 'F'):
                                    
                                    try:
                                        catii = int(input("Ingresa la segunda categoria "))
                                    except:
                                        print("Error: debe ser un numero entero y no estra vacio")
                                    
                                    if  1 <= catii <= 9:
                                        # Determinamos costo del corredor 2 con MATCH
                                        match catii:
                                            case 1 | 2 | 3:
                                                costoii = 50
                                            case 4 | 5 | 6 | 7 | 8 | 9:
                                                costoii = 80

                                        # Regla de Parejas
                                        if costo == costoii:
                                            total= 80 if (costo == 50 and costoii == 50) else 150
                                        
                                            medallas += 1
                                            cor1 = medallas
                                            medallas += 1
                                            cor2 = medallas
                                            
                                            status1 = "¡Ganada!" if cor1 <= 100 else "Agotada"
                                            status2 = "¡Ganada!" if cor2 <= 100 else "Agotada"
                                            
                                            print(f'''
                                            Nombre: {nombre} | {nombreii}
                                            Edad: {edad} | {edadii}
                                            Genero: {genero} | {generoii}
                                            Categoria: {cat} | {catii}
                                            costo: {total}
                                            Medalla: 
                                                {nombre} {status1}
                                                {nombreii} {status2}
                                            ''')
                                        else:
                                            print("Error: categoria invalida")
                                    else:
                                        print("Error: Las categorías tienen precios distintos.")
                                else:
                                    print("Error: genero invalido.")
                        except:
                            print("Error: la edad debe ser un numero y no debe estar vacia.")
                    else:
                        print("Error: le nombre no puede etar vacio")
        except:
            print('Error.')
    else:
        print('Error: eleccion invaida')
else:
    print("Error: categoria inavlida")