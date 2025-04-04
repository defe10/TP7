"""
Tp Nº7
Alumno: Federico Casoni - sabados presencial


1) Escribir una clase llamada Rectángulo que contenga una base y una altura, y que contenga un método que devuelva el área del rectángulo."""

class Rectangulo:
    
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area (self):
        return self.base * self.altura


rectangulo1 = Rectangulo(20,35)
print (f"Área: {rectangulo1.area()}")

"""2) Modelar una clase Mate que describa el funcionamiento de la conocida bebida tradicional argentina. La clase debe contener como miembros:
o Un atributo para la cantidad de cebadas restantes hasta que se lava el mate (representada por un número).
o Un atributo para el estado (lleno o vacío).
o Un atributo n, que indica la cantidad máxima de cebadas.
o Un método cebar, que llena el mate con agua. Si se intenta cebar con el mate lleno, se debe lanzar una excepción que imprima el mensaje ¡Cuidado! ¡Te quemaste!
o Un método beber, que vacía el mate y le resta una cebada disponible. Si se intenta beber un mate vacío, se debe lanzar una excepción que imprima el mensaje: ¡El mate está vacío!
o Es posible seguir cebando y bebiendo el mate aunque no haya cebadas disponibles. En ese caso la cantidad de cebadas restantes se mantendrá en 0, y cada vez que se intente beber se debe imprimir un mensaje de aviso: “Advertencia: el mate está lavado.” pero no se debe lanzar una excepción."""

class Mate:
    def __init__(self, n):
        self.n = n  
        self.cebadas_restantes = n  
        self.lleno = False  

    def cebar(self):
        if self.lleno:
            print("¡Cuidado! ¡Te quemaste!") 
        self.lleno = True   

    def beber(self):
        if not self.lleno:
            print("¡El mate está vacío!")  
        
        self.lleno = False  
        
        if self.cebadas_restantes > 0:
            self.cebadas_restantes -= 1  
        else:
            print("Advertencia: el mate está lavado.")  


mate = Mate(3)  

mate.cebar()  
mate.beber()  

mate.cebar()
mate.beber()

mate.cebar()
mate.beber()

mate.cebar()
mate.beber()  

"""3) Botella y Sacacorchos
 Escribir una clase Corcho, que contenga un atributo bodega (cadena con el nombre de la bodega).
 Escribir una clase Botella que contenga un atributo corcho con una referencia al corcho que la tapa, o None si está destapada.
 Escribir una clase Sacacorchos que tenga un método destapar que le reciba una botella, le saque el corcho y se guarde una referencia al corcho sacado. Debe lanzar una excepción en el caso en que la botella ya esté destapada, o si el sacacorchos ya contiene un corcho.
 Agregar un método limpiar, que saque el corcho del sacacorchos, o lance una excepción en el caso en el que no haya un corcho."""


class Corcho:
    def __init__(self, bodega):
        self.bodega = bodega 

class Botella:
    def __init__(self, corcho):
        self.corcho = corcho  

class Sacacorchos:
    def __init__(self):
        self.corcho_extraido = None  

    def destapar(self, botella):
        if self.corcho_extraido is not None:
            print("El sacacorchos ya tiene un corcho ")
            return  
        
        if botella.corcho is None:
            print("¡La botella ya está destapada!")
            return  
        
        self.corcho_extraido = botella.corcho  
        botella.corcho = None  
        print("Botella destapada")

    def limpiar(self):
        if self.corcho_extraido is None:
            print("El sacacorchos está limpio")
            return  
        
        self.corcho_extraido = None  
        print("Sacacorchos limpiado")


corcho1 = Corcho("Bodega La Calderilla")
botella1 = Botella(corcho1)
sacacorchos1 = Sacacorchos()


sacacorchos1.destapar(botella1)


if sacacorchos1.corcho_extraido:
    print(f"El sacacorchos tiene un corcho de {sacacorchos1.corcho_extraido.bodega}")
else:
    print("El sacacorchos no tiene ningún corcho.")


if botella1.corcho is None:
    print("La botella está destapada.")


sacacorchos1.limpiar()

