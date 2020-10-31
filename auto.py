# Un OBJETO posee PROPIEDADES (atributos) y posee un COMPORTAMIENTO
# (metodo).

# Método: Es una funcion que pertenece a una clase
# Funcion: No pertenecen a ninguna clase
# Metodo: self hace referencia al propio objeto
# Self viene siendo el This en otros lenguajes
# En el constructor declaramos los valores iniciales o por defecto que tendra un objeto de ese tipo
# Self == Auto

class Auto:

    def __init__(self):  # Constructor
        self.largo = 250  # Medida en cms
        self.ancho = 120
        self.__ruedas = 4  # Con __ encapsulamos la variable. Solo se accede desde la clase
        self.__encendido = False

    def mostrar_informacion(self):
        print('\n>>> Caracteristicas de un Automovil <<<')
        print('Cantidad de ruedas:', self.__ruedas)
        print('Largo:', self.largo, 'cm')
        print('Ancho:', self.ancho, 'cm')

        if self.__encendido == False:  # Preguntamos si el motor esta encendido
            return "* El motor se encuentra Apagado."
        else:
            return "* El motor se encuentra Encendido."

    def llave_on(self, llave: int):
        if llave == 1:
            self.__encendido = True  # Cambiamos el estado de encendido si ingresa 1

    def check_engine(self):
        print('\nEscaneando sistemas...')

        self.combustible = True
        self.aceite = True
        self.bateria = True

        if (self.combustible and self.aceite and self.bateria):
            return True
        else:
            return False

    def encender_motor(self):
        check = self.check_engine()

        if self.__encendido and check:
            return '* El motor esta encendido...'
        elif self.__encendido and check == False:
            self.__encendido = False
            return '* Alerta de CHECK ENGINE...'
        else:
            return '* El motor sigue apagado...'