from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from inventario import inventario
import csv
import os
import random

class Product:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price


class VentasWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.products = []
        self.load_products()
            
    def admin(self):
        print("Admin presionado")

    def signout(self):
        print("Signout presionado")

    def load_csv(archivo_csv, inventario):
        try:
            if not archivo_csv.endswith('.csv'):
                raise ValueError("El archivo debe tener la extensión .csv")
            
            with open(archivo_csv, 'r') as archivo:
                lector_csv = csv.DictReader(archivo)
                for fila in lector_csv:
                    inventario.append(fila)
            print("Invntario agregado correctamente desde el archivo CSV.")
        except FileNotFoundError:
            print("El archivo CSV no se encontró.")
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print("Error al agregar el inventario", e)

    inventario = []
    archivo_csv = "inventario.csv"
    load_csv(archivo_csv, inventario)
    print(inventario)

    def load_products(self):
        cantidad = random.randint(10, 100)

        #Cargar Productos de manera manual
        self.products.append(Product('POO1', 'Arroz', 1.100, cantidad))
        self.products.append(Product('POO2', 'Frijoles', 890, cantidad))
        self.products.append(Product('POO3', 'Aceite', 1.800, cantidad))
        self.products.append(Product('POO4', 'Sal', 890, cantidad))
        self.products.append(Product('POO5', 'Azúcar', 900, cantidad))
        self.products.append(Product('POO6', 'Café', 1.200, cantidad))
        self.products.append(Product('POO7', 'Harina', 1.800, cantidad))
        self.products.append(Product('POO8', 'Leche', 1.200, cantidad))
        self.products.append(Product('POO9', 'Pasta', 1.900, cantidad))
        self.products.append(Product('POO10', 'Atún', 1.800, cantidad))
        self.products.append(Product('POO11', 'Jabón', 2.200, cantidad))
        self.products.append(Product('POO12', 'Detergente', 6.800, cantidad))
        self.products.append(Product('POO13', 'Cereal', 1.800, cantidad))
        self.products.append(Product('POO14', 'Galletas', 800, cantidad))
        self.products.append(Product('POO15', 'Refresco', 1.500, cantidad))
        self.products.append(Product('POO15', 'Agua', 1.200, cantidad))
        self.products.append(Product('POO16', 'Pan', 1.800, cantidad))
        self.products.append(Product('POO17', 'Sopa', 1.200, cantidad))
        self.products.append(Product('POO18', 'Chocolate', 600, cantidad))
        self.products.append(Product('POO19', 'Cerveza', 1.200, cantidad))
        self.products.append(Product('POO20', 'Vino', 1.800, cantidad))
        self.products.append(Product('POO21', 'Cigarros', 1.100, cantidad))
        self.products.append(Product('POO22', 'Papel Higiénico', cantidad))

        


class VentasApp(App):
    def build(self):
        return VentasWindow()


if __name__ == '__main__':
    VentasApp().run()