if sacacorchos1.corcho_extraido is None:
    print("El sacacorchos está limpio.")

"""4) Una heladería es un tipo especial de restaurante. Cree una clase Restaurante, cuyo método __init__() guarde dos atributos: restaurante_nombre y tipo_comida. Cree un método describir_restaurante() que muestre estas piezas de información, y un método abrir_restaurante() que muestre un mensaje indicando que el restaurante ahora está abierto. Luego cree una clase Heladeria que herede de Restaurante, y agregue a los existentes un atributo llamado sabores que almacene una lista de los sabores de helado disponibles. Escriba también un método que muestre estos valores, cree una instancia de la clase y llame al método."""

from datetime import datetime

class Restaurante:
    def __init__(self, restaurante_nombre, tipo_comida):
        self.restaurante_nombre = restaurante_nombre
        self.tipo_comida = tipo_comida

    def describir_restaurante(self):
        print(f"Restaurante: {self.restaurante_nombre}")
        print(f"Tipo de comida: {self.tipo_comida}")

    def abrir_restaurante(self):
        hora_actual = datetime.now().hour  
        if hora_actual < 8 or hora_actual > 24:
            print(f"El negocio está cerrado.")
        else:
            print(f"{self.restaurante_nombre} está abierto.")

class Heladeria(Restaurante):
    def __init__(self, restaurante_nombre, tipo_comida, sabores):
        super().__init__(restaurante_nombre, tipo_comida)
        self.sabores = sabores

    def describir_heladeria(self):
        print(f"Heladería: {self.restaurante_nombre}")
        print (f"Tipo de helados: {self.tipo_comida}")
        print (f"Sabores: {', '.join(self.sabores)}")


restaurante1 = Restaurante("La Farola", "Parrilla")
restaurante1.describir_restaurante()
restaurante1.abrir_restaurante()

heladeria1 = Heladeria("Lepon", "Artesanales", ["Dulce de leche", "Chocolate", "Sambayón"])
heladeria1.describir_heladeria()
heladeria1.abrir_restaurante()

"""5) Escribir una clase Personaje que contenga los atributos vida, posicion y velocidad, y los métodos recibir_ataque, que reduzca la vida según una cantidad recibida y lance una excepción si la vida pasa a ser menor o igual que cero, y mover que reciba una dirección y se mueva en esa dirección la cantidad indicada por velocidad.
 Escribir una clase Soldado que herede de Personaje, y agregue el atributo ataque y el método atacar, que reciba otro personaje, al que le debe hacer el daño indicado por el atributo ataque.
 Escribir una clase Campesino que herede de Personaje, y agregue el atributo cosecha y el método cosechar, que devuelva la cantidad cosechada"""


class Personaje:
    def __init__(self, vida, posicion = None, velocidad = 0):
        self.vida = vida
        self.posicion = posicion if posicion is not None else [0, 0]  
        self.velocidad = velocidad

    def recibir_ataque(self, cantidad):
        self.vida -= cantidad
        if self.vida <= 0:
            self.vida = 0
            print("Muerto!")
        else:
            print(f"Te quedan: {self.vida} vidas")

    def mover(self, direccion):
        movimientos = {
            "arriba": (0, 1),
            "abajo": (0, -1),
            "izquierda": (-1, 0),
            "derecha": (1, 0)
        }

        if direccion in movimientos:
            x, y = movimientos[direccion]
            self.posicion[0] += x * self.velocidad
            self.posicion[1] += y * self.velocidad
            print(f"Posición: {self.posicion}")
  



personaje1 = Personaje(10, [5, 6], 2)

personaje1.mover("arriba")

personaje1.recibir_ataque(3)

"""6) Usuarios: Cree una clase Usuario. Cree también dos atributos nombre y apellido, así como otros atributos que típicamente se guardan en un perfil de usuario. Escriba un método describir_usuario() que muestre un resumen de la información del usuario. Escriba otro método saludar_usuario() que muestre un saludo personalizado al usuario.
Cree varias instancias que representen distintos usuarios y llame ambos métodos para cada uno."""

