import threading
import multiprocessing
import os
import time

# Función para simular la descarga de un archivo
def descargar_archivo(nombre):
    print(f"Descargando {nombre}...")
    time.sleep(2)
    print(f"{nombre} descargado")

# Función para ejecutar en segundo plano como un demonio
def tarea_demonio():
    while True:
        print("Tarea de demonio en ejecución...")
        time.sleep(5)

if __name__ == "__main__":
    # Crear un hilo para descargar archivos
    hilo_descarga = threading.Thread(target=descargar_archivo, args=("Archivo1.txt",))
    hilo_descarga.start()

    # Crear un proceso para descargar archivos
    proceso_descarga = multiprocessing.Process(target=descargar_archivo, args=("Archivo2.txt",))
    proceso_descarga.start()

    # Crear un demonio para ejecutar una tarea en segundo plano
    demonio = multiprocessing.Process(target=tarea_demonio)
    demonio.daemon = True
    demonio.start()

    # Esperar a que el hilo y el proceso terminen antes de salir
    hilo_descarga.join()
    proceso_descarga.join()

    # El demonio se ejecutará en segundo plano hasta que el programa principal se cierre
    input("Presiona Enter para salir...\n")

