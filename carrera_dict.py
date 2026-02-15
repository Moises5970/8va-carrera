#datos
nombre1 = input("Ingresa tu nombre: ")
if not nombre1:
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

try:
    cat = int(input("Ingresa tu categoria "))
    if cat not in categorias:
        print('Error: categoria invalida')
        exit()
except ValueError:
    print('Error: debe ser un numero entero.')
    exit()

#Costos y promociones
cp = input('Individual o Pareja (I/P): ').upper()
if not (cp == 'I' or cp == 'P'):
    print('Error: ingrese una opcion valida')
    exit()

#primera catergoria
info_cat = categorias[cat]

#costo 1
costo = info_cat["precio"]

#match case
match cp:
    case "I":
        medallas += 1
        cor1 = medallas
        status = "¡Ganada!" if cor1 <= 100 else "Agotada"
        print(f'''
          Nombre: {nombre1}
          Edad: {edad}
          Genero: {genero}
          Categoria: {info_cat["nombre"]}
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

        #segunda categoria
        info_cat2 = categorias[catii]
        
        #costo 1
        costoii = info_cat2["precio"]

        # Regla de Parejas
        if costo == costoii:
            total= 80 if costo == 50 else 150
        
            medallas += 1
            cor1 = medallas
            medallas += 1
            cor2 = medallas
            
            status1 = "¡Ganada!" if cor1 <= 100 else "Agotada"
            status2 = "¡Ganada!" if cor2 <= 100 else "Agotada"
            
            print(f'''
            Nombre: {nombre1} | {nombreii}
            Edad: {edad} | {edadii}
            Genero: {genero} | {generoii}
            Categoria: {info_cat["nombre"]} | {info_cat2["nombre"]}
            costo: {total}
            Medalla: 
                {nombre1} {status1}
                {nombreii} {status2}
            ''')
            exit()
        else:
            print("Error: Las categorías tienen precios distintos.")