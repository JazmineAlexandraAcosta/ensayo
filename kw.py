  #kw
q = float(input("Introduzca la cantidad de KiloWatts consumidos: "))
kw = 531
pkw=kw*700
print("precio KiloWatts ",kw)
if q > 700:
	kw2 = q-700
	print("se incremento un 5% por exceso de kw")
	pkw2=kw*0.05
	pkw2=pkw2+kw
	p=pkw2*kw2
	precio=(pkw+p)
	print("el valor a pagar es:", precio)
else:
	print("no se le a incrementado nada:")
	precio2=q*kw
	print("el valor a pagar es:", precio2)
	
