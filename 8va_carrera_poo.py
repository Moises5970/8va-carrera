# persona
class Persona:
    def __init__(self, numero = None, nombre = None, edad = None, genero = None, categoria = None):
        self.numero = numero
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.categoria = categoria
        
    def verificar_nombre(self, nombre):
        if not nombre.replace(" ", "").isalpha():
            raise ValueError("Nombre invalido.")
        return nombre
    
    def verificar_edad(self, edad):
        if not edad.isdigit():
            raise ValueError("Edad invalida.")
        return edad
    
    def verificar_genero(self, genero):
        if not (genero == "M" or genero == "F"):
            raise ValueError("Genero invalido.")
        return genero


# categoria
class Categoria:
    def __init__(self, numero, nombre, precio, distancia):
        self.numero = numero
        self.nombre = nombre
        self.precio = precio
        self.distancia = distancia


class Sistema:
    def __init__(self):
        self.medallas = 99
        self.categorias = [
            Categoria(1, "Infantil", 50, " 2 vueltas" ),
            Categoria(2, "Primaria 1ro-3ro", 50, "3 vueltas"),
            Categoria(3, "Primaria 4to-6to", 50, "4 vueltas"),
            Categoria(4, "Secundaria", 80, "7 km"),
            Categoria(5, "Preparatoria", 80, "7 km"),
            Categoria(6, "Universitarios", 80, "7 km"),
            Categoria(7, "Empleados/Iglesia 22-39", 80, "7 km"),
            Categoria(8, "Empleados/Iglesia 40-49", 80, "7 km"),
            Categoria(9, "Empleados/Iglesia 50 y +", 80, "7 km")
        ]
        self.cantidad = 99
        self.inscritos = []
        
    def mostrar_categorias(self):
        print("\nCategorias disponibles:")
        for cat in self.categorias:
            print(f'{cat.numero}.{cat.nombre} - {cat.precio} ({cat.distancia})')
    
    def actalizar_medallas(self):
        self.medallas += 1
        if self.medallas <= 100:
            return ("Alcanzo medalla.")
        else:
            return ("No alcanzo medalla.")
    
    def obtener_categoria(self, catSel):
        for cat in self.categorias:
            if cat.numero == catSel:
                return cat
        return None
    
    def guradar_persona(self, object):
        self.inscritos.append(object)
        return self.cantidad
    
    def obterner_personas(self):
        for data in self.inscritos:
            print(f'numero: {data.numero}, nombre: {data.nombre}, edad: {data.edad}, genero: {data.genero}, categoria: {data.categoria}')
    
    def conteo(self):
        self.cantidad += 1
        return self.cantidad


