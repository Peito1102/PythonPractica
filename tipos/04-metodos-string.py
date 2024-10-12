animal = "  chanCHito     feliz         "
print(animal.upper()) #minusculas
print(animal.lower()) #mayusculas
print(animal.strip().capitalize()) #hace mayuscula la primera y miniscula el resto
print(animal.title()) #pone mayuscula a la inicial de cada palabra
print(animal.strip()) #elimina espacio de la derecha e izquierda, como el trim
print(animal.lstrip()) #elimina los espacio de la izquierda
print(animal.rstrip()) #elimina los espacio de la derecha
print(animal.find("CH")) #devuelve el indice en donde empieza la cadena buscada
print(animal.replace("nCH","j")) #reemplaza lo que quieres reemplazar
print("nCH" in animal) #busca si esta y devuelve boleano
print("nCH" not in animal) #busca si no esta y devuelve boleano

