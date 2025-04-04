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