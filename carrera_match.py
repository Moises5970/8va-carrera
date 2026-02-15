#datos
nombre = input("Ingresa tu nombre: ")
if not nombre:
  print("Error: el nombre no puede estar vacio.")
  exit()

try:
  edad = int(input("Ingresa tu edad: "))
  if not edad:
    print("Error: la edad no puede estar vacia.")
    exit()
except:
  print("Error: la edad debe ser un numero.")
  exit()

genero = input("Genero (M/F): ").upper()
if not (genero == 'M' or genero == 'F'):
  print("Error: genero invalido.")
  exit()

#medallas
medallas = 99
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
    cat = int(input("Ingresa tu categoria "))
    if cat < 1 or cat > 9:
        print('Error: categoria invalida')
        exit()
except ValueError:
    print('Error: debe ser un numero entero.')
    exit()
    
#costo
costo = 0
costoii = 0

# costo
match cat:
    case 1 | 2 | 3:
        costo = 50
    case 4 | 5 | 6 | 7 | 8 | 9:
        costo = 80

#Costos y promociones
cp = input('Individual o Pareja (I/P): ').upper()
if not (cp == 'I' or cp == 'P'):
    print('Error: ingrese una opcion valida')
    exit()

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
        exit()
    case 'P':
        nombreii = input("Nombre del segundo corredor: ").strip()
        if not nombreii: 
            print("Error: nombre vacío"); exit()
        
        try:
            edadii = int(input("Ingresa tu edad: "))
            if not edadii:
                print("Error: la edad no puede estar vacia.")
                exit()
        except:
            print("Error: la edad debe ser un numero.")
            exit()
        
        generoii = input("Genero (M/F): ").upper()
        if not (generoii == 'M' or generoii == 'F'):
            print("Error: genero invalido.")
            exit()
            
        try:
            catii = int(input("Categoría del segundo corredor: "))
        except:
            print("Error: debe ser número"); exit()

        # Determinamos costo del corredor 2 con MATCH
        match catii:
            case 1 | 2 | 3:
                costoii = 50
            case 4 | 5 | 6 | 7 | 8 | 9:
                costoii = 80
            case _:
                print("Categoría no válida"); exit()

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
            exit()
        else:
            print("Error: Las categorías tienen precios distintos.")