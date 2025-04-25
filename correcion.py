print("=======================================================")
print("                                                       ")
print("                     INVENTARIO                        ") 
print("                                                       ")
print("=======================================================")

# Vamos a pedir los datos al usuario

lista_productos = []
total = 0
Total_general = 0
continuar = True

# Función mostrar_lista
def mostrar_lista(lista_productos, total_general):
    print("Lista de productos comprados:")
    for i, producto in enumerate(lista_productos, start=1):
        print(f"{i}. Nombre: {producto[0]} - Precio: {producto[1]} - Cantidad: {producto[2]} - Descuento%: {producto[3]} - Total: {producto[4]}")
    print("Valor acumulado a pagar:", total_general)

# Función agregar_productos
def agregar_producto():
    global Total_general
    while continuar:
        try:
            nombre_producto = str(input("Ingrese el nombre del producto: "))
            if nombre_producto.isalpha():
                break
            else:
                print("ERROR Nombre de producto erroneo")
        except:
            print("Debes ingresar texto")

    while continuar:
        try:
            precio_producto = float(input("Ingrese el precio del producto: "))
            if precio_producto > 0:
                break
            else:
                print("Precio de producto inválido")
        except:
            print("ERROR Debes ingresar numeros")

    while continuar:
        try:
            cantidad_producto = int(input("Ingrese la cantidad del producto: "))
            if cantidad_producto > 0:
                break
            else:
                print("Cantidad de producto inválida")
        except:
            print("ERROR Debes ingresar numeros")

    while continuar:
        try:
            descuento_producto = int(input("Ingrese el valor de descuento porcentual de 0-100: "))
            if 0 < descuento_producto <= 100:
                break
            else:
                print("Valor de descuento inválido")
        except:
            print("ERROR Debes ingresar numeros")

    subtotal1 = cantidad_producto * precio_producto
    descuento = subtotal1 * (descuento_producto / 100)
    subtotal2 = subtotal1 - descuento
    total1 = subtotal2
    Total_general += total1

    lista_productos.append([nombre_producto, precio_producto, cantidad_producto, descuento_producto, total1])

while continuar:
    agregar_producto()

    agregar = input("Desea agregar otro producto, 1(si), 2(no): ").lower()
    if agregar != '1':
        break

    print("Esta es la lista de productos comprados")
    mostrar_lista(lista_productos, Total_general)

while continuar:
    print("============================================")
    print("                                            ")
    print("             SU COMPRA SERÍA                ")
    print("                                            ")
    print("============================================")

    mostrar_lista(lista_productos, Total_general)
    decision = input("Desea eliminar uno de los elementos? S(si), N(no), A(agregar), F(salir): ").lower()

    if decision == 's':
        try:
            eliminar = int(input("Indique el número del producto que desea eliminar: "))
            eliminado = lista_productos.pop(eliminar - 1)
            Total_general -= eliminado[4]
            print("Producto eliminado con éxito.")
        except:
            print("Número inválido.")

    elif decision == 'a':
        agregar_producto()

    elif decision == 'n':
        continue  

    elif decision == 'f':
        print("Gracias por su compra.")
        mostrar_lista(lista_productos, Total_general)
        break
