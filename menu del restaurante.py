# matriz de productos (menu)
# Formato  [Nombre del Producto, Categoría,Precio Base]
menu = [
    ["Hamburguesa", "Comida", 25000],
    ["Perro Caliente", "Comida", 20000],
    ["Gaseosa", "Bebida", 7000],
    ["Jugo Natural", "Bebida", 10000],
    ["Helado", "Postre", 9000],
    ["Banana Split", "Postre", 15000],
]
# Datos de la promocion
categoria_objetivo = "Comida"
umbral = 18000
# función para calcular precio final


def calcular_precio_final(categoria, precio_base):

    precio_final = precio_base

    if categoria == categoria_objetivo and precio_base > umbral:
        descuento = precio_base * 0.15
        precio_final = precio_base - descuento
        return precio_final
    else:
        return precio_base


# mostrar resultados
print("Menu del restaurante")
print("-"*60)

for producto in menu:
    nombre = producto[0]
    categoria = producto[1]
    precio_base = producto[2]

    precio_final = calcular_precio_final(categoria, precio_base)

    print(f"Producto: {nombre}")
    print(f"Categoría: {categoria}")
    print(f"Precio base: ${precio_base}")
    print(f"Precio final: ${precio_final}")
    print("-"*60)
