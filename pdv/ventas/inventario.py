import random

# Lista de nombres de productos
nombres_productos = [
    "Arroz", "Frijoles", "Aceite", "Sal", "Azúcar", "Café", "Harina", "Leche",
    "Pasta", "Atún", "Jabón", "Detergente", "Cereal", "Galletas", "Refresco",
    "Agua", "Pan", "Sopa", "Chocolate", "Cerveza", "Vino", "Cigarros", "Papel higiénico",
    "Pañales", "Jabón líquido", "Salsa de tomate", "Cepillo de dientes", "Pasta dental",
    "Queso", "Jamón", "Huevo", "Yogur", "Frutas", "Verduras", "Carne", "Pollo", "Pescado",
    "Camarones", "Papas", "Cebolla", "Tomate", "Plátano", "Manzana", "Naranja", "Limón",
    "Uva", "Lechuga", "Pepino", "Zanahoria", "Calabacín", "Brócoli", "Cilantro", "Perejil",
    "Canela", "Nuez", "Almendra", "Avena", "Miel", "Pan integral", "Tortillas", "Chiles enlatados",
    "Mermelada", "Mantequilla", "Yogur", "Cerveza", "Galletas saladas", "Papel aluminio",
    "Bolsas de basura", "Té", "Café soluble", "Mayonesa", "Mostaza", "Kétchup", "Salsa picante",
    "Pan de molde", "Pepinillos", "Zanahoria rallada", "Champiñones enlatados", "Salchichas",
    "Hot dogs", "Pan de hamburguesa", "Hamburguesas congeladas", "Mangos", "Duraznos", "Ciruelas",
    "Tamarindos", "Sandías", "Melones", "Piñas", "Melocotones", "Uvas pasas", "Ciruelas pasas",
    "Nueces de la india", "Dátiles", "Higos", "Almendras", "Pistachos", "Macadamias", "Lentejas",
    "Ajo", "Fideos", "Sardinas enlatadas", "Mantequilla de maní", "Helado", "Sirope de chocolate",
    "Sirope de fresa", "Sirope de vainilla", "Pistachos salados", "Cajetas", "Nuez de macadamia",
    "Cacahuates", "Crema dental", "Caramelos", "Chocolates", "Cocadas", "Gomitas", "Palomitas"
]

# Generar inventario aleatorio de 200 productos
inventario = []

for _ in range(200):
    nombre = random.choice(nombres_productos)
    precio = round(random.uniform(1, 50), 2)  # Precio entre 1 y 50
    cantidad = random.randint(10, 100)  # Cantidad entre 10 y 100
    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    inventario.append(producto)

# Imprimir inventario generado
for i, producto in enumerate(inventario, start=1):
    print(f"{i}. {producto['nombre']} - Precio: ${producto['precio']:.2f} - Cantidad: {producto['cantidad']}")
