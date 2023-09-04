import pickle

# Definimos una clase para representar el estado de la aplicación
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