class Usuario:
    def __init__(self, nombre, apellido, edad, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.dni = dni

        self.saludar()
        self.describir_usuario() 

    def describir_usuario (self):
        print(f"\nDATOS USUARIO:\nNombre: {self.nombre}\nApellido: {self.apellido}\nEdad: {self.edad}\nDNI: {self.dni}\n")

    def saludar (self):
        print(f"Hola, {self.nombre} {self.apellido}")


usuario1 = Usuario("Federico", "Casoni", 46, "23232232")
usuario2 = Usuario("Ricardo", "Tapia", 2, "33242232")
usuario3 = Usuario("Bruno", "Díaz", 32, "34234243")

"""7) Admin: Un administrador es un tipo de usuario con privilegios especiales. Cree una clase Admin que herede de la clase Usuario del ejercicio anterior y agréguele un atributo privilegios que almacene una lista de strings tales como “puede postear en el foro”, “puede borrar un post”, “puede banear usuario”, etc. Escriba un método mostrar_privilegios() que muestre el conjunto de privilegios del administrador, cree una instancia de la clase y llame al método."""

class Usuario:
    def __init__(self, nombre, apellido, edad, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.dni = dni

        self.saludar()
        self.describir_usuario() 

    def describir_usuario (self):
        print(f"\nDATOS USUARIO:\nNombre: {self.nombre}\nApellido: {self.apellido}\nEdad: {self.edad}\nDNI: {self.dni}\n")

    def saludar (self):
        print(f"Hola, {self.nombre} {self.apellido}")


class Admin (Usuario):

    def __init__(self, nombre, apellido, edad, dni, privilegios):
        super().__init__(nombre, apellido, edad, dni)
        self.privilegios = privilegios

    def mostrar_privilegios (self):
        print(f"Privilegios del administrador: {', '.join(self.privilegios)}")

        

usuario1 = Usuario("Federico", "Casoni", 46, "23232232")
usuario2 = Usuario("Ricardo", "Tapia", 2, "33242232")
usuario3 = Usuario("Bruno", "Díaz", 32, "34234243")

lista_privilegios = ["puede postear en el foro", "puede borrar un post", "puede banear usuario"]
admin = Admin("Juan", "González", 40, "12345678", lista_privilegios)
admin.mostrar_privilegios()

"""8) Privilegios: Escriba una clase Privilegios. La clase debería tener un atributo, privilegios, que almacene una lista de strings con los privilegios de manera similar a la del ejercicio 7. Mueva el método mostrar_privilegios() de ese ejercicio a esta clase, y haga que una instancia de esta clase sea un atla clase Admiributo de n. Cree una nueva instancia de Admin y use el método para mostrar privilegios."""


class Privilegios:
    def __init__(self, privilegios=None):
        if privilegios is None:
            privilegios = []
        self.privilegios = privilegios

    def mostrar_privilegios(self):
        if self.privilegios:
            print(f"Privilegios del administrador: {', '.join(self.privilegios)}")
        

class Admin:
    def __init__(self, nombre):
        self.nombre = nombre
        self.privilegios = Privilegios()


admin1 = Admin("Ana")


admin1.privilegios.privilegios = ["puede postear en el foro", "puede borrar un post", "puede banear usuario"]


admin1.privilegios.mostrar_privilegios()


"""9) Restaurante importado: Escriba un programa que esté en otro archivo que la clase Restaurante del ejercicio 4, e impórtela al módulo actual. Cree una instancia de Restaurante y llame a alguno de sus métodos para asegurarse que la importación funcionó."""

from restaurante import Restaurante

mi_restaurante = Restaurante("La Farola", "Parrilla")
mi_restaurante.describir_restaurante()
mi_restaurante.abrir_restaurante()

"""10) (Opcional): Repita el ejercicio anterior pero esta vez importando la clase Heladeria. ¿Qué se necesita para que funcione la importación?"""

from restaurante import Heladeria

heladeria1 = Heladeria("Lepon", "Artesanales", ["Dulce de leche", "Chocolate", "Sambayón"])
heladeria1.describir_heladeria()
heladeria1.abrir_restaurante()