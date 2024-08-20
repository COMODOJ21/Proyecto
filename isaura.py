# elabore un algoritmo que muestre la factura de las sigientes compra
#el señor pedro ramirez compro en falabela dos gims de 125.000 pesos cada uno, dos camisas de 45.000 pesos cada una, una camisa tipo polo por 30.000 pesos.
#tener en cuenta lo siguiente: si la compra lleva una  camisa tipo polo tiene un descuento del 5%
# si la compra es superior a 200.000 pesos se realiza un descuento del 30%.
#mostrar el total a pagar  el total del descuento en pesos 

precio_geams = 125.000 
precio_camisa = 45.000 
precio_polo = 30.000 
cantidad_geams = 2 
cantidad_camisas = 2 
cantidad_polo = 1 

total_geams = cantidad_geams * precio_geams
total_camisas = cantidad_camisas * precio_camisa
total_polo = cantidad_polo * precio_polo

total = total_geams + total_camisas + total_polo

descuento_total = 0


if cantidad_polo > 0:
    descuento_polo = total * 0.05
    total -= descuento_polo
    descuento_total += descuento_polo


if total > 200000:
    descuento_adicional = total * 0.30
    total -= descuento_adicional
    descuento_total += descuento_adicional
    

print(f"Precio de la compra: {total_geams + total_camisas + total_polo}")    
print(f"Descuento por camisa tipo polo: {descuento_polo if cantidad_polo > 0 else 0}")
print(f"Descuento adicional por compra superior a 200,000 pesos: {descuento_adicional if total_geams + total_camisas + total_polo > 200000 else 0}")
print(f"Total de descuentos: {descuento_total}")
print(f"Total a pagar: {total}")