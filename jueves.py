print("=======================================================")
print("                                                       ")
print("                     INVENTARIO                        ") 
print("                                                       ")
print("=======================================================")

#vamos a pedir los datos al usuario

lista_productos = []
total=0
Total_general=0
continuar = True


#ahora vamos a calcular
while  continuar:
    
    while continuar:
        try: 
            nombre_producto = str(input("Ingrese el nombre del producto: "))
            if nombre_producto.isalpha():
                break
            else:
                print("ERROR Nombre de producto erroneo")
        except:
            print("Debes ingresar texto") #el except evalua que el nombre_producto si sea str y no numeros. 

    while continuar:
        try:
            precio_producto = float(input("Ingrese el precio del producto: "))
            if precio_producto<=0:
                print("Precio de producto inválido")
            else:
                break    
        
        except:
            print("ERROR Debes ingresar numeros")    

    while continuar:
        try:
            cantidad_producto = int(input("Ingrese la cantidad del producto: "))
            if cantidad_producto<=0:
                print("Precio de producto inválido")
            else:
                break    
        
        except:
            print("ERROR Debes ingresar numeros")                

    while continuar:
        try:
            descuento_producto = int(input("Ingrese el valor de descuento porcentual de 0-100: "))
            if descuento_producto>0 and descuento_producto<=100:
                break
            else:
                print("Valor de descuento inválido")   
        
        except:
            print("ERROR Debes ingresar numeros")
        

    subtotal1= cantidad_producto*precio_producto
    descuento= subtotal1*((descuento_producto/100))
    subtotal2= subtotal1-descuento
    total1= subtotal2
    Total_general += total1
    
    lista_productos.append([nombre_producto,precio_producto, cantidad_producto, descuento_producto,total1,]) 
    total+=total1   
    
    otra = input("Desea agregar otro producto, 1(si), 2(no): ").lower()
    if otra != '1':
            break
        
        
    print("Esta es la lista de productos comprados")
            
    for producto in lista_productos:
        print(f"Nombre: {producto[0]} - Precio: {producto[1]} - Cantidad: {producto[2]} - Descuento%: {producto[3]} - Total: {producto[4]}")
        
    print("El total acumulado es:", Total_general)    

########################################################
#lista final del cliente

print("============================================")
print("                                            ")
print("             SU COMPRA SERÍA                ")
print("                                            ")
print("============================================")

def mostrar_lista (lista_productos,total):
    print("Lista de productos comprados")
    for producto in lista_productos:
        
        id = lista_productos.index(producto)
        print(f"{id +1}. Nombre: {producto[0]} - Precio: {producto[1]} - Cantidad: {producto[2]} - Descuento%: {producto[3]} - Total: {producto[4]}")
        
print("Valor acumulado a pagar:", Total_general)    

eliminar = int(input("Desea eliminar uno de los elementos? Indique el numero: "))
eliminar = lista_productos.pop(eliminar -1)
Total_general -= eliminar[4]


print("El elemento ha sido eliminado con éxito")

while continuar:
    otra = input("Desea agregar otro producto, 1(si), 2(no): ").lower()
    if otra != '1':
            break
            
            
    print("Esta es la lista de productos comprados")
                
    for producto in lista_productos:
            print(f"Nombre: {producto[0]} - Precio: {producto[1]} - Cantidad: {producto[2]} - Descuento%: {producto[3]} - Total: {producto[4]}")
            
    print("El total acumulado es:", Total_general)    



