[8:56 p. m., 6/5/2022] +502 4781 5342: #include <iostream>
#include <iomanip>
using namespace std;

int main() {
	//cin.sync_with_stdio(false);
	//cin.tie(nullptr);
	int n;
	cin >> n;
	while (n != 0) {
		if (n == 1) cout << "10\n";
		else if (n == 2) cout << "9\n";
		else {
			cout << "9" << setw((n - 1) / 2 + 1 ) << setfill('0') << "\n";
		}
		cin >> n;
	}

	return 0;
}
[8:56 p. m., 6/5/2022] +502 4781 5342: #!/usr/bin/env python
# -- coding: utf-8 --
from random import choice
def number_in_row(grid, row, number):
    """
    Chequear si un número se encuentra en la fila especificada.
    """
    return number in grid[row]
def number_in_col(grid, col, number):
    """
    Chequear si un número se encuentra en la columna especificada.
    """
    return number in (row[col] for row in grid)
def number_in_box(grid, row, col, number):
    """
    Chequear si un número se encuentra en la caja a la que
    corresponde la posición especificada.
    """
    # Obtener la caja a la que pertenece el número.
    box_row, box_col = box_by_pos(row, col)
    # Construir una lista con los números en la caja.
    numbers_in_box = unpack(
        row[box_col*3:box_col*3 + 3]
        for row in grid[box_row*3:box_row*3 + 3]
    )
    return number in numbers_in_box
def reduce(n):
    """
    Reducir la posición 9x9 a 3x3.
    """
    n /= 3
    if n == 0 or n != int(n):
        n += 1
    return int(n)
def box_by_pos(row, col):
    # Trabajar temporalmente con base 1.
    row += 1
    col += 1
    # Obtener base 0 nuevamente.
    return reduce(row) - 1, reduce(col) - 1
def unpack(iterable):
    """
    >>> list(unpack([[1, 2], [3, 4]]))
    [1, 2, 3, 4]
    """
    for item in iterable:
        yield from item
def get_possible_numbers(grid, row, col):
    """
    Retorna números posibles para una determinada posición.
    """
    for number in range(1, 10):
        if (not number_in_row(grid, row, number) and
            not number_in_col(grid, col, number) and
            not number_in_box(grid, row, col, number)):
            yield number
def main():
    while True:
        # Los ceros representan casilleros vacíos.
        grid = [
            [0, 0, 0, 8, 0, 3, 0, 0, 0],
            [0, 1, 0, 9, 0, 0, 7, 0, 8],
            [0, 0, 0, 0, 4, 0, 0, 0, 9],
            [2, 0, 0, 0, 0, 4, 0, 6, 0],
            [4, 0, 7, 0, 0, 0, 9, 0, 5],
            [0, 5, 0, 7, 0, 0, 0, 0, 1],
            [7, 0, 0, 0, 3, 0, 0, 0, 0],
            [3, 0, 6, 0, 0, 8, 0, 7, 0],
            [0, 0, 0, 2, 0, 7, 0, 0, 0],
        ]
        
        s = \
        """\
        +-----------------------+
        | {} {} {} | {} {} {} | {} {} {} |
        | {} {} {} | {} {} {} | {} {} {} |
        | {} {} {} | {} {} {} | {} {} {} |
        +-----------------------+
        | {} {} {} | {} {} {} | {} {} {} |
        | {} {} {} | {} {} {} | {} {} {} |
        | {} {} {} | {} {} {} | {} {} {} |
        +-----------------------+
        | {} {} {} | {} {} {} | {} {} {} |
        | {} {} {} | {} {} {} | {} {} {} |
        | {} {} {} | {} {} {} | {} {} {} |
        +-----------------------+
        """
        
        while True:
            possible_numbers = {
                (row, col): None for row in range(9) for col in range(9)
            }
            
            # Obtener una lista de números posibles para cada una de 
            # las posiciones vacías.
            for row in range(9):
                for col in range(9):
                    number = grid[row][col]
                    if number == 0:
                        options = list(
                            get_possible_numbers(grid, row, col)
                        )
                        if options:
                            possible_numbers[(row, col)] = options
            
            # Remover valores vacíos y ordenar por la cantidad de 
            # posibilidades.
            possible_numbers = sorted(
                (
                    (k, v)
                    for (k, v) in possible_numbers.items()
                    if v is not None
                ),
                key=lambda kv: len(kv[1])
            )
            
            if possible_numbers:
                # Obtener el primer item.
                (row, col), numbers = possible_numbers[0]
                # Fuerza bruta: obtener un número aleatorio de la 
                # lista de posibiilidades hasta que la grilla esté
                # completa.
                grid[row][col] = choice(numbers)
            else:
                break
        
        # Chequear si la fuerza bruta dió resultado: si no hay más 
        # ceros en la grilla entonces el Sudoku está resuelto.
        if 0 not in unpack(grid):
            print(s.format(*(unpack(grid))))
            break
if _name_ == "_main_":
    main()
[8:56 p. m., 6/5/2022] +502 4781 5342: """
	Implementación del cifrado César en Python,
	respetando espacios y otros caracteres como la ñ
	@author parzibyte
"""


def codificar(mensaje, rotaciones):
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
