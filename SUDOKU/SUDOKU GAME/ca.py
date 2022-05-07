[8:56 p. m., 6/5/2022] +502 4781 5342: def codificar(mensaje, rotaciones):
    #Nota: también se puede importar a string y usar ascii_letters y ascii_uppercase
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    alfabeto_mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    longitud_alfabeto = len(alfabeto)
    codificado = ""
    for letra in mensaje:
        if not letra.isalpha() or letra.lower() == 'ñ':
            codificado += letra
            continue
        valor_letra = ord(letra)
        # Suponemos que es minúscula, así que esto comienza en 97(a) y se usará el alfabeto en minúsculas
        alfabeto_a_usar = alfabeto
        limite = 97  # Pero si es mayúscula, comienza en 65(A) y se usa en mayúsculas
        if letra.isupper():
            limite = 65
            alfabeto_a_usar = alfabeto_mayusculas

        # Rotamos la letra
        posicion = (valor_letra - limite + rotaciones) % longitud_alfabeto

        # Convertimos el entero resultante a letra y lo concatenamos
        codificado += alfabeto_a_usar[posicion]
    return codificado


def decodificar(mensaje, rotaciones):
    #Nota: también se puede importar a string y usar ascii_letters y ascii_uppercase
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    alfabeto_mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    longitud_alfabeto = len(alfabeto)
    decodificado = ""
    for letra in mensaje:
        if not letra.isalpha() or letra.lower() == 'ñ':
            decodificado += letra
            continue
        valor_letra = ord(letra)
        # Suponemos que es minúscula, así que esto comienza en 97(a) y se usará el alfabeto en minúsculas
        alfabeto_a_usar = alfabeto
        limite = 97  # Pero si es mayúscula, comienza en 65(A) y se usa en mayúsculas
        if letra.isupper():
            limite = 65
            alfabeto_a_usar = alfabeto_mayusculas

        # Rotamos la letra, ahora hacia la izquierda
        posicion = (valor_letra - limite - rotaciones) % longitud_alfabeto

        # Convertimos el entero resultante a letra y lo concatenamos
        decodificado += alfabeto_a_usar[posicion]
    return decodificado


# Ejemplo de uso
mensaje = "Visita parzibyte.me"
print("El mensaje original es: ", mensaje)
#Nota: el mismo número de rotaciones debe usarse tanto para codificar y decodificar
rotaciones = 1
codificado = codificar(mensaje, rotaciones)
print("Codificado es: ", codificado)
decodificado = decodificar(codificado, rotaciones)
print("Decodificado es: ", decodificado)
[8:56 p. m., 6/5/2022] +502 4781 5342: #Intervalo inferior
a=10
#Intervalo superior 
b=454657
#Contador para la cantidad de capicuas
c=0
print("Los capicuas encontrados son los siguientes:")
for i in range(a,b+1):
    num_s=str(i)
    num_list=list(num_s)
    if num_list==num_list[::-1]:
        cap=''.join(num_list)
        c+=1
        print(cap)
        
print("Total de Capicuas:",c)