# metodo principal
def main():
    
    continuar1 = True
    sistema = Sistema()
    datos = Persona()
    
    print("----- Bienvenido a la inscripcion de la 8va carrera -----")
    
    while continuar1:
        while True:
            try:
                opcion = int(input('''
            Seleciona una opcion:
            1. Individual
            2. Pareja
            3. Mostrar inscritos
            4. Salir
            '''))
                if opcion in [1, 2, 3, 4]:
                    break
                else:
                    print("Opcion invalida.")
            except ValueError:
                print("Error: Debes ingresar un número entero.")
            
        match opcion:
            case 1: 
                print('''Usted ha elegido la modalidad individual''')

                # solicitar datos
                # nombre
                while True:
                    try:
                        nombre = input("\nIngresa el nombre: ")
                        datos.verificar_nombre(nombre)
                        break
                    except ValueError as err:
                        print (f'Error: {err}')
                
                # edad
                while True:
                    try:
                        edad = input("Ingresa la edad: ")
                        datos.verificar_edad(edad)
                        break
                    except ValueError as err:
                        print (f'Error: {err}')
                
                # genero
                while True:
                    try:
                        genero = input("Ingresa el genero: ").upper().strip()
                        datos.verificar_genero(genero)
                        break
                    except ValueError as err:
                        print (f'Error: {err}')
                
                # categoria
                while True:
                    try:
                        sistema.mostrar_categorias()
                        cate = int(input("\nIngresa tu categoria: "))
                        cati = sistema.obtener_categoria(cate)
                        break
                    except:
                        print ('Ingresa una categoria valida.')
                
                cant = sistema.conteo()
                corredor = Persona(numero= cant, nombre = nombre, edad = edad, genero = genero, categoria = cati.nombre)
                
                sistema.guradar_persona(corredor)
                
                # recibo
                print(f'''
                Nombre: {nombre}
                Edad: {edad}
                Genero: {genero}
                Categoria: {cati.nombre}
                Costo: {cati.precio}
                Medalla: {sistema.actalizar_medallas()}''')


            case 2:
                print("Ha elegido la modalidad en pareja")
                
                # solicitar datos
                
                # corredor 1
                print("\n----- Corredor 1 -----")
                
                # nombre
                while True:
                    try:
                        nombre = input("\nIngresa el nombre: ")
                        datos.verificar_nombre(nombre)
                        break
                    except ValueError as err:
                        print (f'Error: {err}')
                
                # edad
                while True:
                    try:
                        edad = input("Ingresa la edad: ")
                        datos.verificar_edad(edad)
                        break
                    except ValueError as err:
                        print (f'Error: {err}')
                
                # genero
                while True:
                    try:
                        genero = input("Ingresa el genero: ").upper().strip()
                        datos.verificar_genero(genero)
                        break
                    except ValueError as err:
                        print (f'Error: {err}')
                
                # categoria
                while True:
                    try:
                        sistema.mostrar_categorias()
                        cat1 = int(input("\nIngresa tu categoria: "))
                        cati1 = sistema.obtener_categoria(cat1)
                        break
                    except:
                        print ('Ingresa una categoria valida.')
                
                # medalla 1
                med1 = sistema.actalizar_medallas()
                
                cant1 = sistema.conteo()
                corredor1 = Persona(numero = cant1, nombre = nombre, edad = edad, genero = genero, categoria = cati1.nombre)
                
                sistema.guradar_persona(corredor1)

                # corredor 2
                print("\n----- Corredor 2 -----")
                
                # nombre
                while True:
                    try:
                        nombre2 = input("\nIngresa el nombre: ")
                        datos.verificar_nombre(nombre2)
                        break
                    except ValueError as err:
                        print (f'Error: {err}')
                
                # edad
                while True:
                    try:
                        edad2 = input("Ingresa la edad: ")
                        datos.verificar_edad(edad2)
                        break
                    except ValueError as err:
                        print (f'Error: {err}')
                
                # genero
                while True:
                    try:
                        genero2 = input("Ingresa el genero: ").upper().strip()
                        datos.verificar_genero(genero2)
                        break
                    except ValueError as err:
                        print (f'Error: {err}')
                
                # categoria
                while True:
                    try:
                        sistema.mostrar_categorias()
                        cat2 = int(input("\nIngresa tu categoria: "))
                        cati2 = sistema.obtener_categoria(cat2)
                        break
                    except:
                        print ('Ingresa una categoria valida.')
                
                # medalla 2
                med2 = sistema.actalizar_medallas()
                
                cant2 = sistema.conteo()
                corredor2 = Persona(numero = cant2, nombre = nombre2, edad = edad2, genero = genero2, categoria = cati2.nombre)
                
                sistema.guradar_persona(corredor2)
                
                # verificar precio
                if cati1.precio == cati2.precio:
                    total = 80 if (cati2.precio == 50) else 150 
                
                    # recibo
                    print(f'''
                    Nombre: {nombre} | {nombre2}
                    Edad: {edad} | {edad2}
                    Genero: {genero} | {genero2}
                    Categoria: {cati1.nombre} | {cati2.nombre}
                    Costo: {total}
                    Medalla: {med1} | {med2}''')
                else:
                    print("Los precios son diferentes, no es posible la inscripcion")


            case 3:
                print("Persona inscritas: \n")
                print(sistema.obterner_personas())


            case 4:
                print("Saliendo del sistema...")
                continuar1 = False
        
main()