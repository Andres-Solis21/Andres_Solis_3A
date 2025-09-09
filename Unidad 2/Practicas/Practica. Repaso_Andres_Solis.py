productos = ["Hamburguesa", "Taco", "Burrito"]
precios = [60, 20, 40]

def calcular_total(cantidades, precios):
    total = 0
    for i in range(len(cantidades)):
        total += cantidades[i] * precios[i]
    return total

def aplicar_descuento(total, porcentaje_descuento):
    descuento = total * (porcentaje_descuento / 100)
    return total - descuento, descuento

def imprimir_recibo(nombre, productos, precios, cantidades, subtotal, descuento_aplicado, total_final):
    print("\n" + "="*40)
    print("           RECIBO DE COMPRA")
    print("            TAQUERÍA")
    print("="*40)
    print(f"Cliente: {nombre}")
    print("-"*40)
    
   
    for i in range(len(productos)):
        if cantidades[i] > 0:  
            total_producto = cantidades[i] * precios[i]
            print(f"{productos[i]}")
            print(f"  Cantidad: {cantidades[i]} x ${precios[i]} = ${total_producto}")
    
    print("-"*40)
    print(f"Subtotal:    ${subtotal:.2f}")
    if descuento_aplicado > 0:
        print(f"Descuento (10%):            -${descuento_aplicado:.2f}")
    print(f"TOTAL A PAGAR:               ${total_final:.2f}")
    print("="*40)
    print("¡Gracias por tu compra!")
    print("="*40)

print("Bienvenido a la Taquería")
nombre = input("Ingresa tu nombre: ")

cantidades = []
print("\nSelecciona tu pedido:")
for i in range(len(productos)):
    print(f"{i+1}. {productos[i]} - ${precios[i]}")
    cantidad = int(input(f"¿Cuántos {productos[i]} quieres? "))
    cantidades.append(cantidad)

# Calcular subtotal
subtotal = calcular_total(cantidades, precios)

# Aplicar descuento del 10% si el total es mayor a $100
porcentaje_descuento = 0
descuento_aplicado = 0

if subtotal > 100:
    porcentaje_descuento = 10
    total_final, descuento_aplicado = aplicar_descuento(subtotal, porcentaje_descuento)
    print(f"\n¡Felicidades! Por tu compra mayor a $100, tienes un descuento del {porcentaje_descuento}%")
else:
    total_final = subtotal

# Imprimir el recibo
imprimir_recibo(nombre, productos, precios, cantidades, subtotal, descuento_aplicado, total_final)