from auto import *  # Debemos importar las clases que utilizaremos

auto1 = Auto()  # Instancia de la clase

print(auto1.mostrar_informacion())

print('\n>>> Ingrese un numero <<<')  # Ofrecemos al usuario encender el motor
llave = int(input('1)Encender motor - 2)Apagar motor :'))  # El input almacena string, si queremos obtener
# numeros anteponemos int()
print(auto1.llave_on(llave))  # Enviamos un int como parametro
print(auto1.encender_motor())

print(auto1.mostrar_informacion())
