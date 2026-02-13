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

#Costos y promociones
cp = input('Individual o Pareja (I/P): ').upper()
if not (cp == 'I' or cp == 'P'):
    print('Error: ingrese una opcion valida')
    exit()

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


#caso de pareja
if cp == 'I':        
    #medallas
    if medallas < 100:
        print('Alcanzo medalla')
        medallas + 1
        
    print(f'''
          Nombre: {nombre}
          Edad: {edad}
          Genero: {genero}
          Categoria: {cat}
          costo: {costo}
          ''')
    exit()
elif cp == 'P':
    corr1 = medallas + 1
    nombreii = input('Ingresa el segundo nombre: ')
    if not nombreii:
        print("Error: el nombre no puede estar vacio.")
        exit()
    
    try:
        edadii = int(input("Ingresa la segunda edad: "))
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
    
    catii = int(input('Ingresa la segunda categoria: '))
    if not catii:
        print('Error: la categoria no puede estar vacio.')
        exit()
    
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
    
    #comparacion de precios
    if costo == costoii:
        total= 80 if (costo == 50 and costoii) == 50 else 150
        
        corr2 = medallas + 1
        
        print(f'''
          Nombre: {nombre} | {nombreii}
          Edad: {edad} | {edadii}
          Genero: {genero} | {generoii}
          Categoria: {cat} | {catii}
          costo: {total}
          ''')
        
        if corr1 <= 100:
            print(f'{nombre} Alcanzo medalla')
        else:
            print(f'{nombre} Lo siento, ya no alcanzate')
            
        if corr2 <= 100:
            print(f'{nombreii} Alcanzo medalla')
        else:
            print(f'{nombreii} Lo siento, ya no alcanzate')
        
        exit()
    else:
        print('Error: no se puede procesar por difrencia de precio.')
        exit()