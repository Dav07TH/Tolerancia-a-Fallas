# An Introduction to Scaling Distributed Python Applications
*COMPUTACION TOLERANTE A FALLAS*
> Profesor: Michel Emanuel López Franco

> Alumno: Torres Hernández David

> Código: 215428899	     Carrera: INCO			Sección: D06		Fecha: 11/09/2023

## Introducción
Este informe detalla un ejemplo de aplicación en Python que demuestra el uso de hilos, procesos, demonios y concurrencia. Estos conceptos son esenciales en la programación concurrente y se utilizan para aprovechar al máximo los recursos del sistema y mejorar la eficiencia de las aplicaciones.
### Descripción del Programa
El programa desarrollado es una simulación de descarga de archivos concurrente y una tarea en segundo plano. A continuación, se describe en detalle cada aspecto del programa:
### 1.Descarga de Archivos Concurrente

**_Hilos_**

Se crea un hilo utilizando el módulo threading para simular la descarga de un archivo llamado "Archivo1.txt". Los hilos son una forma de lograr la concurrencia en Python y son útiles cuando se trata de tareas que involucran bloqueos de E/S.
import threading
```python
# Función para simular la descarga de un archivo
def descargar_archivo(nombre):
    print(f"Descargando {nombre}...")
    time.sleep(2)
    print(f"{nombre} descargado")
# Crear un hilo para la descarga de Archivo1.txt
hilo_descarga = threading.Thread(target=descargar_archivo, args=("Archivo1.txt",))
hilo_descarga.start()
```
**_Procesos_**

Además, se crea un proceso utilizando el módulo multiprocessing para simular la descarga de otro archivo llamado "Archivo2.txt". Los procesos son útiles para tareas intensivas en CPU, ya que aprovechan múltiples núcleos del procesador.
import multiprocessing
```python
# Función para simular la descarga de un archivo
def descargar_archivo(nombre):
    print(f"Descargando {nombre}...")
    time.sleep(2)
    print(f"{nombre} descargado")
# Crear un proceso para la descarga de Archivo2.txt
proceso_descarga = multiprocessing.Process(target=descargar_archivo, args=("Archivo2.txt",))
proceso_descarga.start()
```
### 2.Tarea de Demonio en Segundo Plano
Se crea un proceso en segundo plano (demonio) utilizando el módulo multiprocessing para ejecutar una tarea en segundo plano. En este caso, la tarea de demonio simplemente muestra un mensaje cada 5 segundos, pero podría ser cualquier tarea que deba ejecutarse en segundo plano.
import multiprocessing
import time
```python
# Función para ejecutar en segundo plano como un demonio
def tarea_demonio():
    while True:
        print("Tarea de demonio en ejecución...")
        time.sleep(5)
# Crear un proceso demonio para ejecutar la tarea en segundo plano
demonio = multiprocessing.Process(target=tarea_demonio)
demonio.daemon = True
demonio.start()
```
### 3.Coordinación y Espera
Para garantizar que el programa principal no finalice antes de que se completen las descargas y permitir que el demonio siga en ejecución en segundo plano, se utilizan las funciones join() para esperar a que tanto el hilo como el proceso terminen.
```python
# Esperar a que el hilo y el proceso de descarga terminen antes de salir
hilo_descarga.join()
proceso_descarga.join()
# El demonio se ejecutará en segundo plano hasta que el programa principal se cierre
input("Presiona Enter para salir...")
```
### Conclusiones
Este ejemplo detallado ilustra cómo utilizar hilos, procesos, demonios y concurrencia en Python para realizar tareas en paralelo y ejecutar operaciones en segundo plano. Cada uno de estos conceptos tiene su propósito y se adapta a diferentes tipos de tareas y requisitos de rendimiento.

El uso adecuado de hilos y procesos depende de las necesidades específicas de la aplicación y de cómo se deben gestionar los recursos del sistema. Los hilos son ideales para tareas de E/S, mientras que los procesos son útiles para tareas intensivas en CPU. Los demonios son útiles para ejecutar tareas en segundo plano de manera continua.

Este programa puede servir como punto de partida para comprender y experimentar con la concurrencia en Python y puede personalizarse y ampliarse según las necesidades del proyecto. La programación concurrente es una técnica valiosa para mejorar la eficiencia y la capacidad de respuesta de las aplicaciones en entornos multiusuario y multitarea.
