# Application checkpointing
### Introducción:
Generar un programa que sea capaz de restaurar el estado de ejecución.
### Desarrollo:
En este ejemplo, crearemos una clase llamada “AppState” que contiene información sobre el estado de una aplicación ficticia y luego lo guardaremos y restauraremos desde un archivo.
import pickle

# Definimos una clase para representar el estado de la aplicación
```python
 class AppState:
    def __init__(self, user, balance):
        self.user = user
        self.balance = balance

    def __str__(self):
        return f"Usuario: {self.user}, Saldo: ${self.balance}"

# Función para guardar el estado en un archivo
def guardar_estado(estado, archivo):
    with open(archivo, 'wb') as file:
        pickle.dump(estado, file)

# Función para cargar el estado desde un archivo
def cargar_estado(archivo):
    with open(archivo, 'rb') as file:
        estado = pickle.load(file)
    return estado

# Crear una instancia de AppState
estado_actual = AppState("usuario123", 1000.0)

# Guardar el estado actual en un archivo
guardar_estado(estado_actual, 'estado_app.pkl')

# Simular un reinicio de la aplicación
print("Estado actual antes de reiniciar la aplicación:")
print(estado_actual)

# Cargar el estado desde el archivo después del reinicio
estado_recuperado = cargar_estado('estado_app.pkl')

# Mostrar el estado recuperado
print("\nEstado recuperado después del reinicio:")
print(estado_recuperado)
```
En este ejemplo:
1.	Creamos una clase AppState que representa el estado de la aplicación. En este caso, tiene dos atributos: user y balance.
2.	Utilizamos la función guardar_estado para guardar una instancia de AppState en un archivo llamado 'estado_app.pkl'.
3.	Simulamos un reinicio de la aplicación, lo que significa que el estado actual se pierde.
4.	Utilizamos la función cargar_estado para cargar el estado previamente guardado desde el archivo 'estado_app.pkl'.
5.	Mostramos el estado recuperado después del reinicio.
Este ejemplo ilustra cómo puedes crear una clase personalizada para representar el estado de tu aplicación y cómo guardar y cargar ese estado utilizando pickle. Ten en cuenta que este es un ejemplo simple, y en una aplicación real, es posible que necesites serializar y deserializar datos más complejos y gestionar errores y excepciones de manera adecuada.
